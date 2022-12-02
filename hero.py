class Hero:
    def __init__(self, name, power, magic, punch, kick, special, intelligence):
        self.name = name
        self.power = power
        self.magic = magic
        self.punch = punch
        self.kick = kick
        self.special = special
        self.intelligence = intelligence

    def attack(self, attack):
        if attack == 'power':
            return self.power
        elif attack == 'magic':
            return self.magic
        elif attack == 'punch':
            return self.punch
        elif attack == 'kick':
            return self.kick
        elif attack == 'special':
            return self.special
        elif attack == 'intelligence':
            return self.intelligence
        else:
            return 'Invalid attack'


    def show_skills(self):
        return f"Power: {self.power}\nMagic: {self.magic}\nPunch: {self.punch}\nKick: {self.kick}\nSpecial: {self.special}\nIntelligence: {self.intelligence}"

