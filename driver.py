'''
Usage:
    add_person <person_name> <Fellow|Staff> [wants_room]
    create_room <room_name> <room_type>
    
Options:
    -h, --help  Show this screen and exit
    -i --interactive  Interactive Mode
    
'''

from andela_person.Dojo import Dojo
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
    print ("WELCOME TO THE DOJO ROOM ALLOCATION!".center(70))
    print(__doc__)
    print (border)

def save_state_on_interrupt():
    print("saving state...")
    Dojo.save_state()


class DojoApplication(cmd.Cmd):
    cprint(figlet_format('WELCOME TO THE DOJO', font='banner3-D'), 'cyan', attrs=['bold'])

    prompt = "Dojo >>>"

   

    @docopt_cmd
    def do_add_person(self, arg):
        '''Usage: add_person <FELLOW|STAFF> [wants_accommodation]  '''

        name = arg["<firstname>"]
        fellowstaff = arg["<lastname>"]
        wants_accomodation = arg["--wants_accomodation"]
        Dojo.add_person(name, fellowstaff,str(wants_accomodation))
    @docopt_cmd
    def create_room(self, arg):
        '''Usage: create_room <room_name> <room_type>'''
        room_name = arg["<room_name>"]
        room_type = arg["<room_type>"]
        Dojo.create_room(room_name.upper(), room_type.upper())

   

if __name__ == '__main__':
    introduction()
    try:
        DojoApplication().cmdloop()
    except KeyboardInterrupt:
        save_state_on_interrupt()
