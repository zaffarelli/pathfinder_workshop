import math


def aging_class_group_tbl7_1(class_name):
    if class_name in ['barbarian', 'rogue', 'sorcerer']:
        g = 0
    elif class_name in ['bard', 'fighter', 'paladin', 'ranger']:
        g = 1
    elif class_name in ['cleric', 'druid', 'monk', 'wizard']:
        g = 2
    return g


def table7_1(race_name, class_name):
    """
    Random starting ages
    Result:
    <adulthood> + <dice_num>d<dice_type>
    """
    adulthood = 0
    dice_num = 0
    dice_type = 0
    g = aging_class_group_tbl7_1(class_name)
    if race_name == 'human':
        adulthood = 15
        dice_num = [1, 1, 2][g]
        dice_type = [4, 6, 6][g]
    elif race_name == 'dwarf':
        adulthood = 40
        dice_num = [3, 5, 7][g]
        dice_type = [6, 6, 6][g]
    elif race_name == 'elf':
        adulthood = 110
        dice_num = [4, 6, 10][g]
        dice_type = [6, 6, 6][g]
    elif race_name == 'gnome':
        adulthood = 40
        dice_num = [4, 6, 9][g]
        dice_type = [6, 6, 6][g]
    elif race_name == 'half-elf':
        adulthood = 20
        dice_num = [1, 2, 3][g]
        dice_type = [6, 6, 6][g]
    elif race_name == 'half-orc':
        adulthood = 14
        dice_num = [1, 1, 2][g]
        dice_type = [4, 6, 6][g]
    elif race_name == 'halfling':
        adulthood = 20
        dice_num = [2, 3, 4][g]
        dice_type = [4, 6, 6][g]
    return adulthood, dice_num, dice_type


def gender_index(gender_name):
    g = 0
    if gender_name in ['f', 'female', 'Female', 'F']:
        g = 1
    return g


def table7_3(gender_name, race_name, rolled_value=0):
    from collector.utils.pathfinder_tools import dice
    base_height = 0
    base_weight = 0
    modifier_num = 0
    modifier_type = 0
    weight_modifier = 0
    ft = 12
    g = gender_index(gender_name)
    if race_name == 'human':
        base_height = [4 * ft + 10, 4 * ft + 5][g]
        base_weight = [120, 85][g]
        modifier_num = 2
        modifier_type = 10
        weight_modifier = 5
    elif race_name == 'dwarf':
        base_height = [3 * ft + 9, 3 * ft + 7][g]
        base_weight = [150, 120][g]
        modifier_num = 2
        modifier_type = 4
        weight_modifier = 7
    elif race_name == 'elf':
        base_height = [5 * ft + 4, 5 * ft + 4][g]
        base_weight = [100, 90][g]
        modifier_num = 2
        modifier_type = [8, 6][g]
        weight_modifier = 3
    elif race_name == 'gnome':
        base_height = [3 * ft + 0, 2 * ft + 10][g]
        base_weight = [35, 30][g]
        modifier_num = 2
        modifier_type = 4
        weight_modifier = 1
    elif race_name == 'half-elf':
        base_height = [5 * ft + 2, 5 * ft + 0][g]
        base_weight = [110, 90][g]
        modifier_num = 2
        modifier_type = 8
        weight_modifier = 5
    elif race_name == 'half-orc':
        base_height = [4 * ft + 10, 4 * ft + 5][g]
        base_weight = [150, 110][g]
        modifier_num = 2
        modifier_type = 12
        weight_modifier = 7
    elif race_name == 'halfling':
        base_height = [2 * ft + 8, 2 * ft + 6][g]
        base_weight = [30, 25][g]
        modifier_num = 2
        modifier_type = 4
        weight_modifier = 1
    if rolled_value == 0:
        rolled_value = dice(modifier_num, modifier_type)
    height = base_height + rolled_value
    weight = base_weight + rolled_value * weight_modifier
    return height, weight
