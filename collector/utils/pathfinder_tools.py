import math

FONTSET = ['Roboto', 'Ubuntu', 'Neuton', 'Raleway:wght@300;500;800&display=swap', 'UnifrakturMaguntia', 'Khand',
           'Schoolbell']

HITDICE_TYPE = (
    ("4", "d4"),
    ("6", "d6"),
    ("8", "d8"),
    ("10", "d10"),
    ("12", "d12")
)

BABRates = (
    ('FBAB', 'Fast'),
    ('MBAB', 'Medium'),
    ('SBAB', 'Slow'),
)

SaveRates = (
    ('GSAVE', 'Good'),
    ('BSAVE', 'Bad'),
)


def die(maxi):
    import os
    randbyte = int.from_bytes(os.urandom(1), byteorder='big', signed=False)
    x = int(randbyte / 256 * (maxi)) + 1
    return x


def dice(n, maxi):
    t = 0
    for i in range(n):
        t += die(maxi)
    return t


def standard_method():
    return roll4d6_discardmin();


def classic_method():
    return roll3d6();


def roll4d6_discardmin():
    min = 7
    total = 0
    for d in range(4):
        x = die(6)
        if x < min:
            min = x
        total += x
    total -= min
    return total


def roll3d6():
    total = 0
    for d in range(3):
        x = die(6)
        total += x
    return total


ABILITIES_CHOICES = (
    ('STR', 'Strength'),
    ('DEX', 'Dexterity'),
    ('CON', 'Constitution'),
    ('INT', 'Intelligence'),
    ('WIS', 'Wisdom'),
    ('CHA', 'Charisma'),
    ('---', 'None'),
)

ABILITIES = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']


def choose_ability():
    from random import choice
    a = choice(ABILITIES)
    return a


def json_default(value):
    import datetime, uuid
    if isinstance(value, datetime.datetime):
        return dict(year=value.year, month=value.month, day=value.day, hour=value.hour, minute=value.minute)
    elif isinstance(value, datetime.date):
        return dict(year=value.year, month=value.month, day=value.day)
    elif isinstance(value, uuid.UUID):
        return dict(hex=value.hex)
    else:
        return value.__dict__


def as_modifier(i):
    s = f'+{i}'
    if int(i) < 0:
        s = f'{i}'
    return s


def get_modifier(ability):
    import math
    return math.floor((ability - 10) / 2)


def as_squares(speed):
    s = math.floor(speed / 5)
    return s


RANDOM_STARTING_AGE_PER_RACE = (
    ('human', '15'),
    ('dwarf', '40'),
    ('elf', '220'),
    ('gnome', '40'),
    ('half-elf', '20'),
    ('half-orc', '14'),
    ('halfling', '20'),
)

AC_SIZE_MODIFIER = {
    'fine': 8,
    'diminutive': 4,
    'tiny': 2,
    'small': 1,
    'medium': 0,
    'large': -1,
    'huge': -2,
    'gargantuan': -4,
    'colossal': -8,
}

TABLE_3_1 = [
    {'level': 1, 'slow': 0, 'medium': 0, 'fast': 0, 'feats': 1, 'ability_score': 0},
    {'level': 2, 'slow': 3000, 'medium': 2000, 'fast': 1300, 'feats': 1, 'ability_score': 0},
    {'level': 3, 'slow': 7500, 'medium': 5000, 'fast': 3300, 'feats': 2, 'ability_score': 0},
    {'level': 4, 'slow': 14000, 'medium': 9000, 'fast': 6000, 'feats': 2, 'ability_score': 1},
    {'level': 5, 'slow': 23000, 'medium': 15000, 'fast': 10000, 'feats': 3, 'ability_score': 1},
    {'level': 6, 'slow': 35000, 'medium': 23000, 'fast': 15000, 'feats': 3, 'ability_score': 1},
    {'level': 7, 'slow': 53000, 'medium': 35000, 'fast': 23000, 'feats': 4, 'ability_score': 1},
    {'level': 8, 'slow': 77000, 'medium': 51000, 'fast': 34000, 'feats': 4, 'ability_score': 2},
    {'level': 9, 'slow': 115000, 'medium': 75000, 'fast': 50000, 'feats': 5, 'ability_score': 2},
    {'level': 10, 'slow': 160000, 'medium': 105000, 'fast': 71000, 'feats': 5, 'ability_score': 2},
    {'level': 11, 'slow': 235000, 'medium': 155000, 'fast': 105000, 'feats': 6, 'ability_score': 2},
    {'level': 12, 'slow': 333000, 'medium': 220000, 'fast': 145000, 'feats': 6, 'ability_score': 3},
    {'level': 13, 'slow': 475000, 'medium': 315000, 'fast': 210000, 'feats': 7, 'ability_score': 3},
    {'level': 14, 'slow': 665000, 'medium': 445000, 'fast': 295000, 'feats': 7, 'ability_score': 3},
    {'level': 15, 'slow': 955000, 'medium': 635000, 'fast': 425000, 'feats': 8, 'ability_score': 3},
    {'level': 16, 'slow': 1350000, 'medium': 890000, 'fast': 600000, 'feats': 8, 'ability_score': 4},
    {'level': 17, 'slow': 1900000, 'medium': 1300000, 'fast': 850000, 'feats': 9, 'ability_score': 4},
    {'level': 18, 'slow': 2700000, 'medium': 1800000, 'fast': 1200000, 'feats': 9, 'ability_score': 4},
    {'level': 19, 'slow': 3850000, 'medium': 2550000, 'fast': 1700000, 'feats': 10, 'ability_score': 4},
    {'level': 20, 'slow': 5350000, 'medium': 3600000, 'fast': 2400000, 'feats': 10, 'ability_score': 5}
]
