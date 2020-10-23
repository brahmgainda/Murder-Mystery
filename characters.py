# Course: CS 30
# Period: 1
# Date created: 20/10/19
# Date last modified: 20/10/23
# Name: Brahm Gainda
# Description: RPG Classes

from tabulate import tabulate

# Classes For Suspects
class Suspect:
    """Parent class for primary/secondary suspects"""
    def __init__(self, name, trait):
        self.name = name
        self.trait = trait


class PrimarySuspect(Suspect):
    """Class for primary suspects"""
    def __init__(self, name, trait):
        super().__init__(name, trait)

    def __str__(self):
        desc = (f"{self.name} is very {self.trait}\n"
                f"{self.name} is a primary suspect, theres a\
                high chance they committed the crime...")
        return desc


class SecondarySuspect(Suspect):
    """Class for secondary suspects"""
    def __init__(self, name, trait):
        super().__init__(name, trait)

    def __str__(self):
        desc = (f"{self.name} is very {self.trait}\n"
                f"{self.name} is a secondary suspect, theres a\
                lower chance they committed the crime...")
        return desc

# Defining the different suspects
bill = PrimarySuspect("Bill", "high tempered")
shaniqua = PrimarySuspect("Shaniqua", "manipulative")
steven = PrimarySuspect("Steven", "shy")
sam = PrimarySuspect("Sam", "high tempered")
timmy = SecondarySuspect("Tim", "loud")
chad = SecondarySuspect("Chad", "fidgety")


# Map Class
def print_map():
    """Function for printing grid map of Murder Mystery game"""
    map = [['', 'Interrogation Room'],
           ['Empty Fields   ', 'The Gangs House(start)', 'Empty Fields'],
           ['', 'Crime Scene', 'Police Station(end)']]
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
empty_fields = Map("Empty Fields", "you go to think in silence")

message = "Where would you like to go first?\
Interrogation Room, The Gangs House, Crime Scene, Empty Fields "

keypress = input(message)

# map
if keypress.lower() == "map":
    print_map()
if keypress.lower() == "interrogation room":
    print(interrogation_room)
if keypress.lower() == "the gangs house":
    print(the_gangs_house)
if keypress.lower() == "crime scene":
    print(crime_scene)
if keypress.lower() == "empty fields":
    print(empty_fields)
