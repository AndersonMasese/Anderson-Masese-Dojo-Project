import unittest
from unittest import TestCase
from andela_person.room import *

class TestRoom(TestCase):

    def test_max_ls_occupants(self):
        living_space = LivingSpace('LS')
        self.assertEqual(living_space.max_occupants, 4)
    def test_max_office_occupants(self):
        office = Office('blue')
        self.assertEqual(office.max_occupants, 6)

    def test_room_is_office(self):
        office1 = Office('blue')
        self.assertEqual(office1.room_type.upper(), 'OFFICE')

    def test_room_is_livingspace(self):
        living_space = LivingSpace('LS')
        self.assertEqual(living_space.room_type.upper(), 'LIVINGSPACE')

    def test_room_is_not_empty(self):
        self.assertTrue(True,living_space.Office_existst(),msg='can only allocate non-empty office spaces')
