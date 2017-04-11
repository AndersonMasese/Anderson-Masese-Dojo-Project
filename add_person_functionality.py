@staticmethod
    def add_person(firstname, lastname, position, wants_accomodation='N'):
        '''
        Add person details to the system
        '''
        full_name = firstname + " " + lastname
        person_id = len(list(Amity.all_people)) + 1

        if full_name.upper() in Amity.all_people:
            print ('Person with %s id already exist.' % full_name)

        elif position.upper() == 'F' and wants_accomodation.upper() == 'Y':
            new_fellow = Fellow(person_id, firstname, lastname)
            Amity.all_people[new_fellow.full_name.upper()] = position
            Amity.fellows.append(new_fellow.full_name.upper())
            random_office = Amity.generate_random_office()
            random_ls = Amity.generate_random_living_space()
            if not random_office and not random_ls:
                Amity.unallocated_person[new_fellow.full_name.upper()] = position
                print('Added %s to the unallocated list' % new_fellow.full_name)
            elif not random_office and random_ls:
                Amity.unallocated_person[new_fellow.full_name.upper()] = position
                print('Added %s to the unallocated list' % new_fellow.full_name)
                Amity.ls_rooms[random_ls].append(new_fellow.full_name.upper())
                print("Added: %s and allocated them to a living space %s: " % (new_fellow.full_name, random_ls))
            elif not random_ls and random_office:
                Amity.unallocated_person[new_fellow.full_name.upper()] = position
                print('Added %s to the unallocated list' % new_fellow.full_name)
                Amity.office_rooms[random_office].append(new_fellow.full_name.upper())
                print("Added: %s and allocated them to an office %s: " % (new_fellow.full_name, random_office))

            else:
                Amity.office_rooms[random_office].append(new_fellow.full_name.upper())
                print("Added: %s and allocated them to %s: " % (new_fellow.full_name, random_office))
                Amity.ls_rooms[random_ls].append(new_fellow.full_name.upper())
                print("Added: %s and allocated them to %s: " % (new_fellow.full_name, random_ls))

        elif position.upper() == 'F':
            new_fellow = Fellow(person_id, firstname, lastname)
            Amity.all_people[new_fellow.full_name.upper()] = position
            Amity.fellows.append(new_fellow.full_name.upper())
            random_office = Amity.generate_random_office()
            if not random_office:
                Amity.unallocated_person[new_fellow.full_name.upper()] = position
                print('Added %s to the unallocated list' % new_fellow.full_name)
            else:
                Amity.office_rooms[random_office].append(new_fellow.full_name.upper())
                print("Added: %s and allocated them to %s: " % (new_fellow.full_name, random_office))

        elif position.upper() == 'S' and wants_accomodation.upper() == 'Y':
            new_staff = Staff(person_id, firstname, lastname)
            Amity.all_people[new_staff.full_name.upper()] = position
            Amity.staffs.append(new_staff.full_name)
            random_office = Amity.generate_random_office()
            if not random_office:
                Amity.unallocated_person[new_staff .full_name.upper()] = position
                print('Added %s to the unallocated list' % new_staff.full_name)
                print('Staff cannot be llocated a living space')
            else:
                Amity.office_rooms[random_office].append(new_staff.full_name.upper())
                print("Added: %s and allocated them to %s: " % (new_staff.full_name, random_office))
                print('Staff cannot be llocated a living space')

        elif position.upper() == 'S':
            new_staff = Staff(person_id, firstname, lastname)
            Amity.all_people[new_staff.full_name.upper()] = position
            Amity.staffs.append(new_staff.full_name.upper())
            random_office = Amity.generate_random_office()
            if not random_office:
                Amity.unallocated_person[new_staff.full_name.upper()] = position
                print('Added %s to the unallocated list' % new_staff.full_name)
            else:
                Amity.office_rooms[random_office].append(new_staff.full_name.upper())
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
        if not full_name in Amity.all_people:
            return 'The person called %s does not exist' % full_name

        if len(Amity.office_rooms[new_room_name]) == 6:
            return '%s is already full' % new_room_name

        if full_name in Amity.office_rooms[new_room_name]:
            return '%s is already allocated to %s' % (full_name, new_room_name)

        for room, members in list(Amity.office_rooms.items()):
            if full_name in members:
                Amity.office_rooms[room].remove(full_name)
                Amity.office_rooms[new_room_name].append(full_name)
                print('%s has been reallocated to %s ' % (full_name, new_room_name))

    @staticmethod
    def reallocate_person_to_ls(full_name, new_room_name):
        '''
        use the person full name to remove the person from one livingspace
        to another, should not reallocate to the same room or a room that is full
        '''
        full_name = full_name.upper()
        if not full_name in Amity.all_people:
            return 'The person called %s does not exist' % full_name

        if len(Amity.ls_rooms[new_room_name]) == 4:
            return '%s is already full' % new_room_name

        if full_name in Amity.ls_rooms[new_room_name]:
            return '%s is already allocated to %s' % (full_name, new_room_name)

        for room, members in list(Amity.ls_rooms.items()):
            if full_name in members:
                Amity.ls_rooms[room].remove(full_name)
                Amity.ls_rooms[new_room_name].append(full_name)
                print('%s has been reallocated to %s ' % (full_name, new_room_name))