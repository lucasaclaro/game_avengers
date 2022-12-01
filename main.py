from hero import *
from functions import *

captain_america = Hero('Captain America', 88, 28, 89, 80, 74, 82)
black_panther = Hero('Black Panther', 90, 87, 91, 82, 92, 88)
iron_man = Hero('Iron Man', 62, 52, 90, 74, 82, 98)
doctor_strange = Hero('Doctor Strange', 97, 98, 65, 64, 87, 97)

print("Let's fight!!\n")



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

print('')


print('''Choose the number of second character:\n
      [1] Captain America
      [2] Black Panther
      [3] Iron Man
      [4] Doctor Strange   
      ''')
choise_character_two = int(input('Choise: '))

while True:
    if choise_character_two == choise_character_one:
        print('The character has already been chosen. Choose other: ')
        choise_character_two = int(input('Choise: '))
    else:
        if choise_character_two == 1:
            character_two = captain_america
            break
        elif choise_character_two == 2:
            character_two = black_panther
            break
        elif choise_character_two == 3:
            character_two = iron_man
            break
        elif choise_character_two == 4:
            character_two = doctor_strange
            break
        else:
            print('Invalid number! Try again.')
            choise_character_two = int(input('Choise: '))




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
        skill = 'power'
        break
    elif choise_skill == 2:
        skill = 'magic'
        break
    elif choise_skill == 3:
        skill = 'punch'
        break
    elif choise_skill == 4:
        skill = 'kick'
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

print(f'Character one: {character_one.name}.')
print(f'Character two: {character_two.name}.')
print(f'Skill: {skill.title()}.')

if skill == 'Power':
    print(fight(character_one.name, character_two.name, skill, character_one.power, character_two.power))
elif skill == 'Magic':
    print(fight(character_one.name, character_two.name, skill, character_one.magic, character_two.magic))
elif skill == 'Punch':
    print(fight(character_one.name, character_two.name, skill, character_one.punch, character_two.punch))
elif skill == 'Kick':
    print(fight(character_one.name, character_two.name, skill, character_one.kick, character_two.kick))
elif skill == 'Special':
    print(fight(character_one.name, character_two.name, skill, character_one.special, character_two.special))
elif skill == 'Intelligence':
    print(fight(character_one.name, character_two.name, skill, character_one.intelligence, character_two.intelligence))




