import unittest
from unittest import TestCase
from andela_person.dojo import Dojo
import unittest.mock as mock
import os
from collections import defaultdict

class TestDojo(TestCase):

    def test_room_does_not_exist(self):
        Dojo.create_room('Venus', 'O')
        self.assertTrue('VENUS' in Dojo.all_rooms)
        response = Dojo.create_room('VENUS', 'O')
        self.assertEqual(response, "Room already exist")

    

    def test_add_person_staff(self):
        Dojo.create_room('MARS', 'O')
        previous_staff_count = len(Dojo.staffs)
        self.assertFalse('MARK ZUCK' in Dojo.all_people)
        Dojo.add_person('MARK', 'ZUCK', 'S')
        self.assertTrue('MARK ZUCK' in Dojo.all_people)
        current_staff_count = len(Dojo.staffs)
        self.assertEqual(previous_staff_count + 1, current_staff_count,  'Person staff has not been added')


    def test_create_office(self):
        previous_room_count = len(Dojo.all_rooms)
        self.assertFalse('Venus' in Dojo.all_rooms)
        Dojo.create_room('Venus', 'O')
        self.assertTrue('Venus'.upper() in Dojo.all_rooms)
        new_room_count = len(Dojo.all_rooms)
        self.assertEqual(previous_room_count + 1, new_room_count)

    def test_create_ls(self):
        previous_room_count = len(Dojo.all_rooms)
        self.assertFalse('Ruby' in Dojo.all_rooms)
        Dojo.create_room('Ruby', 'L')
        self.assertTrue('Ruby'.upper() in Dojo.all_rooms)
        new_room_count = len(Dojo.all_rooms)
        self.assertEqual(previous_room_count + 1, new_room_count)

    def test_add_fellow(self):
        Dojo.create_room('MARS', 'O')
        previous_fellow_count = len(Dojo.fellows)
        self.assertFalse('AMBA MAY' in Dojo.all_people)
        Dojo.add_person('amba', 'may', 'F')
        self.assertTrue('AMBA MAY' in Dojo.all_people)
        current_fellow_count = len(Dojo.fellows)
        self.assertEqual(previous_fellow_count + 1, current_fellow_count, 'Person fellow has not been added')