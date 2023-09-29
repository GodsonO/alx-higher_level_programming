#!/usr/bin/python3
"""
A python script that fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == '__main__':
    import requests
    h = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(h.text.__class__))
    print("\t- content: {}".format(h.text))
