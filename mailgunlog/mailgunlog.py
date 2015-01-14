# -*- coding: utf-8 -*-

from __future__ import print_function
import sys
import json
import argparse
import time
from datetime import datetime, date as _date
from email.Utils import formatdate
import requests

def logs(domain, api_key, begin=None, end=None):
    url = 'https://api.mailgun.net/v2/%s/events' % domain
    params = {
        'begin': begin or formatdate(),
    }
    if end:
        params['end'] = end
    init = True
    while True:
        if params:
            req = requests.get(url=url, auth=('api', api_key), params=params)
        else:
            req = requests.get(url=url, auth=('api', api_key))
        data = req.json()

        items = data['items']
        for record in items:
            yield record

        if not len(items):
            if init:
                # first iteraction, fetch first page
                url = data['paging']['first']
                params=None
            else:
                # EOF
                return
        else:
            url = data['paging']['next']
        init = False

def strdate_to_rfc2822(value=None, midnight=False):
    '''Convert date in format YYYY/MM/DD to RFC2822 format.
        If value is None, return current utc time.
    '''
    strdate =  value if value else datetime.utcnow().strftime('%Y/%m/%d')
    datetimetuple = map(int, strdate.split('/'))
    if midnight:
        datetimetuple += (23, 59, 59)
    date = datetime(*datetimetuple)
    timestamp = time.mktime(date.utctimetuple())
    return date.strftime('%a, %d %b %Y %H:%M:%S -0000')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Retrieve Mailgun event logs.')
    parser.add_argument('-b', '--begin',   dest='begin',                        default=None,  help='Begin date (YYYY/MM/DD)')
    parser.add_argument('-e', '--end'  ,   dest='end',                          default=None,  help='End date (YYYY/MM/DD)')
    parser.add_argument('-j', '--json',    dest='json',    action='store_true', default=False, help='Print json (original) log records')
    parser.add_argument('domain',  metavar='domain',  type=str, nargs=1, help='Domain registered on Mailgun')
    parser.add_argument('api_key', metavar='api_key', type=str, nargs=1, help='Mailgun API KEY')

    args = parser.parse_args()

    jsondata = {
        'domain': args.domain[0],
        'logs': [],
    }

    begin = strdate_to_rfc2822(args.begin)
    end   = strdate_to_rfc2822(args.end, midnight=True) if args.end else None
    print (begin, end)
    sys.exit()
    if args.begin:
        jsondata['begin'] = begin
    if args.end:
        jsondata['end'] = end

    for log in logs(domain=args.domain[0], api_key=args.api_key[0], begin=begin, end=end):
        if args.json:
            jsondata['logs'].append(log)
        else:
            status = log['event'].upper()
            ok = status in [ 'ACCEPTED', 'DELIVERED' ]
            line = '[%s] %s <%s>' % (datetime.utcfromtimestamp(log['timestamp']), status , log['recipient'])
            if not ok:
                line += '--> "%s"' % log['delivery-status']['description']
            print(line)

    if args.json:
        print(json.dumps(jsondata, indent=3))
