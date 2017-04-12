'''
Usage:
    add_person <first_name> <last_name> <status> [--wants_accomodation=N]
    create_room <room_type> <room_name>
    
    quit
Options:
    --help  Show this screen and exi
    --wants_accomodation=<N> [defult: N]
'''

from app.dojo import Dojo
import sys, cmd, os
from termcolor import cprint, colored
from pyfiglet import figlet_format
from docopt import docopt, DocoptExit


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn

border = colored("*" * 20, 'cyan').center(80)
def introduction():
    print (border)
    print ("WELCOME TO DOJO".center(70))
    print(__doc__)
    print (border)

def save_state_on_interrupt():
    print("saving state...")
    Dojo.save_state()


class DojoApplication(cmd.Cmd):
    cprint(figlet_format('THE DOJO', font='banner3-D'), 'cyan', attrs=['bold'])

    prompt = "dojo>>"

    @docopt_cmd
    def do_create_room(self, arg):
        '''Usage: create_room <room_type> <room_name>...'''
        room_type = arg["<room_type>"]
        room_name=arg["<room_name>"]
        Dojo.create_room(room_type, room_name)

    @docopt_cmd
    def do_add_person(self, arg):
        '''Usage: add_person <firstname> <lastname> <status> [--wants_accomodation=N] '''

        first_name = arg["<firstname>"]
        last_name = arg["<lastname>"]
        pos = arg["<status>"]
        wants_accomodation = arg["--wants_accomodation"]
        Dojo.add_person(first_name, last_name, pos.upper(), str(wants_accomodation))

    

   

    @docopt_cmd
    def do_quit(self, arg):
        '''Usage: quit '''
        print("EXITED")
        exit()


if __name__ == '__main__':
    introduction()
    try:
        DojoApplication().cmdloop()
    except KeyboardInterrupt:
        save_state_on_interrupt()
