from collector.models.pathfinder_race import PathfinderRace
from collector.models.pathfinder_class import PathfinderClass
from collector.models.pathfinder_skill import PathfinderSkill

book_data = {
    'races': [
        {
            'name': 'Human',
            'size': 'Medium',
            'category': 'humanoid',
            'CHOICE_racial_mod': 2,
            'speed': 30,
            'languages': 'common',
        }, {
            'name': 'Elf',
            'size': 'Medium',
            'category': 'humanoid',
            'DEX_racial_mod': 2,
            'INT_racial_mod': 2,
            'CON_racial_mod': -2,
            'speed': 30,
            'languages': 'common;elven',
        }, {
            'name': 'Half Elf',
            'size': 'Medium',
            'category': 'humanoid',
            'CHOICE_racial_mod': 2,
            'speed': 30,
            'languages': 'common;elven',
        }, {
            'name': 'Half Orc',
            'size': 'Medium',
            'category': 'humanoid',
            'CHOICE_racial_mod': 2,
            'speed': 30,
            'languages': 'common;orc',
        }, {
            'name': 'Dwarf',
            'size': 'Medium',
            'category': 'humanoid',
            'CON_racial_mod': 2,
            'WIS_racial_mod': 2,
            'CHA_racial_mod': -2,
            'speed': 20,
            'languages': 'common;dwarven',
        }, {
            'name': 'Gnome',
            'size': 'Small',
            'category': 'humanoid',
            'CON_racial_mod': 2,
            'CHA_racial_mod': 2,
            'STR_racial_mod': -2,
            'speed': 20,
            'languages': 'common;gnome;sylvan',
        }, {
            'name': 'Halfling',
            'size': 'Small',
            'category': 'humanoid',
            'DEX_racial_mod': 2,
            'CHA_racial_mod': 2,
            'STR_racial_mod': -2,
            'speed': 20,
            'languages': 'common;halfling',
        }
    ],
    'classes': [
        {
            'name': 'Barbarian',
            'hit_die': 12,
            'skill_ranks_per_level': 4,
        }, {
            'name': 'Fighter',
            'hit_die': 10,
            'skill_ranks_per_level': 2,
        }, {
            'name': 'Paladin',
            'hit_die': 10,
            'skill_ranks_per_level': 2,
        }, {
            'name': 'Ranger',
            'hit_die': 10,
            'skill_ranks_per_level': 6,
        }, {
            'name': 'Cleric',
            'hit_die': 8,
            'skill_ranks_per_level': 2,
        }, {
            'name': 'Druid',
            'hit_die': 8,
            'skill_ranks_per_level': 4,
        }, {
            'name': 'Rogue',
            'hit_die': 8,
            'skill_ranks_per_level': 8,
        }, {
            'name': 'Bard',
            'hit_die': 8,
            'skill_ranks_per_level': 6,
        }, {
            'name': 'Wizard',
            'hit_die': 6,
            'skill_ranks_per_level': 2,
        }, {
            'name': 'Sorcerer',
            'hit_die': 6,
            'skill_ranks_per_level': 2,
        }, {
            'name': 'Monk',
            'hit_die': 8,
            'skill_ranks_per_level': 4,
        }

    ],
    'skills': [
        {
            'name': 'Acrobatics',
            'ability': 'DEX',
        }, {
            'name': 'Appraise',
            'ability': 'INT',
        }, {
            'name': 'Bluff',
            'ability': 'CHA',
        }, {
            'name': 'Climb',
            'ability': 'STR',
        }, {
            'name': 'Craft',
            'is_wildcard': True
        }, {
            'name': 'Diplomacy',
            'ability': 'CHA',
        }, {
            'name': 'Disable Device',
            'is_trained_only': True,
            'ability': 'DEX',
        }, {
            'name': 'Disguise',
            'ability': 'CHA',
        }, {
            'name': 'Escape Artist',
            'ability': 'DEX',
        }, {
            'name': 'Fly',
            'ability': 'DEX',
        }, {
            'name': 'Handle Animal',
            'is_trained_only': True,
            'ability': 'CHA',
        }, {
            'name': 'Heal',
            'ability': 'WIS',
        }, {
            'name': 'Intimidate',
            'ability': 'CHA',
        }, {
            'name': 'Knowledge (Arcana)',
            'is_trained_only': True,
        }, {
            'name': 'Knowledge (Dungeoneering)',
            'is_trained_only': True,
        }, {
            'name': 'Knowledge (Engineering)',
            'is_trained_only': True,
        }, {
            'name': 'Knowledge (Geography)',
            'is_trained_only': True,
        }, {
            'name': 'Knowledge (History)',
            'is_trained_only': True,
        }, {
            'name': 'Knowledge (Local)',
            'is_trained_only': True,
        }, {
            'name': 'Knowledge (Nature)',
            'is_trained_only': True,
        }, {
            'name': 'Knowledge (Nobility)',
            'is_trained_only': True,
        }, {
            'name': 'Knowledge (Planes)',
            'is_trained_only': True,
        }, {
            'name': 'Knowledge (Religion)',
            'is_trained_only': True,
        }, {
            'name': 'Linguistics',
            'is_trained_only': True,
        }, {
            'name': 'Perception',
            'ability': 'WIS',
        }, {
            'name': 'Perform',
            'is_wildcard': True,
            'ability': 'CHA',

        }, {
            'name': 'Profession',
            'is_trained_only': True,
            'is_wildcard': True,
            'ability': 'WIS',
        }, {
            'name': 'Ride',
            'ability': 'DEX',
        }, {
            'name': 'Sense motive',
            'ability': 'WIS',
        }, {
            'name': 'Sleight of Hand',
            'is_trained_only': True,
            'ability': 'DEX',
        }, {
            'name': 'Spellcraft',
            'is_trained_only': True,
        }, {
            'name': 'Stealth',
            'ability': 'DEX',
        }, {
            'name': 'Survival',
            'ability': 'WIS',
        }, {
            'name': 'Swim',
            'ability': 'STR',
        }, {
            'name': 'Use Magic Device',
            'is_trained_only': True,
            'ability': 'CHA',
        }

    ],
    'weapons': [
        {
            'name': 'longsword',

        },
    ],
    'armors': [
        {
            'name': 'padded',
            'gp_value': '5',

        },
    ],
    'gears': [

    ]
}

adventure_data = {
    'npcs': [
        {
            'name': 'Daenerym Nemraskalli',
            'rolls': {
                'STR': 14,
                'DEX': 10,
                'CON': 10,
                'INT': 10,
                'WIS': 10,
                'CHA': 10,
            },

        }

    ]

}

# Clean up
es = PathfinderRace.objects.all()
for e in es:
    e.delete()

es = PathfinderClass.objects.all()
for e in es:
    e.delete()

es = PathfinderSkill.objects.all()
for e in es:
    e.delete()

# populate
for e in book_data['races']:
    item = PathfinderRace()
    for k, v in e.items():
        print('k', k, 'v', v)
        setattr(item, k, v)
    item.save()

for e in book_data['classes']:
    item = PathfinderClass()
    for k, v in e.items():
        print('k', k, 'v', v)
        setattr(item, k, v)
    item.save()

for e in book_data['skills']:
    item = PathfinderSkill()
    for k, v in e.items():
        print('k', k, 'v', v)
        setattr(item, k, v)
    item.save()
