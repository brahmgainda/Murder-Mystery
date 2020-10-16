menu = ['A : Check Suspects List', ' B : Investigate Crime Scene', 
'C : Check Persuasion Points', 'D : Check Time ']

print("Please Select: ")
for menus in menu[:4]:
    print(f'- {menus}'.title())
selection = input()

if selection.lower() == 'a':
    print("Here are the suspects you have left:")
elif selection.lower() == 'b':
    print("You found a new clue at the crime scence its:")
elif selection.lower() == 'c':
    print("You need 10 persuasion points agaonst a suspect to prove to the gang they did it, here how many you have:")
elif selection.lower() == 'd':
    print("The gang only gave you 24 hrs to solve the case, here how much time you have left:")
else:
    print("Unknown Option Selected!")
    