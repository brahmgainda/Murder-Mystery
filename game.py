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
