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
    def create_room(room_type,room_name):
        '''
        Check that the room does not exist and determine what type of room it is
        '''
        if room_name in Dojo.all_rooms:
            print('Room already exists')
            return 'Room already exists'
        elif room_type == 'O':
            current_room = Office(room_name)
            Dojo.all_rooms[current_room.room_name.upper()] = current_room.room_type
            Dojo.office_rooms[current_room.room_name.upper()]
            print('Office called %s created succesfully' % room_name)

        elif room_type == 'L':
            current_room = LivingSpace(room_name)
            Dojo.all_rooms[current_room.room_name.upper()] = current_room.room_type
            Dojo.ls_rooms[current_room.room_name.upper()]
            print('Living space called %s created succesfully' % room_name)

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
            if not random_office and not random_ls:
                Dojo.unallocated_person[new_fellow.full_name.upper()] = position
                print('Added %s to the unallocated list' % new_fellow.full_name)
            elif not random_office and random_ls:
                Dojo.unallocated_person[new_fellow.full_name.upper()] = position
                print('Added %s to the unallocated list' % new_fellow.full_name)
                Dojo.ls_rooms[random_ls].append(new_fellow.full_name.upper())
                print("Added: %s and allocated them to a living space %s: " % (new_fellow.full_name, random_ls))
            elif not random_ls and random_office:
                Dojo.unallocated_person[new_fellow.full_name.upper()] = position
                print('Added %s to the unallocated list' % new_fellow.full_name)
                Dojo.office_rooms[random_office].append(new_fellow.full_name.upper())
                print("Added: %s and allocated them to an office %s: " % (new_fellow.full_name, random_office))

            else:
                Dojo.office_rooms[random_office].append(new_fellow.full_name.upper())
                print("Added: %s and allocated them to %s: " % (new_fellow.full_name, random_office))
                Dojo.ls_rooms[random_ls].append(new_fellow.full_name.upper())
                print("Added: %s and allocated them to %s: " % (new_fellow.full_name, random_ls))

        elif position.upper() == 'F':
            new_fellow = Fellow(person_id, firstname, lastname)
            Dojo.all_people[new_fellow.full_name.upper()] = position
            Dojo.fellows.append(new_fellow.full_name.upper())
            random_office = Dojo.generate_random_office()
            if not random_office:
                Dojo.unallocated_person[new_fellow.full_name.upper()] = position
                print('Added %s to the unallocated list' % new_fellow.full_name)
            else:
                Dojo.office_rooms[random_office].append(new_fellow.full_name.upper())
                print("Added: %s and allocated them to %s: " % (new_fellow.full_name, random_office))

        elif position.upper() == 'S' and wants_accomodation.upper() == 'Y':
            new_staff = Staff(person_id, firstname, lastname)
            Dojo.all_people[new_staff.full_name.upper()] = position
            Dojo.staffs.append(new_staff.full_name)
            random_office = Dojo.generate_random_office()
            if not random_office:
                Dojo.unallocated_person[new_staff .full_name.upper()] = position
                print('Added %s to the unallocated list' % new_staff.full_name)
                print('Staff cannot be llocated a living space')
            else:
                Dojo.office_rooms[random_office].append(new_staff.full_name.upper())
                print("Added: %s and allocated them to %s: " % (new_staff.full_name, random_office))
                print('Staff cannot be llocated a living space')

        elif position.upper() == 'S':
            new_staff = Staff(person_id, firstname, lastname)
            Dojo.all_people[new_staff.full_name.upper()] = position
            Dojo.staffs.append(new_staff.full_name.upper())
            random_office = Dojo.generate_random_office()
            if not random_office:
                Dojo.unallocated_person[new_staff.full_name.upper()] = position
                print('Added %s to the unallocated list' % new_staff.full_name)
            else:
                Dojo.office_rooms[random_office].append(new_staff.full_name.upper())
                print("Added: %s and allocated them to %s: " % (new_staff.full_name, random_office))

        else:
            print('%s is not a valid position.' % position)

    @staticmethod
    def load_people(filename):
        '''
        Loads people to the system from a text file.
        '''
        if filename:
            with open(filename) as people_file:
                for line in people_file:
                    people_details = line.split()
                    if len(people_details) == 4:
                        Dojo.add_person(firstname=people_details[0], lastname=people_details[1],
                        position=people_details[2], wants_accomodation=people_details[3])
                    elif len(people_details) == 3:
                        Dojo.add_person(firstname=people_details[0], lastname=people_details[1],
                        position=people_details[2], wants_accomodation='N')
                    else:
                        print('Cannot process the data provided')
        else:
            print('Provide a file, please')

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

    @staticmethod
    def reallocate_person_to_office(full_name, new_room_name):
        '''
        use the person full name to remove the person from one office
        to another
        '''
        full_name = full_name.upper()
        if not full_name in Dojo.all_people:
            return 'The person called %s does not exist' % full_name

        if len(Dojo.office_rooms[new_room_name]) == 6:
            return '%s is already full' % new_room_name

        if full_name in Dojo.office_rooms[new_room_name]:
            return '%s is already allocated to %s' % (full_name, new_room_name)

        for room, members in list(Dojo.office_rooms.items()):
            if full_name in members:
                Dojo.office_rooms[room].remove(full_name)
                Dojo.office_rooms[new_room_name].append(full_name)
                print('%s has been reallocated to %s ' % (full_name, new_room_name))

    @staticmethod
    def reallocate_person_to_ls(full_name, new_room_name):
        '''
        use the person full name to remove the person from one livingspace
        to another, should not reallocate to the same room or a room that is full
        '''
        full_name = full_name.upper()
        if not full_name in Dojo.all_people:
            return 'The person called %s does not exist' % full_name

        if len(Dojo.ls_rooms[new_room_name]) == 4:
            return '%s is already full' % new_room_name

        if full_name in Dojo.ls_rooms[new_room_name]:
            return '%s is already allocated to %s' % (full_name, new_room_name)

        for room, members in list(Dojo.ls_rooms.items()):
            if full_name in members:
                Dojo.ls_rooms[room].remove(full_name)
                Dojo.ls_rooms[new_room_name].append(full_name)
                print('%s has been reallocated to %s ' % (full_name, new_room_name))


    @staticmethod
    def print_room(room_name):
        '''
        prints a room and all the people allocated to that room
        '''
        if room_name.upper() in Dojo.office_rooms.keys():
            print(room_name.upper())
            print('-' * 50)
            print(', '.join(Dojo.office_rooms[room_name.upper()]))

        elif room_name.upper() in Dojo.ls_rooms.keys():
            print(room_name.upper())
            print('-' * 50)
            print(' ,'.join(Dojo.ls_rooms[room_name.upper()]))
        else:
            print('There is no room called %s in Dojo' % room_name)

    @staticmethod
    def print_allocations(filename=''):
        '''
        prints a list of all the people that have been allocated a room
        '''

        if filename:
            with open(filename, 'w') as allocation:
                print("\nWriting to the file .., \n")
                response = 'People in offices \n'
                for room, name in Dojo.office_rooms.items():
                    response = response + (room + '\n')
                    response = response + '-' * 50 + '\n'
                    response = response + (', '.join(name) + '\n')
                    allocation.write(response)

                response = 'People in living space \n'
                for room, name in Dojo.ls_rooms.items():
                    response = response + (room + '\n')
                    response = response + '-' * 50 + '\n'
                    response = response + (', '.join(name) + '\n')
                    allocation.write(response)
        else:
            print('People in office')
            for room, name in Dojo.office_rooms.items():
                print(room)
                print('-' * 50)
                print(', '.join(name))
                print('=' * 50)

            print('People in Living space rooms')
            for room, name in Dojo.ls_rooms.items():
                print(room)
                print('-' * 50)
                print(', '.join(name))
                print('=' * 50)

    @staticmethod
    def print_unallocated(filename=''):
        '''
        prints a list of people that have not been allocated to a room yet
        '''
        if filename:
            with open(filename, 'w') as unallocated:
                print("\nWriting to the file .., \n")
                response = 'People who are not allocated a living space \n'
                response = response + '-' * 50 + '\n'
                response = response + ', '.join(Dojo.unallocated_person)
                unallocated.write(response)
        else:
            print('People not in an room')
            print(', '.join(Dojo.unallocated_person))

    