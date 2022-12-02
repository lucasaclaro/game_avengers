from time import sleep

def fight(hero_one, hero_two, attack, hero_one_attack, hero_two_attack):
    if hero_one_attack > hero_two_attack:
        print(f"{hero_one} attack {hero_two}!")
        sleep(1)
        print(f"\n\n{hero_one} has {hero_one_attack} points of {attack}.\n{hero_two} has {hero_two_attack} points of {attack}.")
        sleep(1)
        print('POW!!!')
        sleep(2)
        print(f"{hero_one} wins!!")
    elif hero_one_attack < hero_two_attack:
        print(f"{hero_two} attack {hero_one}!")
        sleep(1)
        print(f"\n\n{hero_two} has {hero_two_attack} points of {attack}.\n{hero_one} has {hero_one_attack} points of {attack}.")
        sleep(1)
        print('POW!!!')
        sleep(2)
        print(f"{hero_two} wins!!")
    else:
        print(f"{hero_two} attack {hero_one}!")
        sleep(1)
        print(f"\n\n{hero_two} has {hero_two_attack} points of {attack}.\n{hero_one} has {hero_one_attack} points of {attack}.")
        sleep(1)
        print('POW!!!')
        sleep(2)
        print(f"Draw!!")
