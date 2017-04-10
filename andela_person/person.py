"""Class person is the parent class to the classes Fellow and Class Staff from which the application driver 
class driver presents command line interface

"""


class Person(object):
    
    def __init__(self,fname, lname, index=''):
        self.fname = fname
        self.lname = lname
        self.index = index
        self.full_name = self.fname + " " + self.lname


class Staff(Person):

    def __init__(self, *args, **kwargs):
        super(Staff, self).__init__(*args, index = 'Staff')
class Fellow(Person):

    def __init__(self, *args, **kwargs):
        super(Fellow, self).__init__(*args, index = 'Fellow')
