'''
Usage:
    add_person <person_id> <first_name> <last_name> <F|S> [--wants_accomodation=N]
    create_room <room_name> <room_type>
    Usage: reallocate_person <firstname> <lastname> <new_room_name>
    load_people <filename>
    print_allocations [--o=filename]
    print_unallocated [--o=filename]
    print_room <room_name>
    quit

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
    print ("Dojo Space Allocation".center(70))
    print(__doc__)
    print (border)

def save_state_on_interrupt():
    print("saving state...")
    Dojo.save_state()


class DojoApplication(cmd.Cmd):
    cprint(figlet_format('Dojo', font='banner3-D'), 'cyan', attrs=['bold'])

    prompt = "dojo>>"

    @docopt_cmd
    def do_create_room(self, arg):
        '''Usage: create_room <room_type> <room_name>'''
        room_name = arg["<room_name>"]
        room_type = arg["<room_type>"]
        Dojo.create_room(room_type, room_name)

    @docopt_cmd
    def do_add_person(self, arg):
        '''Usage: add_person <firstname> <lastname> <position> [--wants_accomodation=N] '''

        first_name = arg["<firstname>"]
        last_name = arg["<lastname>"]
        pos = arg["<position>"]
        wants_accomodation = arg["--wants_accomodation"]
        Dojo.add_person(first_name, last_name, pos.upper(), str(wants_accomodation))

    @docopt_cmd
    def do_load_people(self, arg):
        ''' Usage: load_people <filename>'''
        file_name = arg["<filename>"]
        if os.path.exists(file_name):
            Dojo.load_people(file_name)
        else:
            print("File not found")

    @docopt_cmd
    def do_reallocate_person(self, arg):
        ''' Usage: reallocate_person <firstname> <lastname> <new_room_name>'''
        first_name = arg["<firstname>"]
        last_name = arg["<lastname>"]
        full_name = first_name + " " + last_name
        new_room = arg["<new_room_name>"]

        if new_room.upper() in Dojo.office_rooms:
            Dojo.reallocate_person_to_office(full_name.upper(), new_room.upper())
        elif new_room.upper() in Dojo.ls_rooms:
            Dojo.reallocate_person_to_ls(full_name.upper(), new_room.upper())
        else:
            print('%s is not a room in Dojo' % new_room)

    @docopt_cmd
    def do_print_room(self, arg):
        ''' Usage: print_room <room_name>'''
        room_name = arg["<room_name>"]
        Dojo.print_room(room_name)

    @docopt_cmd
    def do_print_allocations(self, arg):
        '''Usage: print_allocations [--o=filename] '''
        filename = arg["--o"]

        Dojo.print_allocations(filename)

    @docopt_cmd
    def do_print_unallocated(self, arg):
        '''Usage: print_unallocated [--o=filename] '''
        filename = arg["--o"]

        Dojo.print_unallocated(filename)

    

    @docopt_cmd
    def do_quit(self, arg):
        '''Usage: quit '''
        print("quit")
        exit()


if __name__ == '__main__':
    introduction()
    try:
        DojoApplication().cmdloop()
    except KeyboardInterrupt:
        save_state_on_interrupt()
