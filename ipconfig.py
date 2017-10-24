'''
The is an external command file used by the shell.

This file is used to retrieve the ip configuration of eth0 as default
If another interface is provided the information will be retrieved
'''

import os


def main(args):
    if args == '':
        info = os.popen('ifconfig eth0')
        result = info.read()
    else:
        info = os.popen('ifconfig ' + args)
        result = info.read()
    return result
