from .person import *
from .room import *
import random


class Dojo(object):
    office_rooms = defaultdict(list)
    ls_rooms = defaultdict(list)
    all_rooms  = {}
    staffs = []
    fellows = []
    all_people = {}
    unallocated_person = {}



    @staticmethod
    def create_room(room_type, room_name):
        #global new_room=room_type
        #global new_name=room_name[0]
        '''
        Check that the room does not exist and determine what type of room it is
        '''
        for i in room_name:
            print('%s called %s has been succesfully created!' %(room_type,i) )
            

        #print(add_room_to_dict())

    @staticmethod
    def add_room_to_dict():
        '''
        Check that the room does not exist and determine what type of room it is
        '''
        #global new_room
        #global new_name
        #print(new_room)

   


    @staticmethod
    def add_person(firstname, lastname, position, wants_accomodation='N'):
        '''
        Add person details to the system
        '''
        full_name = firstname + " " + lastname
        person_id = len(list(Dojo.all_people)) + 1

        if full_name.upper() in Dojo.all_people:
            print ('Person with %s id already exist.' % full_name)

        elif position.upper() == 'F' and wants_accomodation.upper() == 'Y':
            new_fellow = Fellow(person_id, firstname, lastname)
            Dojo.all_people[new_fellow.full_name.upper()] = position
            Dojo.fellows.append(new_fellow.full_name.upper())
            random_office = Dojo.generate_random_office()
            random_ls = Dojo.generate_random_living_space()

            Dojo.office_rooms[random_office].append(new_fellow.full_name.upper())
            print("Added: %s and allocated them to %s: " % (new_fellow.full_name, random_office))
            Dojo.ls_rooms[random_ls].append(new_fellow.full_name.upper())
            print("Added: %s and allocated them to %s: " % (new_fellow.full_name, random_ls))

        elif position.upper() == 'F':
            new_fellow = Fellow(person_id, firstname, lastname)
            Dojo.all_people[new_fellow.full_name.upper()] = position
            Dojo.fellows.append(new_fellow.full_name.upper())
            random_office = Dojo.generate_random_office()
        
            Dojo.office_rooms[random_office].append(new_fellow.full_name.upper())
            print("Added: %s and allocated them to %s: " % (new_fellow.full_name, random_office))

        

        elif position.upper() == 'S':
            new_staff = Staff(person_id, firstname, lastname)
            Dojo.all_people[new_staff.full_name.upper()] = position
            Dojo.staffs.append(new_staff.full_name.upper())
            random_office = Dojo.random.generate_random_office()
            
            Dojo.office_rooms[random_office].append(new_staff.full_name.upper())
            print("Added: %s and allocated them to %s: " % (new_staff.full_name, random_office))

        else:
            print('%s is not a valid position.' % position)

    @staticmethod
    def generate_random_office():
        '''
        Generates a random office that is not full
        '''
        available_offices = [room for room in Dojo.office_rooms if len(Dojo.office_rooms[room]) < 6]

        if len(available_offices) > 0:
            random_office = random.choice(available_offices)
            return random_office
        else:
            print('No offices availble')

    @staticmethod
    def generate_random_living_space():
        '''
        Generate a random living space that is not full_occupied
        '''
        available_ls = [room for room in Dojo.ls_rooms if len(Dojo.ls_rooms[room]) < 4]

        if len(available_ls) > 0:
            random_ls = random.choice(available_ls)
            return random_ls
        else:
            print('No living space available')

  