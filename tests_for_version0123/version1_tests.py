import unittest
from unittest import TestCase
from andela_person.dojo import Dojo
import unittest.mock as mock
import os
from collections import defaultdict

class TestDojo(TestCase):

    def test_return_random_office_room(self):
        Dojo.create_room('Carmel', 'O')
        Dojo.create_room('Narnia', 'O')
        random_office = Dojo.generate_random_office()
        self.assertIn(random_office, Dojo.office_rooms)


    def test_return_random_ls_room(self):
        Dojo.create_room('PHP', 'L')
        Dojo.create_room('Go', 'L')
        random_ls = Dojo.generate_random_living_space()
        self.assertIn(random_ls, Dojo.ls_rooms)

    def test_reallocate_person(self):
        Dojo.create_room('PHP', 'l')
        Dojo.create_room('NARNIA', 'O')
        Dojo.add_person('steve', 'kanyi', 'F', 'Y')
        self.assertIn('STEVE KANYI', Dojo.ls_rooms['PHP'])
        Dojo.create_room('GO', 'l')
        Dojo.reallocate_person_to_ls('steve kanyi', 'GO')
        self.assertIn('STEVE KANYI', Dojo.ls_rooms['GO'])
        self.assertNotIn('STEVE KANYI', Dojo.ls_rooms['PHP'])

    def test_does_not_reallocate_to_a_full_ls_room(self):
        Dojo.create_room('PHP', 'L')
        Dojo.create_room('NARNIA', 'O')
        previous_count = len(Dojo.ls_rooms['PHP'])
        Dojo.add_person('hellen', 'degenerez', 'F', 'Y')
        Dojo.add_person('viona', 'awuor', 'F', 'Y')
        Dojo.add_person('patrice', 'leah', 'F', 'Y')
        Dojo.add_person('okindo', 'omutka', 'F', 'Y')
        current_count = len(Dojo.ls_rooms['PHP'])
        self.assertEqual(previous_count + 4, current_count)
        Dojo.create_room('GO', 'L')
        Dojo.add_person('anderson', 'masese', 'F', 'Y')
        response = Dojo.reallocate_person_to_ls('Clement Mwendwa', 'PHP')
        self.assertEqual(response, 'PHP is already full')

    def test_does_reallocate_to_same_ls_room(self):
        Dojo.create_room('PHP', 'L')
        Dojo.create_room('NARNIA', 'O')
        Dojo.add_person('Steve', 'Kanyi', 'F', 'Y')
        response = Dojo.reallocate_person_to_ls('Steve Kanyi', 'PHP')
        self.assertEqual(response, 'STEVE KANYI is already allocated to PHP')

    def test_does_not_reallocate_to_a_full_office_room(self):
        Dojo.create_room('Narnia', 'O')
        previous_count = len(Dojo.office_rooms['NARNIA'])
        Dojo.add_person('degenez', 'hellen', 'F')
        Dojo.add_person('viona', 'awuor', 'F')
        Dojo.add_person('patrice', 'leah', 'S')
        Dojo.add_person('okindo', 'omutka', 'F')
        Dojo.add_person('liza', 'muli', 'S')
        Dojo.add_person('justin', 'Mzonge', 'S')
        current_count = len(Dojo.office_rooms['NARNIA'])
        self.assertEqual(previous_count + 6, current_count)
        Dojo.create_room('Carmel', 'O')
        Dojo.add_person('anderson', 'masese', 'F')
        response = Dojo.reallocate_person_to_office('anderson masese', 'NARNIA')
        self.assertEqual(response, 'NARNIA is already full')

    def test_does_reallocate_to_same_office_room(self):
        Dojo.create_room('NARNIA', 'O')
        Dojo.add_person('mundi', 'james', 'F')
        response = Dojo.reallocate_person_to_office('mundi james', 'NARNIA')
        self.assertEqual(response, 'MUNDI JAMES is already allocated to NARNIA')

