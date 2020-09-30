# Course: CS 30
# Period: 1
# Date created: 20/09/20
# Date last modified: 20/09/21
# Name: Brahm Gainda
# Description: RPG Numerical list

# Define the lists

suspects = ['Bill', 'Shaniqua', 'Steven', 'Sam']
clues = ['Bills shoe at crime scene', 'Bills DNA at crime scene']
extra_suspects = ['Timmy', 'Chad']
extra_clues = ['Sams hair at the crime scene', 'Gun with Bills finger prints']

# Set up numerical lists to print one iteam per line


def numer_list(name, list):
    print(f"{name}:")
    for index, value in enumerate(list):
        print(f"{index + 1}: {value.capitalize()}")

# Print numerical list with one iteam per line

numer_list('Suspects', suspects)
numer_list("Clues", clues)
numer_list("Extra Clues", extra_clues)
numer_list("Extra Supects", extra_suspects)

# Dictonary for characters

characters = {1: {'name': 'Barb', 'age': '21', 'sex': 'Male',
              'relevance': 'Detective', 'trait': 'magnificent at theyre work'},
              2: {'name': 'bill', 'age': '24', 'sex': 'Male',
              'relevance': 'Suspect', 'trait': 'friendly'},
              3: {'name': 'sam', 'age': '19', 'sex': 'Male',
              'relevance': 'Suspect', 'trait': 'short-tempered'},
              4: {'name': 'Steven', 'age': '28', 'sex': 'Male',
              'relevance': 'Suspect', 'trait': 'quiet'},
              5: {'name': 'Shaniqua', 'age': '18', 'sex': 'Female',
              'relevance': 'Suspect', 'trait': 'manipulative'},
              6: {'name': 'Timmy', 'age': '31', 'sex': 'Male',
              'relevance': 'extra Suspect', 'trait': 'impulsive'},
              7: {'name': 'Chad', 'age': '23', 'sex': 'Male',
              'relevance': 'extra Suspect', 'trait': 'short-tempered'}}

for character, character_info in characters.items():
    name = character_info['name'].title()
    age = character_info['age']
    sex = character_info['sex']
    relevance = character_info['relevance']
    trait = character_info['trait']

    print("\n" + name.title() + " is a " + age + " year old " + sex)
    print(" They are a " + relevance + " in the case.")
    print(" They are considerably " + trait + " .")

# Dictionary For Inventory

print('\n\n')

inventory = []

clue = {
    'item': 'Bills DNA',
    'description': 'clue found at the crime scene',
    'persuasion_points': 2,
    }
inventory.append(clue)

clue = {
    'item': 'Bills shoe',
    'description': 'a clue found at the crime scene',
    'persuasion_points': 2,
    }

inventory.append(clue)

clue = {
    'item': 'Sams hair',
    'description': 'extra clue that was hidden at the crime \
scene',
    'persuasion_points': 4,
    }
inventory.append(clue)

clue = {
    'item': 'a gun with Bills finger prints',
    'description': 'extra clue at the \
crime scene',
    'persuasion_points': 4,
    }
inventory.append(clue)


for inventory in inventory:
    print("\n you found " + inventory['item'])
    print(" thats a " + inventory['description'] + ".")
    print(" It has " + str(inventory['persuasion_points']) +
          " persuasion points.")

# Dictionary For Locations and Descriptions

print('\n\n')

locations = []

description = {
    'location_name': 'New York City',
    'description': ' you and the deadly gang live, and where the game is set.',
    }
locations.append(description)

description = {
    'location_name': 'Chuck E Cheese',
    'description': ' the murder occurred and where you look for \
clues',
    }
locations.append(description)


description = {
    'location_name': 'An Abandoned Warehouse on the outskirts of the city',
    'description': ' the deadly gang that has \
kidnapped you lives.',
    }
locations.append(description)

description = {
    'location_name': 'A room in the abandoned warehouse',
    'description': ' you interrogate the suspects.',
    }
locations.append(description)

for location in locations:
    print("\n" + location['location_name'])
    print("is where" + location['description'])
