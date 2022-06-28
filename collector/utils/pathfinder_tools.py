FONTSET = ['Roboto', 'Ubuntu', 'Neuton']

HITDICE_TYPE = (
    ("4", "d4"),
    ("6", "d6"),
    ("8", "d8"),
    ("10", "d10"),
    ("12", "d12")
)

BABRates = (
    ('FBAB', 'Fast BAB'),
    ('MBAB', 'Medium BAB'),
    ('SBAB', 'Slow BAB'),
)

SaveRates = (
    ('GSAVE', 'Good Save'),
    ('BSAVE', 'Bad Save'),
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


RANDOM_STARTING_AGE_PER_RACE = (
    ('human', '15'),
    ('dwarf', '40'),
    ('elf', '220'),
    ('gnome', '40'),
    ('half-elf', '20'),
    ('half-orc', '14'),
    ('halfling', '20'),
)
