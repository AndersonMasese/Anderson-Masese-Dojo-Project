"""
using collections to avoid throwing a key error wherever we try using a non-existent key, insert the non_existent key instead

"""
from collections import defaultdict

class Room(object):
    


    def __init__(self, r_name='', r_type='', maximum_occumpants=0):
        self.r_name = r_name
        self.r_type = r_type
        self.maximum_occupants = maximum_occupants


class Office(Room):

    def __init__(self, *args, **kwargs):
        super(Office, self).__init__(*args, r_type='OFFICE', maximum_occupants=6)


class LivingSpace(Room):

    def __init__(self, *args, **kwargs):
        super(LivingSpace, self).__init__(*args, r_type='LIVINGSPACE', maximum_occupants=4)
