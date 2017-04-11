 class IOModule(Object):
 
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

        @staticmethod
        def load_state(db_name):
            '''
            loads the data from database to the app
            '''
            if db_name:
                db = DatabaseCreator(db_name)
            else:
                db = DatabaseCreator('default_db')

            Base.metadata.bind = db.engine

            db_session = db.session

            #load people from database
            people_in_db = select([DojoPersons])
            result = db.session.execute(people_in_db)
            for person in result.fetchall():
                name = person.name
                position = person.position
                Dojo.all_people[name] = position

            db_session.close()

            #load rooms from database
            rooms_in_db = select([DojoRooms])
            result = db.session.execute(rooms_in_db)
            for room in result.fetchall():
                name = room.name
                room_type = room.room_type
                Dojo.all_rooms[name] = room_type

            db_session.close()

            #load office allocations from database
            people_in_offices = select([OfficeAllocations])
            result = db.session.execute(people_in_offices)
            for room in result.fetchall():
                room_name = room.room_name
                member = room.members
                Dojo.office_rooms[room_name]
                if member not in Dojo.office_rooms[room_name]:
                    Dojo.office_rooms[room_name].append(member)

            db_session.close()

            #load living space allocations from database
            people_in_ls = select([LivingSpaceAllocations])
            result = db.session.execute(people_in_ls)
            for person in result.fetchall():
                room_name = person.room_name
                member = person.members
                Dojo.ls_rooms[room_name]
                if member not in Dojo.ls_rooms[room_name]:
                    Dojo.ls_rooms[room_name].append(member)

            db_session.close()

            #load unalloccated people from database
            unallocated_people = select([UnAllocated])
            result = db.session.execute(unallocated_people)
            for person in result.fetchall():
                name = person.name
                if name not in Dojo.unallocated_person:
                    Dojo.unallocated_person.append(name)

            db_session.close()

        @staticmethod
        def save_state(db_name='default_db'):
            '''
            Saves the data in the app to the database
            '''
            if db_name:
                db = DatabaseCreator(db_name)
            else:
                db = DatabaseCreator('default_db')

            Base.metadata.bind = db.engine

            db_session = db.session

            #save people to database
            people_in_db = select([DojoPersons])
            result = db_session.execute(people_in_db)
            people_list = [item.name for item in result]

            for full_name, position in Dojo.all_people.items():
                if full_name not in people_list:
                    new_person = DojoPersons(name = full_name,
                                            position=position)
                    db.session.add(new_person)
                    db.session.commit()

            # saves the rooms to database
            rooms_in_db = select([DojoRooms])
            result = db.session.execute(rooms_in_db)
            rooms_list = [item.name for item in result]

            for room, r_type in Dojo.all_rooms.items():
                if room not in rooms_list:
                    new_room = DojoRooms(name=room,
                                        room_type=r_type)
                    db.session.add(new_room)
                    db.session.commit()

            #saves the people in offices
            peopl_in_office = select([OfficeAllocations])
            result = db.session.execute(peopl_in_office)
            office_people_list = [person.members for person in result]
            for room, members in Dojo.office_rooms.items():
                for member in members:
                    if member not in office_people_list:
                        new_room = OfficeAllocations(room_name=room,
                                                    members=member)
                        db.session.add(new_room)
                        db.session.commit()

            #saves the people in livingspace
            peopl_in_ls = select([LivingSpaceAllocations])
            result = db.session.execute(peopl_in_ls)
            ls_people_list = [person.members for person in result]
            for room, members in Dojo.ls_rooms.items():
                for member in members:
                    if member not in ls_people_list:
                        new_room = LivingSpaceAllocations(room_name=room,
                                                    members=member)
                        db.session.add(new_room)
                        db.session.commit()

            #saves the fellow who are not allocated a livingspace
            unallocated_people = select([UnAllocated])
            result = db.session.execute(unallocated_people)
            unallocated_people_list = [person.name for person in result]
            for person in Dojo.unallocated_person:
                if person not in unallocated_people_list:
                    new_room = UnAllocated(name=person)

                    db.session.add(new_room)
                    db.session.commit()
