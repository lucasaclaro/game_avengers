def fight(hero_one, hero_two, attack, hero_one_attack, hero_two_attack):
    if hero_one_attack > hero_two_attack:
        return f"{hero_one} attack {hero_two}.\nChosen skill: {attack}.\n{hero_one}: {hero_one_attack}.\n{hero_two}: {hero_two_attack}.\nPOW!!!\n{hero_one} wins!!"
    elif hero_one_attack < hero_two_attack:
        return f"{hero_two} attack {hero_one}\nChosen skill: {attack}\n{hero_one}: {hero_one_attack}\n{hero_two}: {hero_two_attack}\nPOW!!!\n{hero_two} wins!!"
    else:
        return f"{hero_one} attack {hero_two}\nChosen skill: {attack}\n{hero_one}: {hero_one_attack}\n{hero_two}\nPOW!!!\nDraw!!"
