python-mailgun
==============

[![Build Status](https://travis-ci.org/getupcloud/python-mailgunlog.png?branch=master)](https://travis-ci.org/getupcloud/python-mailgunlog)

Python Package to retrieve Mailgun logs for a given domain.

## Install

```
pip install mailgunlog
```

## Usage

### Command line tool

As a command line tool (use -h for help):

```
$ mailgunlog <domain> <api-key> --begin 2015/01/01 --end 2015/01/31 --json
```

If your prefer, call it as an executable module:

```
$ python -m mailgunlog <domain> <api-key> --begin 2015/01/01 --end 2015/01/31
```

In order to keep it a little bit secure, define your API Key and Domain from environment variables:

```
$ export MAILGUN_DOMAIN=example.com
$ export MAILGUN_API_KEY=<mailgunapi-key-goes-here>
```

Now it's possible to dump logs from an specific number of days ago:

```
$ python -m mailgunlog <domain> <api-key> --days 5
```

### Module

You can use it inside your project, as a python module:

```python
import mailgunlog

for log in mailgunlog.logs():
    print json.dumps(log, indent=3)
```

## License

Written by [Getup Cloud](https://getupcloud.com).

Released under the Apache License 2.0: http://opensource.org/licenses/Apache-2.0
