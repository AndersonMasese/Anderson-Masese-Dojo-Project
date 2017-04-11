class Dojo(Object):

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
                    Dojo.ls_rooms[room].remove(full_name)y
                    Dojo.ls_rooms[new_room_name].append(full_name)
                    print('%s has been reallocated to %s ' % (full_name, new_room_name))