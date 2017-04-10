import unittest
from unittest import TestCase
from andela_person.dojo import Dojo
import unittest.mock as mock
import os
from collections import defaultdict

class TestDojo(TestCase):
    @mock.patch('andela_person.Dojo.open')
    def test_load_people_calls_open_function(self, mock_open):
        Dojo.load_people('data/people.txt')
        mock_open.assert_called_with('data/people.txt')

    def test_load_people_read_lines(self):
        dirname = os.path.dirname(os.path.realpath(__file__))
        with mock.patch.object(Dojo, 'add_person') as mock_method:
            Dojo.load_people(os.path.join(dirname, 'data/people.txt'))
        mock_method.assert_any_call(firstname='OLUWAFEMI', lastname='SULE', position='F', wants_accomodation='Y')
        mock_method.assert_any_call(firstname='LEIGH', lastname='RILEY', position='S', wants_accomodation='N')
        self.assertEqual(mock_method.call_count, 7)
