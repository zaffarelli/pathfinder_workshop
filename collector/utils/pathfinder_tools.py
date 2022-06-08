FONTSET = ['Cinzel', 'Trade+Winds', 'Imprima', 'Roboto', 'Philosopher', 'Ruda', 'Khand', 'Allura', 'Gochi+Hand',
           'Reggae+One', 'Syne+Mono', 'Zilla+Slab', 'Spartan', 'News+Cycle', 'Archivo', 'Francois+One', 'Caveat',
           'Gruppo', 'Voltaire', "Fredericka+the+Great", 'Esteban', 'Pompiere', 'Niconne', 'Delius',
           'Nanum+Pen+Script', 'Schoolbell', 'Jim+Nightshade', 'Julee', 'Estonia', 'East+Sea+Dokdo', 'Julee']

HITDICE_TYPE = (
    ("4", "d4"),
    ("6", "d6"),
    ("8", "d8"),
    ("10", "d10"),
    ("12", "d12")
)


def die(maxi):
    import os
    randbyte = int.from_bytes(os.urandom(1), byteorder='big', signed=False)
    x = int(randbyte / 256 * (maxi)) + 1
    return x


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


ABILITIES = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']


def choose_ability():
    from random import choice
    a = choice(ABILITIES)
    return a
