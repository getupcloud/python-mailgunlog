python-mailgun
==============

[![Build Status](https://travis-ci.org/getupcloud/python-mailgunlog.png?branch=master)](https://travis-ci.org/getupcloud/python-mailgunlog)

Python Package to retrieve Mailgun logs for a given domain.

## Install

```
pip install mailgunlog
```

## Usage

As a command line tool (use -h for help)

```
$ mailgunlog <domain> <api-key> --begin 2015/01/01 --end 2015/01/31 --json
```

As a python module

```python
import mailgunlog

for log in mailgunlog.logs():
    print json.dumps(log, indent=3)
```

## License

Written by [Getup Cloud](https://getupcloud.com).

Released under the Apache License 2.0: http://opensource.org/licenses/Apache-2.0
