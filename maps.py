# Course: CS 30
# Period: 1
# Date created: 20/10/16
# Date last modified: 20/10/16
# Name: Brahm Gainda
# Description: RPG modules and maps

from tabulate import tabulate

# defining map
def print_map():
    """Function for printing grid map of Murder Mystery game"""
    map = [['', 'Interrogation Room'],
           ['Empty Fields   ', 'The Gangs House', 'Empty Fields'],
           ['', 'Crime Scene', ]]
    print(tabulate(map, tablefmt="grid"))

# creating a class for the rooms in the map
class Map:
    """Class for different rooms and their relevance"""
    def __init__(self, room, relevance):
        self.room = room
        self.relevance = relevance

    def __str__(self):
        desc = (f"the {self.room} is the room where "
                f"{self.relevance}")
        return desc

# Defining the different rooms
interrogation_room = Map("Interrogation Room", "you interrogate suspects to\
see if their guilty")
the_gangs_house = Map("The Gangs House", "you are being kept\
prisoner till you solve the case")
crime_scene = Map("Crime Scene", "is where the murder occurred\
and where you look for clues")
