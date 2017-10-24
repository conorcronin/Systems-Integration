'''
This is an external command file used by the shell to find the current working directory
The current working directory will be returned to the main shell
'''

import os


def main():
    cwd = os.getcwd()
    return cwd
