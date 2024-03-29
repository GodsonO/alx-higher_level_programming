#!/usr/bin/python3
"""A script that
- fetches https://alx-intranet.hbtn.io/status.
"""


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        bodycontent = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(bodycontent)))
        print("\t- content: {}".format(bodycontent))
        print("\t- utf8 content: {}".format(bodycontent.decode('utf-8')))
