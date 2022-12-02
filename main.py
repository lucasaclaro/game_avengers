from hero import *
from functions import *
from random import randint
from time import sleep

captain_america = Hero('Captain America', 88, 28, 89, 80, 74, 82)
black_panther = Hero('Black Panther', 90, 87, 91, 82, 92, 88)
iron_man = Hero('Iron Man', 62, 52, 90, 74, 82, 98)
doctor_strange = Hero('Doctor Strange', 97, 98, 65, 64, 87, 97)


print('\n\n****** Avengers Game ******\n\n')
sleep(2)

print("Let's fight!!\n")
sleep(2)


print('''Choose the number of first character:\n
      [1] Captain America
      [2] Black Panther
      [3] Iron Man
      [4] Doctor Strange   
      ''')
choise_character_one = int(input('Choise: '))

while True:
    if choise_character_one == 1:
        character_one = captain_america
        break
    elif choise_character_one == 2:
        character_one = black_panther
        break
    elif choise_character_one == 3:
        character_one = iron_man
        break
    elif choise_character_one == 4:
        character_one = doctor_strange
        break
    else:
        print('Invalid number! Try again.')
        choise_character_one = int(input('Choise: '))
sleep(1)
print('')
print(f'Skills of {character_one.name}:\n{character_one.show_skills()}\n')


list_characters = [1, 2, 3, 4]
list_characte


character_two = randint(1, 4)

if character_two == character_one:
    character_two = randint(1, 4)
else:
    if character_two == 1:
        character_two = captain_america
    elif character_two == 2:
        character_two = black_panther
    elif character_two == 3:
        character_two = iron_man
    elif character_two == 4:
        character_two = doctor_strange


print('''Choose the skill:\n
      [1] Power
      [2] Magic
      [3] Punch
      [4] Kick
      [5] Special
      [6] Intelligence   
      ''')
choise_skill = int(input('Choise: '))
while True:
    if choise_skill == 1:
        skill = 'Power'
        break
    elif choise_skill == 2:
        skill = 'Magic'
        break
    elif choise_skill == 3:
        skill = 'Munch'
        break
    elif choise_skill == 4:
        skill = 'Kick'
        break
    elif choise_skill == 5:
        skill = 'Special'
        break
    elif choise_skill == 6:
        skill = 'Intelligence'
        break
    else:
        print('Invalid number! Try again.')
        choise_skill = int(input('Choise: '))
sleep(2)
print('---------'*5)
print(f'\nYou chose: {character_one.name} for attack with {skill}.')
print(f'\nPC chose: {character_two.name}.')
print('---------'*5)
print(f'\n***Battle between {character_one.name} VS {character_two.name}***\n')
sleep(2)
if skill == 'Power':
    fight(character_one.name, character_two.name, skill, character_one.power, character_two.power)
elif skill == 'Magic':
    fight(character_one.name, character_two.name, skill, character_one.magic, character_two.magic)
elif skill == 'Punch':
    fight(character_one.name, character_two.name, skill, character_one.punch, character_two.punch)
elif skill == 'Kick':
    fight(character_one.name, character_two.name, skill, character_one.kick, character_two.kick)
elif skill == 'Special':
    fight(character_one.name, character_two.name, skill, character_one.special, character_two.special)
elif skill == 'Intelligence':
    fight(character_one.name, character_two.name, skill, character_one.intelligence, character_two.intelligence)




