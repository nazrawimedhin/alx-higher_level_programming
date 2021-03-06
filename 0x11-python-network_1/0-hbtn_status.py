#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
from urllib import request


if __name__ == '__main__':
    with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        data = response.read()
        print(f'Body response:\n\t- type: {type(data)}')
        print(f'\t- content: {data}\n\t- utf8 content: {data.decode("utf-8")}')
