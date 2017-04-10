"""
These unit test is modelled around a modelled project
For example, andela_person will be a folder containing files such as person from which everything has been imported
"""
import unittest
from unittest import TestCase
from andela_person.person import *#andela_person will be a directory

class TestPerson(TestCase):

    def test_fellow(self):
        fellow = Fellow('anderson', 'masese')
        self.assertEqual(fellow.position.upper(), 'FELLOW', msg='The position must be a fellow')

    def test_staff(self):
        staff = Staff('mark', 'homes')
        self.assertEqual(staff.position.upper(), 'STAFF', msg='The position must be a staff')

    def test_must_be_staff_or_fellow(self):
        anonymous=Anon()
        self.assertIsNotEmpty(True,Anon(),msg='Function Anon should return something to avoid allocating rooms to persons who are neither staff nor students')
