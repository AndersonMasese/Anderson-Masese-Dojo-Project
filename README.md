
##**Week 2 Andela Boot Camp dojo project**
####_Andela Checkpoint 1 Project Requirements_

**_Andela cohort xvii Boot camp project_**




**Introduction**
Requirements
To complete this application you’ll need to know Programming Basics, Data Structures, Object-Oriented Programming (OOP) and Test Driven Development (TDD) in Python. 
You are advised to consult the learning resources shared with you, other cool resources you find online and your learning community to level up on these concepts.

**Problem Description**
When a new Fellow joins Andela they are assigned an office space and an optional living space if they choose to opt in. When a new Staff joins they are assigned an office space only. In this exercise you will be required to digitize and randomize a room allocation system for one of Andela Kenya’s facilities called The Dojo.

**Constraints**
The Dojo has rooms, which can be offices or living spaces. An office can accommodate a maximum of 6 people. A living space can accommodate a maximum of 4 people.

A person to be allocated could be a fellow or staff. Staff cannot be allocated living spaces. Fellows have a choice to choose a living space or not.

This system will be used to automatically allocate spaces to people at random.

**Expectations***
By the end of Task 3 you should have created the following classes and implemented the required functionality within them - Person, Fellow, Staff, Dojo, Room, Office, LivingSpace

Ensure that you are properly structuring your class files and using easily navigable folder structures.
It’s highly recommended that you have UML Class Diagrams for your system. Keep the diagrams in a /designs folder.

Practise Test Driven Development. What this means is that you will be writing unit tests before you create functionality. 

You are free to add on extra functionality beyond what’s specified in the specifications. You are encouraged to do this to exceed expectations.






**Task 0 - Version 0 of the System***
For this task you are required to create a command line interface using docopt that has the following commands:

create_room <room_type> <room_name>... - Creates rooms in the Dojo. 
Using this command, the user should be able to create as many rooms as possible by specifying multiple room names after the create_room command.

 Sample input with one office
1.create_room office Orange

# Sample output with one office
1.An office called Orange has been successfully created!

# Sample input with multiple offices
1.create_room office Blue Black Brown

# Sample output with multiple offices
1.An office called Blue has been successfully created!
1.An office called Black has been successfully created!
1.An office called Brown has been successfully created!

add_person <person_name> <FELLOW|STAFF> [wants_accommodation] - Adds a person to the system and allocates the person to a random room. 
wants_accommodation here is an optional argument which can be either Y or N. The default value if it is not provided is N.

# Sample input for adding Staff
_add_person Neil Armstrong Staff_

# Sample output for adding Staff
1.Staff Neil Armstrong has been successfully added.
2.Neil has been allocated the office Blue

# Sample input for adding Fellow with accommodation option

_addperson Nelly Armweek Fellow Y_

# Sample output for adding Fellow with accommodation option

1.Fellow Nelly Armweek has been successfully added.
1.Nelly has been allocated the office Blue
1.Nelly has been allocated the livingspace Python




###Instructions for install and usage


1.create_room <room_name>... - Creates a room in the Dojo. This command can create as many rooms as possible by specifying multiple room names
1.add_person <firstname> <lastname> <F|S> [--wants_accomodation=N] - Add a person to the system and allocates the person to a random room
1.reallocate_person <person_identifier> <new_room_name> - Reallocate the person with person with person_identifier to new_room_name
1.load_people - Adds people to rooms from a text file
1.print_allocations [-o=filename] - Prints a list of allocations onto the screen. Specifying the optional -o option here outputs the information to the text 1.file provided
1.print_unallocated [-o=filename] - Prints a list of unallocated people to the screen. Specifying the -o option here outputs the information to the text file provided
1.print_room <room_name> - Prints the names of the people in room_name on the screen
1.save_state [--db=sqlite_database] - Persists all the data stored in the app to a SQLite database. Specifying the --db parameter explicitly stores the data in the sqlite_database specified.
1.load_state <sqlite_database> - Loads data from a database into the application.

####Installation & Setup

1.Download & Install Python
Head over to the Python Downloads Site and download a version compatible with your operating system
1.To confirm that you have successfully installed Python:
1.Open the Command Propmpt on Windows or Terminal on Mac/Linux
1.Type python
1.If the Python installation was successfull you the Python version will be printed on your screen and the python REPL will start
1.Clone the repository to your personal computer to any folder
1.Url - https://github.com/AndersonMasese/Anderson-Masese-Dojo-Project
1.Enter the terminal on Mac/Linux or Git Bash on Windows
1.Type git clone and paste the URL
1.Virtual Environment Installation
1.Install the virtual environment by typing: pip install virtualenv on your terminal
1.Install the required modules
1.Inside the directory where you cloned the repository run pip install -r requirements.txt
1.Inside the application folder run the driver.py file:
1.On the terminal type python driver.py  to start the application


