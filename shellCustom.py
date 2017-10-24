'''
Create a custom shell for Systems Integration CA
Author : Conor Cronin
Date 18/10/2017

Create an executable shell that locks down user functionality
pwd and ifconfig should be executed as external commands
'''

import getpass, time, datetime, os, pwdfile, ipconfig
from cmd import Cmd


class CustomShell(Cmd):

    def welcomescreen(self):
        username = getpass.getuser()
        print("Welcome Conor's Custom Shell: %s\n" % username)
        print("If you would like some help please type 'helpme'.\n")
        print('Please enter a command to begin:')

    def do__dt(self):
        i = datetime.datetime.now()
        print('The date and time are as follows (YYMMDDHHMMSS): %s%s%s%s%s%s\n' %
              (i.year, i.day, i.month, i.hour, i.minute, i.second))

    def do_ud(self):
        dir = os.getenv("HOME")
        dirinfo = os.stat(dir)
        inode_id = dirinfo.st_ino
        print('Your user details are as follows: \nUser Id: %s\nGroup ID: %s\nUsername: %s\n'
              'Groupname: %s\niNode of directory: %s\n' %
              (os.getuid(), os.getgid(), os.uname(), os.getgroups(), inode_id))

    def do_ifc(self, args):
        if args == '':
            config = ipconfig.main(args)
            print('Your network configuration for eth0 is: %s\n' % config)
        else:
            config = ipconfig.main(args)
            print('The information for %s is:' % args, config)

    def do_pw(self):
        cwd = pwdfile.main()
        print('Your current working directory is: %s\n' % cwd)

    def do_whereami(self):
        print("********************************")
        print("                                ")
        print("You are in Conor's Custom Shell.")
        print("                                ")
        print("********************************")

    def do_exit(self):
        answer = input('Are you sure you want to exit? (y/n)\n')
        if answer == 'y':
            print('Thank you for using the custom shell, good bye!')
            time.sleep(3)
            os._exit(1)
        elif answer == 'n':
            CustomShell.welcomescreen(self)

    def do_helpme(self):
        print('Hello there, it seems you need some help!\n'
              'Please choose from one of the following commands:\n')
        print(' ___________________________________________________')
        print('|COMMAND     |       OUTPUT                         |')
        print('|____________|______________________________________|')
        print('|whereami    -       Displays shell information     |')
        print('|dt          -       Displays current time and date |')
        print('|ud          -       Displays user information      |')
        print('|ifc         -       Displays ip configuration      |')
        print('|                    information for eth0 as default|')
        print('|                    User can specify interface also|')
        print('|pw          -       Displays information of current|')
        print('|                    working directory              |')
        print('|___________________________________________________|')


main = CustomShell()
main.cmdloop()
