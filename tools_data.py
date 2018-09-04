race_list = {'Dwarf': {'str': [8, 18], 'dex': [3, 17], 'con': [11, 18],
                       'int': [3, 18], 'wis': [3, 18], 'cha': [3, 17]},
             'Elf': {'str': [3, 18], 'dex': [6, 18], 'con': [7, 18],
                     'int': [8, 18], 'wis': [3, 18], 'cha': [8, 18]},
             'Gnome': {'str': [6, 18], 'dex': [3, 18], 'con': [8, 18],
                       'int': [6, 18], 'wis': [3, 18], 'cha': [3, 18]},
             'Half-Elf': {'str': [3, 18], 'dex': [6, 18], 'con': [6, 18],
                          'int': [4, 18], 'wis': [3, 18], 'cha': [3, 18]},
             'Halfling': {'str': [7, 18], 'dex': [7, 18], 'con': [10, 18],
                          'int': [6, 18], 'wis': [3, 18], 'cha': [3, 18]},
             'Human': {'str': [3, 18], 'dex': [3, 18], 'con': [3, 18],
                       'int': [3, 18], 'wis': [3, 18], 'cha': [3, 18]}}

class_list = {'Fighter': {'str': 9, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0,
                           'permit': ['all']},
               'Paladin': {'str': 12, 'dex': 0, 'con': 9, 'int': 0, 'wis': 13, 'cha': 17,
                           'permit': ['human']},
               'Ranger': {'str': 13, 'dex': 13, 'con': 14, 'int': 0, 'wis': 14, 'cha': 0,
                          'permit': ['elf', 'half_Elf', 'human']},
               'Mage': {'str': 0, 'dex': 0, 'con': 0, 'int': 9, 'wis': 0, 'cha': 0,
                        'permit': ['elf', 'half_elf', 'human', 'gnome']},
               'Cleric': {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 9, 'cha': 0,
                          'permit': ['all']},
               'Druid': {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 12, 'cha': 15,
                         'permit': ['human', 'half_elf']},
               'Thief': {'str': 0, 'dex': 9, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0,
                         'permit': ['all']},
               'Bard': {'str': 0, 'dex': 12, 'con': 0, 'int': 13, 'wis': 0, 'cha': 15,
                        'permit': ['human', 'half_elf']}}

class_list2 = { 'Fighter': { 'stats' : { 'str': 9, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0 },
                             'permit': ['all'],
                             'desc': 'Fighter     - The skilled combatant and strategist.'},
                'Paladin': { 'stats' : { 'str': 12, 'dex': 0, 'con': 9, 'int': 0, 'wis': 13, 'cha': 17 },
                             'permit': ['human'],
                             'desc': 'Paladin    - A novice fighter bolstered by divine magic.'},
                'Ranger': { 'stats' : { 'str': 13, 'dex': 13, 'con': 14, 'int': 0, 'wis': 14, 'cha': 0},
                            'permit': ['elf', 'half-elf', 'human'] ,
                            'desc': 'Ranger     - One who blends wilderness knowledge and martial ability'},
                'Mage': { 'stats' : { 'str': 0, 'dex': 0, 'con': 0, 'int': 9, 'wis': 0, 'cha': 0 },
                          'permit': ['elf', 'half_elf', 'human', 'gnome'],
                          'desc' : 'Mage        - A magic user with natural abilities'},
                'Cleric': { 'stats' : {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 9, 'cha': 0 },
                            'permit': ['all'],
                            'desc': 'Cleric      - A holy man capable of healing wounds.'},
                'Druid': { 'stats' : {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 12, 'cha': 15 },
                           'permit': ['human', 'half_elf'] ,
                           'desc': 'Druid       - A nomad devoted to the powers of Nature'},
                'Thief': { 'stats' : {'str': 0, 'dex': 9, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0 },
                           'permit': ['all'],
                           'desc': 'Thief       - A sub class of the Rogue Character'},
                'Bard': { 'stats' : {'str': 0, 'dex': 12, 'con': 0, 'int': 13, 'wis': 0, 'cha': 15 },
                          'permit': ['human', 'half_elf'],
                          'desc': 'Bard         - A story witty storyteller or musician.'}
       }

social_class_list = ['Upper', 'Middle', 'Lower']


race_desc = {'Dwarf': "     - Bold, hardy, warrior, miner, long memory and grudges",
             'Elf': "       - Magical people of otherworldly grace, in but not of the world",
             'Halfling':  "  - You love peace, food, hearth, and home",
             "Human": "     - Young, short-lived race, innovators and achievers",
             "Gnome": "     - You delight in life, are an inventor, and explorer",
             "Half-Elf":  "  - Curious, inventive, ambitious, love nature, artistic"
             }



Cleric_desc = 'Cleric    - A holy man capable of healing wounds.'
Barbarian_desc = 'Barbarian - The relentless combatant fueled by fury.'
Bard_desc = 'Bard      - A story witty storyteller or musician.'
Druid_desc = 'Druid     - A nomad devoted to the powers of Nature'
Fighter_desc = 'Fighter   - The skilled combatant and strategist.'
Paladin_desc = 'Paladin   - A novice fighter bolstered by divine magic.'
Ranger_desc = 'Ranger    - One who blends wilderness knowledge and martial ability'
Rogue_desc = 'Rogue     - The thief, assassin, and stealthy character.'
Thief_desc = 'Thief     - A sub class of the Rogue Character'
Wizard_desc = 'Wizard    - Keeper of arcane secrets and manipulator of magic.'

race_short = [
    "Dwarf", "Elf", "Halfling", "Human", "Gnome", "Half-Elf"
]

class_desc = {"Barbarian": " - The relentless combatant fueled by fury.",
              "Bard": "     - A story witty storyteller or musician.",
              "Cleric": "    - A holy man capable of healing wounds.",
              "Druid": "     - A nomad devoted to the powers of Nature",
              "Fighter": "   - The skilled combatant and strategist.",
              "Paladin": "   - A novice fighter bolstered by divine magic.",
              "Ranger": "    - One who blends wilderness knowledge and martial ability",
              "Rogue": "     - The thief, assassin, and stealthy character.",
              "Wizard ": "   - Keeper of arcane secrets and manipulator of magic."
              }


strength_stats = {'str1': {'Str': 1, 'Hit Prob': '-5', 'Dam Adj': '-4', 'Wt Allow': 1, 'Max Press': 3, 'Open Doors': 1, 'BB LG': '0%'},
                  'str2': {"Str": 2, "Hit Prob": '-3', "Dam Adj": '-2', "Wt Allow": 1, "Max Press": 5, "Open Doors": 1, "BB LG": '0%'},
                  'str3': {"Str": 3, "Hit Prob": '-3', "Dam Adj": '-1', "Wt Allow": 5, "Max Press": 10, "Open Doors": 2, "BB LG": '0%'},
                  'str4' : {"Str": 4, "Hit Prob": '-2', "Dam Adj": '-1', "Wt Allow": 10, "Max Press": 25, "Open Doors": 2, "BB LG": '0%'},
                  'str5': {"Str": 5, "Hit Prob": '-2', "Dam Adj": '-1', "Wt Allow": 10, "Max Press": 25, "Open Doors": 2, "BB LG": '0%'},
                  'str6': {"Str": 6, "Hit Prob": '-1', "Dam Adj": 'None', "Wt Allow": 20, "Max Press": 55, "Open Doors": 4, "BB LG": '0%'},
                  'str7': {"Str": 7, "Hit Prob": '-1', "Dam Adj": 'None', "Wt Allow": 20, "Max Press": 55, "Open Doors": 4, "BB LG": '0%'},
                  'str8': {"Str": 8, "Hit Prob": 'Normal', "Dam Adj": 'None', "Wt Allow": 35, "Max Press": 90, "Open Doors": 5, "BB LG": '1%'},
                  'str9': {"Str": 9, "Hit Prob": 'Normal', "Dam Adj": 'None', "Wt Allow": 35, "Max Press": 90, "Open Doors": 5, "BB LG": '1%'},
                  'str10': {"Str": 10, "Hit Prob": 'Normal', "Dam Adj": 'None', "Wt Allow": 40, "Max Press": 115, "Open Doors": 6, "BB LG": '2%'},
                  'str11': {"Str": 11, "Hit Prob": 'Normal', "Dam Adj": 'None', "Wt Allow": 40, "Max Press": 115, "Open Doors": 6, "BB LG": '2%'},
                  'str12': {"Str": 12, "Hit Prob": 'Normal', "Dam Adj": 'None', "Wt Allow": 45, "Max Press": 140, "Open Doors": 7, "BB LG": '4%'},
                  'str13': {"Str": 13, "Hit Prob": 'Normal', "Dam Adj": 'None', "Wt Allow": 45, "Max Press": 140, "Open Doors": 7, "BB LG": '4%'},
                  'str14': {"Str": 14, "Hit Prob": 'Normal', "Dam Adj": 'None', "Wt Allow": 55, "Max Press": 170, "Open Doors": 8, "BB LG": '7%'},
                  'str15': {"Str": 15, "Hit Prob": 'Normal', "Dam Adj": 'None', "Wt Allow": 55, "Max Press": 170, "Open Doors": 8, "BB LG": '7%'},
                  'str16': {"Str": 16, "Hit Prob": 'Normal', "Dam Adj": '+1', "Wt Allow": 70, "Max Press": 195, "Open Doors": 9, "BB LG": '10%'},
                  'str17': {"Str": 17, "Hit Prob": '+1', "Dam Adj": '+2', "Wt Allow": 85, "Max Press": 220, "Open Doors": 10, "BB LG": '13%'},
                  'str18': {"Str": 18, "Hit Prob": '+1', "Dam Adj": '+2', "Wt Allow": 110, "Max Press": 225, "Open Doors": 11, "BB LG": '16%'}
                  }


dexterity_stats = {'dex1': {'Dex': 1, 'Reaction Adj': '-6', 'Missle Attack Adj': '-6', 'Defense Adj': '+5'},
                   'dex2': {'Dex': 2, 'Reaction Adj': '-4', 'Missle Attack Adj': '-4', 'Defense Adj': '+5'},
                   'dex3': {'Dex': 3, 'Reaction Adj': '-3', 'Missle Attack Adj': '-3', 'Defense Adj': '+4'},
                   'dex4': {'Dex': 4, 'Reaction Adj': '-2', 'Missle Attack Adj': '-2', 'Defense Adj': '+3'},
                   'dex5': {'Dex': 5, 'Reaction Adj': '-1', 'Missle Attack Adj': '-1', 'Defense Adj': '+2'},
                   'dex6': {'Dex': 6, 'Reaction Adj': 0, 'Missle Attack Adj': 0, 'Defense Adj': '+1'},
                   'dex7': {'Dex': 7, 'Reaction Adj': 0, 'Missle Attack Adj': 0, 'Defense Adj': 0},
                   'dex8': {'Dex': 8, 'Reaction Adj': 0, 'Missle Attack Adj': 0, 'Defense Adj': 0},
                   'dex9': {'Dex': 9, 'Reaction Adj': 0, 'Missle Attack Adj': 0, 'Defense Adj': 0},
                   'dex10': {'Dex': 10, 'Reaction Adj': 0, 'Missle Attack Adj': 0, 'Defense Adj': 0},
                   'dex11': {'Dex': 11, 'Reaction Adj': 0, 'Missle Attack Adj': 0, 'Defense Adj': 0},
                   'dex12': {'Dex': 12, 'Reaction Adj': 0, 'Missle Attack Adj': 0, 'Defense Adj': 0},
                   'dex13': {'Dex': 13, 'Reaction Adj': 0, 'Missle Attack Adj': 0, 'Defense Adj': 0},
                   'dex14': {'Dex': 14, 'Reaction Adj': 0, 'Missle Attack Adj': 0, 'Defense Adj': 0},
                   'dex15': {'Dex': 15, 'Reaction Adj': 0, 'Missle Attack Adj': 0, 'Defense Adj': '-1'},
                   'dex16': {'Dex': 16, 'Reaction Adj': '+1', 'Missle Attack Adj': '+1', 'Defense Adj': '-2'},
                   'dex17': {'Dex': 17, 'Reaction Adj': '+2', 'Missle Attack Adj': '+2', 'Defense Adj': '-3'},
                   'dex18': {'Dex': 18, 'Reaction Adj': '+2', 'Missle Attack Adj': '+2', 'Defense Adj': '-4'},
                   'dex19': {'Dex': 19, 'Reaction Adj': '+3', 'Missle Attack Adj': '+3', 'Defense Adj': '-4'}
                  }



constitution_stats = {'con1': {'Con': 1, 'HP Adj': - 3, 'System Shock': '25%', 'Resurrection Survival': '30%', 'Poison Save': '-2', 'Regeneration': 'Nil'},
                      'con2': {'Con': 2, 'HP Adj': - 2, 'System Shock': '30%', 'Resurrection Survival': '35%', 'Poison Save': '-1', 'Regeneration': 'Nil'},
                      'con3': {'Con': 3, 'HP Adj': - 2, 'System Shock': '35%', 'Resurrection Survival': '40%', 'Poison Save': 0, 'Regeneration': 'Nil' },
                      'con4': {'Con': 4, 'HP Adj': - 1, 'System Shock': '40%', 'Resurrection Survival': '45%', 'Poison Save': 0, 'Regeneration': 'Nil' },
                      'con5': {'Con': 5, 'HP Adj': - 1, 'System Shock': '45%', 'Resurrection Survival': '50%', 'Poison Save': 0, 'Regeneration': 'Nil' },
                      'con6': {'Con': 6, 'HP Adj': - 1, 'System Shock': '50%', 'Resurrection Survival': '55%', 'Poison Save': 0, 'Regeneration': 'Nil' },
                      'con7': {'Con': 7, 'HP Adj': 0, 'System Shock': '55%', 'Resurrection Survival': '60%', 'Poison Save': 0, 'Regeneration': 'Nil' },
                      'con8': {'Con': 8, 'HP Adj': 0, 'System Shock': '60%', 'Resurrection Survival': '65%', 'Poison Save': 0, 'Regeneration': 'Nil' },
                      'con9': {'Con': 9, 'HP Adj': 0, 'System Shock': '65%', 'Resurrection Survival': '70%', 'Poison Save': 0, 'Regeneration': 'Nil' },
                      'con10': {'Con': 10, 'HP Adj': 0, 'System Shock': '70%', 'Resurrection Survival': '75%', 'Poison Save': 0, 'Regeneration': 'Nil' },
                      'con11': {'Con': 11, 'HP Adj': 0, 'System Shock': '75%', 'Resurrection Survival': '80%', 'Poison Save': 0, 'Regeneration': 'Nil' },
                      'con12': {'Con': 12, 'HP Adj': 0, 'System Shock': '80%', 'Resurrection Survival': '85%', 'Poison Save': 0, 'Regeneration': 'Nil' },
                      'con13': {'Con': 13, 'HP Adj': 0, 'System Shock': '85%', 'Resurrection Survival': '90%', 'Poison Save': 0, 'Regeneration': 'Nil' },
                      'con14': {'Con': 14, 'HP Adj': 0, 'System Shock': '88%', 'Resurrection Survival': '92%', 'Poison Save': 0, 'Regeneration': 'Nil' },
                      'con15': {'Con': 15, 'HP Adj': 0, 'System Shock': '90%', 'Resurrection Survival': '94%', 'Poison Save': 0, 'Regeneration': 'Nil' },
                      'con16': {'Con': 16, 'HP Adj': + 1, 'System Shock': '95%', 'Resurrection Survival': '96%', 'Poison Save': 0, 'Regeneration': 'Nil' },
                      'con17': {'Con': 17, 'HP Adj': + 2, 'System Shock': '97%', 'Resurrection Survival': '98%', 'Poison Save': 0, 'Regeneration': 'Nil' },
                      'con18': {'Con': 18, 'HP Adj': + 2, 'System Shock': '99%', 'Resurrection Survival': '100%', 'Poison Save': 0, 'Regeneration': 'Nil' },
                      'con19': {'Con': 19, 'HP Adj': + 2, 'System Shock': '99%', 'Resurrection Survival': '100%', 'Poison Save': '+1', 'Regeneration': 'Nil' }
                      }


intelligence_stats = {'int1': {'Int': 1, 'Languages': 0, 'Spell Level': '--', 'Learn Spells': '--',
                               'Max Spells/Level': '--', 'Illusion Immunity': '--'},
                      'int2': {'Int': 2, 'Languages': 1, 'Spell Level': '--', 'Learn Spells': '--',
                               'Max Spells/Level': '--', 'Illusion Immunity': '--'},
                      'int3': {'Int': 3, 'Languages': 1, 'Spell Level': '--', 'Learn Spells': '--',
                               'Max Spells/Level': '--', 'Illusion Immunity': '--'},
                      'int4': {'Int': 4, 'Languages': 1, 'Spell Level': '--', 'Learn Spells': '--',
                               'Max Spells/Level': '--', 'Illusion Immunity': '--'},
                      'int5': {'Int': 5, 'Languages': 1, 'Spell Level': '--', 'Learn Spells': '--',
                               'Max Spells/Level': '--', 'Illusion Immunity': '--'},
                      'int6': {'Int': 6, 'Languages': 1, 'Spell Level': '--', 'Learn Spells': '--',
                               'Max Spells/Level': '--', 'Illusion Immunity': '--'},
                      'int7': {'Int': 7, 'Languages': 1, 'Spell Level': '--', 'Learn Spells': '--',
                               'Max Spells/Level': '--', 'Illusion Immunity': '--'},
                      'int8': {'Int': 8, 'Languages': 1, 'Spell Level': '--', 'Learn Spells': '--',
                               'Max Spells/Level': '--', 'Illusion Immunity': '--'},
                      'int9': {'Int': 9, 'Languages': 2, 'Spell Level': '4th', 'Learn Spells': '35%',
                               'Max Spells/Level': 6, 'Illusion Immunity': '--'},
                      'int10': {'Int': 10, 'Languages': 2, 'Spell Level': '5th', 'Learn Spells': '40%',
                                'Max Spells/Level': 7, 'Illusion Immunity': '--'},
                      'int11': {'Int': 11, 'Languages': 2, 'Spell Level': '5th', 'Learn Spells': '45%',
                                'Max Spells/Level': 7, 'Illusion Immunity': '--'},
                      'int12': {'Int': 12, 'Languages': 3, 'Spell Level': '6th', 'Learn Spells': '50%',
                                'Max Spells/Level': 7, 'Illusion Immunity': '--'},
                      'int13': {'Int': 13, 'Languages': 3, 'Spell Level': '6th', 'Learn Spells': '55%',
                                'Max Spells/Level': 9, 'Illusion Immunity': '--'},
                      'int14': {'Int': 14, 'Languages': 4, 'Spell Level': '7th', 'Learn Spells': '60%',
                                'Max Spells/Level': 9, 'Illusion Immunity': '--'},
                      'int15': {'Int': 15, 'Languages': 4, 'Spell Level': '7th', 'Learn Spells': '65%',
                                'Max Spells/Level': 11, 'Illusion Immunity': '--'},
                      'int16': {'Int': 16, 'Languages': 5, 'Spell Level': '8th', 'Learn Spells': '70%',
                                'Max Spells/Level': 11, 'Illusion Immunity': '--'},
                      'int17': {'Int': 17, 'Languages': 6, 'Spell Level': '8th', 'Learn Spells': '75%',
                                'Max Spells/Level': 14, 'Illusion Immunity': '--'},
                      'int18': {'Int': 18, 'Languages': 7, 'Spell Level': '9th', 'Learn Spells': '85%',
                                'Max Spells/Level': 18, 'Illusion Immunity': '--'},
                      'int19': {'Int': 19, 'Languages': 8, 'Spell Level': '9th', 'Learn Spells': '95%',
                                'Max Spells/Level': 'All', 'Illusion Immunity': '1st Level'}
                      }

wisdom_stats = {'wis1': {'Wis': 1, 'Magical Defense Adj': '-6', 'Bonus Spells': '--', 'Spell Failure': '80%', 'Spell Immunity': '--'},
                'wis2': {'Wis': 2, 'Magical Defense Adj': '-4', 'Bonus Spells': '--', 'Spell Failure': '60%', 'Spell Immunity': '--'},
                'wis3': {'Wis': 3, 'Magical Defense Adj': '-3', 'Bonus Spells': '--', 'Spell Failure': '50%', 'Spell Immunity': '--'},
                'wis4': {'Wis': 4, 'Magical Defense Adj': '-2', 'Bonus Spells': '--', 'Spell Failure': '45%', 'Spell Immunity': '--'},
                'wis5': {'Wis': 5, 'Magical Defense Adj': '-1', 'Bonus Spells': '--', 'Spell Failure': '40%', 'Spell Immunity': '--'},
                'wis6': {'Wis': 6, 'Magical Defense Adj': '-1', 'Bonus Spells': '--', 'Spell Failure': '35%', 'Spell Immunity': '--'},
                'wis7': {'Wis': 7, 'Magical Defense Adj': '-1', 'Bonus Spells': '--', 'Spell Failure': '30%', 'Spell Immunity': '--'},
                'wis9': {'Wis': 9, 'Magical Defense Adj': 0, 'Bonus Spells': 0, 'Spell Failure': '20%', 'Spell Immunity': '--'},
                'wis10': {'Wis': 10, 'Magical Defense Adj': 0, 'Bonus Spells': 0, 'Spell Failure': '15%', 'Spell Immunity': '--'},
                'wis11': {'Wis': 11, 'Magical Defense Adj': 0, 'Bonus Spells': 0, 'Spell Failure': '10%', 'Spell Immunity': '--'},
                'wis12': {'Wis': 12, 'Magical Defense Adj': 0, 'Bonus Spells': 0, 'Spell Failure': '5%', 'Spell Immunity': '--'},
                'wis13': {'Wis': 13, 'Magical Defense Adj': 0, 'Bonus Spells': '1st', 'Spell Failure': '0%', 'Spell Immunity': '--'},
                'wis14': {'Wis': 14, 'Magical Defense Adj': 0, 'Bonus Spells': '1st', 'Spell Failure': '0%', 'Spell Immunity': '--'},
                'wis15': {'Wis': 15, 'Magical Defense Adj': '+1', 'Bonus Spells': '2nd', 'Spell Failure': '0%', 'Spell Immunity': '--'},
                'wis16': {'Wis': 16, 'Magical Defense Adj': '+2', 'Bonus Spells': '2nd', 'Spell Failure': '0%', 'Spell Immunity': '--'},
                'wis17': {'Wis': 17, 'Magical Defense Adj': '+3', 'Bonus Spells': '3rd', 'Spell Failure': '0%', 'Spell Immunity': '--'},
                'wis18': {'Wis': 18, 'Magical Defense Adj': '+4', 'Bonus Spells': '4th', 'Spell Failure': '0%', 'Spell Immunity': '--'}
}

charisma_stats = {'cha1': {'Cha': 1, 'Max Henchmen': 0, 'Loyalty Base': '-8', 'Reaction Adj': '-7'},
                  'cha2': {'Cha': 2, 'Max Henchmen': 1, 'Loyalty Base': '-7', 'Reaction Adj': '-6'},
                  'cha3': {'Cha': 3, 'Max Henchmen': 1, 'Loyalty Base': '-6', 'Reaction Adj': '-5'},
                  'cha4': {'Cha': 4, 'Max Henchmen': 1, 'Loyalty Base': '-5', 'Reaction Adj': '-4'},
                  'cha5': {'Cha': 5, 'Max Henchmen': 2, 'Loyalty Base': '-4', 'Reaction Adj': '-3'},
                  'cha6': {'Cha': 6, 'Max Henchmen': 2, 'Loyalty Base': '-3', 'Reaction Adj': '-2'},
                  'cha7': {'Cha': 7, 'Max Henchmen': 3, 'Loyalty Base': '-2', 'Reaction Adj': '-1'},
                  'cha8': {'Cha': 8, 'Max Henchmen': 3, 'Loyalty Base': '-1', 'Reaction Adj': 0},
                  'cha9': {'Cha': 9, 'Max Henchmen': 4, 'Loyalty Base': 0, 'Reaction Adj': 0},
                  'cha10': {'Cha': 10, 'Max Henchmen': 4, 'Loyalty Base': 0, 'Reaction Adj': 0},
                  'cha11': {'Cha': 11, 'Max Henchmen': 4, 'Loyalty Base': 0, 'Reaction Adj': 0},
                  'cha12': {'Cha': 12, 'Max Henchmen': 5, 'Loyalty Base': 0, 'Reaction Adj': 0},
                  'cha13': {'Cha': 13, 'Max Henchmen': 5, 'Loyalty Base': 0, 'Reaction Adj': '+1'},
                  'cha14': {'Cha': 14, 'Max Henchmen': 6, 'Loyalty Base': '+1', 'Reaction Adj': '+2'},
                  'cha15': {'Cha': 15, 'Max Henchmen': 7, 'Loyalty Base': '+3', 'Reaction Adj': '+3'},
                  'cha16': {'Cha': 16, 'Max Henchmen': 8, 'Loyalty Base': '+4', 'Reaction Adj': '+5'},
                  'cha17': {'Cha': 17, 'Max Henchmen': 10, 'Loyalty Base': '+6' , 'Reaction Adj': '+6'},
                  'cha18': {'Cha': 18, 'Max Henchmen': 15, 'Loyalty Base': '+8' , 'Reaction Adj': '+7'}
                 }



savings_stats = {'priest1': {'L1': 1, 'ppdm': 10, 'rsw': 14, 'ppoly': 13, 'bw': 16, 'spell': 15},
                 'priest2': {'L2': 2, 'ppdm': 10, 'rsw': 14, 'ppoly': 13, 'bw': 16, 'spell': 15},
                 'priest3': {'L3': 3, 'ppdm': 10, 'rsw': 14, 'ppoly': 13, 'bw': 16, 'spell': 15},
                 'priest4': {'L4': 4, 'ppdm': 9, 'rsw': 13, 'ppoly': 12, 'bw': 15, 'spell': 14},
                 'priest5': {'L5': 5, 'ppdm': 9, 'rsw': 13, 'ppoly': 12, 'bw': 15, 'spell': 14},
                 'priest6': {'L6': 6, 'ppdm': 9, 'rsw': 13, 'ppoly': 12, 'bw': 15, 'spell': 14},
                 'priest7': {'L7': 7, 'ppdm': 11, 'rsw': 10, 'ppoly': 9, 'bw': 13, 'spell': 12},
                 'priest8': {'L8': 8, 'ppdm': 11, 'rsw': 10, 'ppoly': 9, 'bw': 13, 'spell': 12},
                 'priest9': {'L9': 9, 'ppdm': 11, 'rsw': 10, 'ppoly': 9, 'bw': 13, 'spell': 12},
                 'priest10': {'L10': 10, 'ppdm': 6, 'rsw': 10, 'ppoly': 9, 'bw': 12, 'spell': 11},
                 'priest11': {'L11': 11, 'ppdm': 6, 'rsw': 10, 'ppoly': 9, 'bw': 12, 'spell': 11},
                 'priest12': {'L12': 12, 'ppdm': 6, 'rsw': 10, 'ppoly': 9, 'bw': 12, 'spell': 11},
                 'priest13': {'L13': 13, 'ppdm': 9, 'rsw': 9, 'ppoly': 8, 'bw': 11, 'spell': 10},
                 'priest14': {'L14': 14, 'ppdm': 9, 'rsw': 9, 'ppoly': 8, 'bw': 11, 'spell': 10},
                 'priest15': {'L15': 15, 'ppdm': 9, 'rsw': 9, 'ppoly': 8, 'bw': 11, 'spell': 10},
                 'priest16': {'L16': 16, 'ppdm': 4, 'rsw': 8, 'ppoly': 7, 'bw': 10, 'spell': 9},
                 'priest17': {'L16': 17, 'ppdm': 4, 'rsw': 8, 'ppoly': 7, 'bw': 10, 'spell': 9},
                 'priest19': {'L16': 19, 'ppdm': 2, 'rsw': 6, 'ppoly': 5, 'bw': 8, 'spell': 7},

                 'rogue1': {'L1': 1, 'ppdm': 13, 'rsw': 14, 'ppoly': 12, 'bw': 16, 'spell': 15},
                 'rogue3': {'L3': 3, 'ppdm': 13, 'rsw': 14, 'ppoly': 12, 'bw': 16, 'spell': 15},
                 'rogue4': {'L4': 4, 'ppdm': 13, 'rsw': 14, 'ppoly': 12, 'bw': 16, 'spell': 15},
                 'rogue6': {'L6': 6, 'ppdm': 12, 'rsw': 13, 'ppoly': 11, 'bw': 15, 'spell': 13},
                 'rogue7': {'L7': 7, 'ppdm': 12, 'rsw': 13, 'ppoly': 11, 'bw': 15, 'spell': 13},
                 'rogue8': {'L8': 8, 'ppdm': 12, 'rsw': 13, 'ppoly': 11, 'bw': 15, 'spell': 13},
                 'rogue9': {'L9': 9, 'ppdm': 11, 'rsw': 10, 'ppoly': 10, 'bw': 14, 'spell': 11},
                 'rogue10': {'L10': 10, 'ppdm': 11, 'rsw': 10, 'ppoly': 10, 'bw': 14, 'spell': 11},
                 'rogue11': {'L11': 11, 'ppdm': 11, 'rsw': 10, 'ppoly': 10, 'bw': 14, 'spell': 11},
                 'rogue12': {'L12': 12, 'ppdm': 11, 'rsw': 10, 'ppoly': 10, 'bw': 14, 'spell': 11},
                 'rogue13': {'L13': 13, 'ppdm': 10, 'rsw': 8, 'ppoly': 9, 'bw': 13, 'spell': 9},
                 'rogue14': {'L14': 14, 'ppdm': 10, 'rsw': 8, 'ppoly': 9, 'bw': 13, 'spell': 9},
                 'rogue15': {'L15': 15, 'ppdm': 10, 'rsw': 8, 'ppoly': 9, 'bw': 13, 'spell': 9},
                 'rogue16': {'L16': 16, 'ppdm': 10, 'rsw': 8, 'ppoly': 9, 'bw': 13, 'spell': 9},
                 'rogue17': {'L17': 17, 'ppdm': 9, 'rsw': 6, 'ppoly': 8, 'bw': 12, 'spell': 7},
                 'rogue18': {'L18': 18, 'ppdm': 9, 'rsw': 6, 'ppoly': 8, 'bw': 12, 'spell': 7},
                 'rogue19': {'L19': 19, 'ppdm': 9, 'rsw': 6, 'ppoly': 8, 'bw': 12, 'spell': 7},
                 'rogue20': {'L20': 20, 'ppdm': 9, 'rsw': 6, 'ppoly': 8, 'bw': 12, 'spell': 7},
                 'rogue21': {'L21': 21, 'ppdm': 8, 'rsw': 4, 'ppoly': 7, 'bw': 11, 'spell': 5},

                 'warrior0': {'L0': 0, 'ppdm': 16, 'rsw': 18, 'ppoly': 17, 'bw': 20, 'spell': 19},
                 'warrior1': {'L1': 1, 'ppdm': 14, 'rsw': 16, 'ppoly': 15, 'bw': 17, 'spell': 17},
                 'warrior2': {'L2': 2, 'ppdm': 14, 'rsw': 16, 'ppoly': 15, 'bw': 17, 'spell': 17},
                 'warrior3': {'L3': 3, 'ppdm': 13, 'rsw': 15, 'ppoly': 14, 'bw': 16, 'spell': 16},
                 'warrior4': {'L4': 4, 'ppdm': 13, 'rsw': 15, 'ppoly': 14, 'bw': 16, 'spell': 16},
                 'warrior5': {'L5': 5, 'ppdm': 11, 'rsw': 13, 'ppoly': 12, 'bw': 13, 'spell': 14},
                 'warrior6': {'L6': 6, 'ppdm': 11, 'rsw': 13, 'ppoly': 12, 'bw': 13, 'spell': 14},
                 'warrior7': {'L7': 7, 'ppdm': 10, 'rsw': 12, 'ppoly': 11, 'bw': 12, 'spell': 13},
                 'warrior8': {'L8': 8, 'ppdm': 10, 'rsw': 12, 'ppoly': 11, 'bw': 12, 'spell': 13},
                 'warrior9': {'L9': 9, 'ppdm': 8, 'rsw': 10, 'ppoly': 9, 'bw': 9, 'spell': 11},
                 'warrior10': {'L10': 10, 'ppdm': 8, 'rsw': 10, 'ppoly': 9, 'bw': 9, 'spell': 11},
                 'warrior11': {'L11': 11, 'ppdm': 7, 'rsw': 9, 'ppoly': 8, 'bw': 8, 'spell': 10},
                 'warrior12': {'L12': 12, 'ppdm': 7, 'rsw': 9, 'ppoly': 8, 'bw': 8, 'spell': 10},
                 'warrior13': {'L13': 13, 'ppdm': 5, 'rsw': 7, 'ppoly': 6, 'bw': 5, 'spell': 8},
                 'warrior14': {'L14': 14, 'ppdm': 5, 'rsw': 7, 'ppoly': 6, 'bw': 5, 'spell': 8},
                 'warrior15': {'L15': 15, 'ppdm': 4, 'rsw': 6, 'ppoly': 5, 'bw': 4, 'spell': 7},
                 'warrior16': {'L16': 16, 'ppdm': 4, 'rsw': 6, 'ppoly': 5, 'bw': 4, 'spell': 7},
                 'warrior17': {'L17': 17, 'ppdm': 3, 'rsw': 5, 'ppoly': 4, 'bw': 4, 'spell': 4},

                 'wizard1': {'L1': 1, 'ppdm': 14, 'rsw': 11, 'ppoly': 13, 'bw': 15, 'spell': 12},
                 'wizard2': {'L2': 2, 'ppdm': 14, 'rsw': 11, 'ppoly': 13, 'bw': 15, 'spell': 12},
                 'wizard3': {'L3': 3, 'ppdm': 14, 'rsw': 11, 'ppoly': 13, 'bw': 15, 'spell': 12},
                 'wizard4': {'L4': 4, 'ppdm': 14, 'rsw': 11, 'ppoly': 13, 'bw': 15, 'spell': 12},
                 'wizard5': {'L5': 5, 'ppdm': 14, 'rsw': 11, 'ppoly': 13, 'bw': 15, 'spell': 12},
                 'wizard6': {'L6': 6, 'ppdm': 13, 'rsw': 9, 'ppoly': 11, 'bw': 13, 'spell': 10},
                 'wizard7': {'L7': 7, 'ppdm': 13, 'rsw': 9, 'ppoly': 11, 'bw': 13, 'spell': 10},
                 'wizard8': {'L8': 8, 'ppdm': 13, 'rsw': 9, 'ppoly': 11, 'bw': 13, 'spell': 10},
                 'wizard9': {'L9': 9, 'ppdm': 13, 'rsw': 9, 'ppoly': 11, 'bw': 13, 'spell': 10},
                 'wizard10': {'L10': 10, 'ppdm': 13, 'rsw': 9, 'ppoly': 11, 'bw': 13, 'spell': 10},
                 'wizard11': {'L11': 11, 'ppdm': 11, 'rsw': 7, 'ppoly': 9, 'bw': 11, 'spell': 8},
                 'wizard12': {'L12': 12, 'ppdm': 11, 'rsw': 7, 'ppoly': 9, 'bw': 11, 'spell': 8},
                 'wizard13': {'L13': 13, 'ppdm': 11, 'rsw': 7, 'ppoly': 9, 'bw': 11, 'spell': 8},
                 'wizard14': {'L4': 14, 'ppdm': 11, 'rsw': 7, 'ppoly': 9, 'bw': 11, 'spell': 8},
                 'wizard15': {'L15': 15, 'ppdm': 11, 'rsw': 7, 'ppoly': 9, 'bw': 11, 'spell': 8},
                 'wizard16': {'L16': 16, 'ppdm': 10, 'rsw': 5, 'ppoly': 7, 'bw': 9, 'spell': 6},
                 'wizard17': {'L17': 17, 'ppdm': 10, 'rsw': 5, 'ppoly': 7, 'bw': 9, 'spell': 6},
                 'wizard18': {'L18': 18, 'ppdm': 10, 'rsw': 5, 'ppoly': 7, 'bw': 9, 'spell': 6},
                 'wizard19': {'L19': 19, 'ppdm': 10, 'rsw': 5, 'ppoly': 7, 'bw': 9, 'spell': 6},
                 'wizard20': {'L20': 20, 'ppdm': 10, 'rsw': 5, 'ppoly': 7, 'bw': 9, 'spell': 6},
                 'wizard21': {'L21': 21, 'ppdm': 8, 'rsw': 3, 'ppoly': 5, 'bw': 7, 'spell': 4}
                 }

dwarf_home_land = ["Griff Clan", "Calaunt", "Baulders Gate", "Zhentil Keep", "Westgate", "Waterdeep", "Teziir",
                   "Tantras", "Tasseldale", "Silverymoon", "Pirate Isles", "Procampur", "Mulmaster", "Neverwinter",
                   "Moonsea City States", "Mirabar", "Impiltur", "Iriaebor", "The Great Glacier", "Elturel", "Elversult"]

elven_home_land = ['Edhesseand', 'Ellon', 'Ilienon', 'Ellonel', 'Londorwin', 'Edhel', 'Tirisea', 'Vinimris',
                   'Valoroth', 'Ningalond','Doline', 'Honargel', 'Karne', 'Evras', 'Bariande', 'Honimris', 'Nioningal',
                   'Gelasea', 'Enen', 'Gulade', 'Adrimlast', 'Brisea', 'Karnione', 'Nevrine', 'Forlothlond', 'Enon',
                   'Vallone', 'Esseavas', 'Nionyamen']

# Class Descriptions - https://redd.it/2e9vzl


char_who = ['composed ',
            'crass ',
            'guarded ',
            'soul-less ',
            'discerning ',
            'diplomatic ',
            'courageous ',
            'suspicious ',
            'callous ',
            'sentimental ',
            'methodical ',
            'egotistical '
            'cheerful ',
            'dutiful ',
            'cold ',
            'funny ',
            'delightful '
            'modest '
            'philosophical ']

char_from = ['from a complex bureaucratic society ',
             'from a high end gambling house ',
             'from a slave owning city ',
             'from a high-class brothel ',
             'from the Salt Flats Aragun',
             'from the Iceberg Sea ',
             'from a local street gang ',
             'from a secluded forest village ',
             'from a fishing village ',
             'from an unchartable island ',
             'from the Forest of Sadness ',
             'from the City of Lights ',
             'from a bustling city ',
             'from an underground network of dragon caves ',
             'from the Shifting Desert ',
             'from a war torn city ',
             'from the City of Waterdeep ',
             'from a line of fallen royalty ',
             'from The Northern Wastelands ',
             'from a forgotten Elven Monastery ',
             'from the Quality Control Brewing Association ',
             'from a desert town hidden inside a sand storm ']

fem_char_issues = ['who worries some of her memories have been tampered with',
               "who doesn't believe in hygiene",
               'who carries a charmed locket that she cannot open',
               "who in hindsight shouldn't have had that treasure map tattooed on herself",
               'who likes to speak in rhyme',
               'who was forced to watch her families execution',
               'who has no sense of smell',
               'who is searching for the knowledge of true immortality',
               'who bribed a nobleman to help her smuggle slaves out of a tyrannical kingdom',
               'who always alliterates her anecdotes',
               'who exaggerates everything she talks about',
               'who came out of retirement for this adventure',
               'who has a serious weapons fetish',
               'who is the only surviving member of her previous adventure party',
               'who ran afoul of the Goblin Mob',
               'who is completely and utterly tone-deaf',
               'who is quick to assign blame',
               'who has wooden teeth after that incident with a -= mace =-',
               'who believes in racial purity',
               'who is downright racist towards living skeletons',
               'who hates the written word',
               'who lost her shadow in a bet',
               'who likes to settle arguments with headbutting contests',
               'who makes all minor decisions by flipping a coin',
               'who drunkenly swore a blood oath and forgot what for',
               'who has anger problems']

male_char_issues = ['who worries some of his memories have been tampered with',
                    "who doesn't believe in hygiene",
                    'who carries a charmed locket that he cannot open',
                    "who in hindsight shouldn't have had that treasure map tattooed on himself",
                    'who likes to speak in rhyme',
                    'who was forced to watch his families execution',
                    'who has no sense of smell',
                    'who is searching for the knowledge of true immortality',
                    'who bribed a nobleman to help him smuggle slaves out of a tyrannical kingdom',
                    'who always alliterates his anecdotes',
                    'who exaggerates everything he talks about',
                    'who came out of retirement for this adventure',
                    'who has a serious weapons fetish',
                    'who is the only surviving member of his previous adventure party',
                    'who ran afoul of the Goblin Mob',
                    'who is completely and utterly tone-deaf',
                    'who is quick to assign blame',
                    'who has wooden teeth after that incident with a -= mace =-',
                    'who believes in racial purity',
                    'who is downright racist towards living skeletons',
                    'who hates the written word',
                    'who lost his shadow in a bet',
                    'who likes to settle arguments with headbutting contests',
                    'who makes all minor decisions by flipping a coin',
                    'who drunkenly swore a blood oath and forgot what for',
                    'who has anger problems,'
                    'who acts on impulse',
                    'who loves shiny objects',
                    'who will constantly pray at inopportune moments',
                    'who reads every book he comes across',
                    'who tries to convert everyone he meets',
                    'who is incredibly lazy',
                    'who complicates simple situations',
                    'who goes out at night secretly looking for belts',
                    'who loves shiny objects',
                    'who sees insults as an art',
                    'who talks so fast that he is very difficult to understand',
                    'who occasionally thinks aloud',
                    'who is very competitive',
                    'who keeps a very precise journal',
                    'who has a pet dog companion named Daisy',
                    'who is very selfish',
                    'who is non-materialistic',
                    'who is very intolerant towards other faiths',
                    'who would rather act than talk or think',
                    'who has a fascination with explosions',
                    "who doesn't like change",
                    'who collects bottle corks',
                    'who constantly looks for the loophole',
                    'who is always scribbling notes',
                    'who has a pet parrot companion named Jacky',
                    "who doesn't care about risks or odds",
                    'who has a solution for everything',
                    'who is an alcoholic',
                    'who spaces out often, lost in thought',
                    'who often spies on other people',
                    'who has a detailed map of everywhere he has been to',
                    'who is haunted by horrible memories',
                    'who dreams of becoming rich and famous',
                    'who is always prepared',
                    'who loves discovering new mysteries and solving them',
                    'who has lost many friends',
                    'who rarely speaks',
                    'who has a pet cat companion named Mister Man',
                    'who is very focused',
                    'who takes everything at face-value',
                    'who sees divine omens in everything',
                    'who sporadically lies',
                    "who can't stand laziness",
                    'who always carries food in his pockets',
                    'who feels ill at ease in open spaces',
                    'who is very impatient',
                    'who is more comfortable underground',
                    'who never surrenders',
                    'who always does what he is told not to',
                    'who is a pacifist',
                    'who is very courageous, to a fault',
                    'who only talks in whispers',
                    'who can see an opening in any defense',
                    'who knows all the gossip around town',
                    'who has an extra finger on his left hand',
                    'who has a problem with nervous flatulation',
                    'who has a large scar on his chest, and does NOT want to talk about it',
                    'who is allergic to goblins',
                    'who has an unfinished tribal tattoo on his right hand',
                    'who frequently hums old dwarven songs',
                    'who spends every morning training'
                    ]


starting_items = ["explorer’s outfit", "belt pouch", "chalk", "gear maintenance kit", "grooming kit", "mess kit",
                  "pot (common)", "shaving kit", "soap", "string (50 ft.)", "torch (5)",
                  "waterskin", "traveller’s outfit", "trail rations (7 days)",'sturdy boots', 'leather breeches',
                  'skirt', 'belt', 'shirt', 'vest  or  jacket', 'gloves', 'cloak',
                 'scarf', 'wide-brimmed hat']

alignment1 = ["Lawful ", "Neutral ", "Chaotic "]
alignment2 = ["Good", "Neutral", "Evil"]

dwarven_deities = ['Abbathor', 'Berronar Truesilver', 'Clanggedin Silverbeard', 'Deep Duerra', 'Dugmaren Brightmantle',
                   'Dumathoin', 'Gorm Gulthyn', 'Haela Brightaxe', 'Hanseath', 'Laduguer', 'Marthammor Duin', 'Moradin',
                   'Muamman Duathal', 'Mya', 'Roknar', 'Sharindlar', 'Thard Harr', 'Tharmekhul', 'Thautam', 'Ulaa',
                   'Valkauna', 'Vergadain',
                   ]

elven_deities = ['Aerdrie Faenya', 'Corellon Larethian', 'Deep Sashelas', 'Erevan Ilesere', 'Fenmarel Mestarine',
                 'Hanali Celanil', 'Labelas Enoreth', 'Rillifane Rallathil', 'Sehanine Moonbow', 'Solonor Thelandira',
                 'Alobal Lorfiril', 'Elebrin Liothiel', 'Vandria Gilmadrith', 'Araleth Letheranil', 'Alathrien Druanna',
                 'Darahl Firecloak', 'Kirith Sotheril', 'Melira Taralen', 'Mythrien Sarath', 'Naralis Analor',
                 'Rellavar Danuvien', 'Sarula Iliene', 'Tethrin Veralde', 'Tarsellis Meunniduin'
                 ]

halfling_deities = ['Yondalla the Provider', 'Sheela Peryroyl', 'Cyrrollalee', 'Arvoreen the Defender', 'Brandobaris']


gnome_deities = ['Baervan Wildwanderer', 'Flandal Steelskin', 'Garl Glittergold', 'Segojan Earthcaller',
                 'Callarduran Smoothhands','Urdlen'
                 ]

human_deities = ['Greyhawk', "Al'Akbar", "Azor'a", 'Amaunator', 'Auril', 'Azuth', 'Beshaba', 'Chauntea', 'Deneir',
                 'Gargauth', 'Eshowdow', 'Gond', 'Helm', 'Ilmater', 'Ibrandul'
                 ]
half_elf_deities = ['Greyhawk', "Al'Akbar", "Azor'a", 'Amaunator', 'Auril', 'Azuth', 'Beshaba', 'Chauntea', 'Deneir',
                    'Gargauth', 'Eshowdow', 'Gond', 'Helm', 'Ilmater', 'Ibrandul', 'Aerdrie Faenya', 'Corellon Larethian',
                    'Deep Sashelas', 'Erevan Ilesere', 'Fenmarel Mestarine',
                    'Hanali Celanil', 'Labelas Enoreth', 'Rillifane Rallathil', 'Sehanine Moonbow', 'Solonor Thelandira',
                    'Alobal Lorfiril', 'Elebrin Liothiel', 'Vandria Gilmadrith', 'Araleth Letheranil', 'Alathrien Druanna',
                    'Darahl Firecloak', 'Kirith Sotheril', 'Melira Taralen', 'Mythrien Sarath', 'Naralis Analor',
                    'Rellavar Danuvien', 'Sarula Iliene', 'Tethrin Veralde', 'Tarsellis Meunniduin'
                    ]

dwarven_language_list = ['Gnome', 'Goblin', 'Kobold', 'Orc', 'Elven', 'Halfling', 'Giant']
elven_language_list = ['Goblin', 'Orc', 'Hobgoblin', 'Gnoll', 'Halfling', 'Gnome']
gnome_language_list = ['Kobold', 'Goblin', 'Halfling', 'Dwarf', 'Burrowing Mammals', 'Elven']
halfling_language_list = ['Gnome', 'Goblin', 'Orc', 'Elven', 'Dwarf']
half_elf_language_list = ['Gnome', 'Halfling', 'Goblin', 'Hobgoblin', 'Orc', 'Gnoll', 'Elven']
human_language_list = ["Elven", "Giant", "Gnome", "Goblin", "Gnoll", "Halfling", "Orc", 'Dwarf']
generic_language_list = ['Elven', "Giant", "Gnome", "Goblin", "Gnoll", "Halfling", "Orc", 'Dwarf', 'Hobgoblin', 'Kobold']


religion_weapons = {"Boccob": "Quarterstaff", "Corellon Larethian": "Long Sword", "Ehlonna": "Long Bow", "Erythnul": "Morningstar", "Fharlanghn": "Quarterstaff", "Garl Glittergold": "Battleaxe", "Gruumsh": "Spear", "Heironeous": "Long Sword", "Hextor": "Flail", "Kord": "Greatsword", "Moradin": "Warhammer", "Nerull": "Scythe", "Obad Hai": "Quarterstaff", "Olidammara": "Rapier", "Pelor": "Heavy Mace", "St. Cuthbert": "Light Mace", "Vecna": "Dagger", "Wee Jas": "Dagger", "Yondalla": "Short Sword"}
religion_alignments = {"Boccob": 5, "Corellon Larethian": 7, "Ehlonna": 4, "Erythnul": 9, "Fharlanghn": 5, "Garl Glittergold": 4, "Gruumsh": 9, "Heironeous": 1, "Hextor": 3, "Kord": 7, "Moradin": 1, "Nerull": 6, "Obad Hai": 5, "Olidammara": 8, "Pelor": 4, "St. Cuthbert": 2, "Vecna": 6, "Wee Jas": 2, "Yondalla": 1}
religion_table = {1: "Lawful Good", 2: "Lawful Neutral", 3: "Lawful Evil", 4: "Neutral Good", 5: "Neutral Neutral", 6: "Neutral Evil", 7: "Chaotic Good", 8: "Chaotic Neutral", 9: "Chaotic Evil"}

cleric_armor = ['Padded', 'Leather', 'Padded Leather', 'Hide', 'Chain Shirt', 'Scalemail', 'Chainmail', 'Breastplate', 'Splintmail', 'Bandedmail', 'Half Plate']

druid_weapons = ['Club', 'Dagger', 'Quarterstaff', 'Scimitar', 'Sickle', 'Short Spear', 'Sling', 'Spear']

ranger_favored_enemies = ['Aberration', 'Animal', 'Construct', 'Dragon', 'Elemental', 'Fey', 'Giant', 'Humanoid (aquatic)', 'Humanoid (dwarf)', 'Humanoid (elf)', 'Humanoid (goblinoid)', 'Humanoid (gnoll)', 'Humanoid (gnome)', 'Humanoid (halfling)', 'Humanoid (human)', 'Humanoid (orc)', 'Humanoid (reptilian)', 'Magical beast', 'Monstrous humanoid', 'Ooze', 'Outsider (air)', 'Outsider (chaotic)', 'Outsider (earth)', 'Outsider (evil)', 'Outsider (fire)', 'Outsider (good)', 'Outsider (lawful)', 'Outsider (native)', 'Outsider (water)', 'Plant', 'Undead', 'Vermin']

druid_companions = ['Badger', 'Camel', 'Dire Rat', 'Dog', 'Riding Dog', 'Eagle', 'Hawk', 'Light Horse', 'Heavy Horse', 'Owl', 'Pony', 'Small Snake', 'Medium Snake', 'Viper', 'Wolf']

fighter_religions = ['Heironeous', 'Kord', 'St. Cuthbert', 'Hextor', 'Erythnul']

monk_weapons = ['Club', 'Light Crossbow', 'Heavy Crossbow', 'Dagger', 'Handaxe', 'Javelin', 'Kama', 'Nunchaku', 'Quarterstaff', 'Sai', 'Shuriken', 'Siangham', 'Sling']

rogue_weapons = ['Hand Crossbow', 'Sap', 'Short Bow', 'Rapier', 'Short Sword', 'Club', 'Dagger', 'Javelin', 'Light Mace', 'Heavy Mace', 'Short Spear', 'Sickle', 'Spear', 'Spiked Gauntlet', 'Great Club', 'Morningstar', 'Quarterstaff', 'Scythe', 'Sling', 'Light Crossbow', 'Heavy Crossbow']

thief_weapons = ['Hand Crossbow', 'Sap', 'Short Bow', 'Rapier', 'Short Sword', 'Club', 'Dagger', 'Javelin', 'Light Mace', 'Heavy Mace', 'Short Spear', 'Sickle', 'Spear', 'Spiked Gauntlet', 'Great Club', 'Morningstar', 'Quarterstaff', 'Scythe', 'Sling', 'Light Crossbow', 'Heavy Crossbow']


familiars = ["Bat", "Cat", "Hawk", "Lizard", "Owl", "Rat", "Raven", "Snake", "Toad", "Weasel"]

wizard_schools = {'Abjuration':2, 'Conjuration':2, 'Divination':1, 'Enchantment':2, 'Evocation':2, 'Illusion':2,
                  'Necromancy':2, 'Transmutation':2}

wizard_weapons = ['Club', 'Dagger', 'Heavy Crossbow', 'Light Crossbow', 'Quarterstaff']

barbarian_armor = ['Padded Leather', 'Padded Leather', 'Chain Shirt', 'Hide', 'Scalemail', 'Chainmail', 'Breastplate']

bard_weapons = ['Whip', 'Long Sword', 'Rapier', 'Sap', 'Short Sword', 'Short Bow', 'Dagger', 'Gauntlet', 'Light Mace',
                'Sickle', 'Club', 'Heavy Mace', 'Morningstar', 'Short Spear', 'Long Spear', 'Quarterstaff', 'Spear',
                'Heavy Crossbow', 'Light Crossbow', 'Javelin', 'Sling']

dwarf_first_names = ["Adrik", "Alberich", "Baern", "Barendd", "Brottor", "Bruenor", "Dain", "Darrak", "Delg", "Eberk",
                     "Einkil", "Fargrim", "Flint", "Gardain", "Harbek", "Kildrak", "Morgran", "Orsik", "Oskar",
                     "Rangrim", "Rurik","Taklinn", "Thoradin", "Thorin", "Tordek", "Traubon", "Travok", "Ulfgar",
                     "Veit", "Vondal"]

gender = ["Male", "Female"]

dwarf_last_names = ["Balderk", "Battlehammer", "Brawnanvil", "Dankil", "Fireforge", "Frostbeard", "Gorunn", "Holderhek",
                    "Ironfist", "Loderr", "Lutgehr", "Rumnaheim", "Strakeln", "Torunn", "Ungart"]

dwarf_clans = ["Balderk", "Dankil", "Gorunn", " Holderhek", "Loderr", "Lutgehr", "Rumnaheim", "Strakeln", "Torunn", "Ungart"]
dwarf_skin_tones = ['Deep Tan', 'Pale', 'Beige', 'Light Brown']
dwarf_hair_colors = ['Black', 'Brown', 'Grey']
dwarf_hair_types = ['Curly', 'Wavy', 'Straight']
dwarf_eye_colors = ['Brown', 'Black', 'Deep Grey']

elf_clans = ['Alfevien', 'Galerion', 'Nadriendel', 'Anuliinde', 'Calol', 'Amyl', 'Endamaar', 'Vilmadien', 'Gorfiviel',
             'Nethiar', 'Celebryl', 'Felistyr', 'Gelbalf', 'Parador', 'Geffroen', 'Rendiye', 'Deliryl', 'Meril',
             'Hil-Gamir', 'Isionia', 'Hawynn', 'Truedyl', 'Sheyallia', 'Taureshey', 'Veirdyr', 'Melydor', 'Bryhydd',
             'Feasiann', 'Sylvaria', 'Ganduil', 'Anirion', 'Lothenar', 'Chossum', 'Erendyl', 'Erewan', 'Grunalf',
             'Nornanda', 'Mealidil', 'Pilinkaarne', 'Aldtyrme', 'Diamarak', 'Etheredyl', 'Hierydyl', 'Laaseluune',
             'Wyntaarie', 'Anuwiel', 'Callathien', 'Delaldor', 'Lymandyr', 'Tanduil', 'Shiye', 'Shiye-Niur',
             'Shiye-Lyeere', 'Shiye-Taarii', 'Feadiel']

elf_first_names = ["Adran", "Aelar", "Aramil", "Arannis", "Aust", "Beiro", "Berrian", "Carric", "Enialis", "Erdan",
                   "Erevan", "Galinndan", "Hadarai", "Heian", "Himo", "Immeral", "Ivellios", "Laucian", "Mindartis",
                   "Paelias", "Peren", "Quarion", "Riardon", "Rolen", "Soveliss", "Thamior", "Tharivol", "Theren",
                   "Varis"]

elf_last_names = ["Amakiir", "Amastacia", "Galanodel", "Holimion", "Ilphelkiir", "Liadon", "Meliamne", "Nailo",
                  "Siannodel", "Xiloscient"]

elf_skin_tones = ['Light Pale', 'Pale', 'Dark Pale']
elf_hair_colors = ['Black', 'Brown', 'Grey']
elf_hair_types = ['Curly', 'Wavy', 'Straight']
elf_eye_colors = ['Light Green', 'Green', 'Dark Green', 'Green Grey']

halfling_first_names = ["Alton", "Ander", "Cade", "Corrin", "Eldon", "Errich", "Finnan", "Garret", "Lindal", "Lyle",
                        "Merric", "Milo", "Osborn", "Perrin", "Reed", "Roscoe", "Wellby"]
halfling_last_names = ["Brushgather", "Goodbarrel", "Greenbottle", "Highhill", "Hilltopple", "Leagallow", "Tealeaf",
                       "Thorngage", "Tosscobble", "Underbough"]

halfling_skin_tones = ['Light Pale', 'Pale', 'Pink']
halfling_hair_colors = ['Black', 'Dark Brown', 'Dark Red', 'Grey']
halfling_eye_colors = ['Black', 'Brown', 'Dark Green', 'Dark Grey']

half_elf_skin_tones = ['Brown', 'Beige', 'White', 'Pink']
half_elf_hair_colors = ['Black', 'Brown', 'Blond', 'Red', 'White']
half_elf_hair_types = ['Curly', 'Wavy', 'Straight']
half_elf_eye_colors = ['Amber', 'Blue', 'Brown', 'Grey', 'Green', 'Hazel']

half_orc_skin_tones = ['Black', 'Brown', 'Grey', 'White']
half_orc_hair_colors = ['Black', 'Brown', 'Blond', 'Red', 'White']
half_orc_hair_types = ['Curly', 'Wavy', 'Straight']
half_orc_eye_colors = ['Amber', 'Blue', 'Brown', 'Grey', 'Green', 'Hazel']

gnome_first_names = ["Boddynock", "Dimble", "Fonkin", "Gimble", "Glim", "Gerbo", "Jebeddo", "Namfoodle", "Roondar",
                     "Seebo", "Zook"]
gnome_last_names = ["Beren", "Daergel", "Folkor", "Garrick", "Nackle", "Murnig", "Ningel", "Raulnor", "Scheppen",
                    "Turen"]
gnome_clans = ["Beren", "Daergel", "Folkor", "Garrick", "Nackle", "Murnig", "Ningel", "Raulnor", "Scheppen", "Turen"]

gnome_nick_names = ["Aleslosh", "Ashhearth", "Badger", "Cloak", "Doublelock", "Filchbatter", "Fnipper", "Oneshoe",
                    "Sparklegem", "Stumbleduck"]

gnome_eye_colors = ['Light Blue', 'Blue', 'Dark Blue', 'Blue Grey']
gnome_hair_colors = ['Blond', 'Brown', 'White', 'Orange', 'Green']

orc_first_names = ["Dench", "Feng", "Gell", "Henk", "Holg", "Imsh", "Keth", "Krusk", "Ront", "Shump", "Thokk"]

human_first_names = ["Aseir", "Bardeid", "Haseid", "Khemed", "Mehmen", "Sudeiman", "Zasheir", "Darvin", "Dorn",
                     "Evendur", "Gorstag", "Grim", "Helm", "Malark", "Morn", "Randal", "Stedd", "Bor", "Fodel",
                     "Glar", "Grigor", "Igan", "Ivor", "Kosef", "Mival", "Orel", "Pavel", "Sergor", "Ander", "Blath",
                     "Bran", "Frath", "Geth", "Lander", "Luth", "Malcer", "Stor", "Taman", "Urth", "Aoth", "Bareris",
                     "Ehput Ki", "Kethoth", "Mumed", "Ramas", "So Kehur", "Thazar De", "Urhur" , "Borivik", "Faurgar",
                     "Jandar", "Kanithar", "Madislak", "Ralmevik", "Shaumar", "Vladislak", "Chien", "Huang", "Kao",
                     "Kung", "Lao", "Ling", "Mei", "Pin", "Shin", "Sum", "Tan", "Wan", "Anton", "Diero", "Marcon",
                     "Pieron", "Rimardo", "Romero", "Salazar", "Umbero"
                     ]


human_last_names = ["Basha", "Dumein", "Jassan", "Khalid", "Mostana", "Pashar", "Rein", "Amblecrown", "Buckman",
                    "Dundragon", "Evenwood", "Greycastle", "Tallstag", "Bersk", "Chernin", "Dotsk", "Kulenov", "Marsk",
                    "Nemetsk", "Shemov", "Starag", "Brightwood", "Helder", "Hornraven", "Lackman", "Stormwind",
                    "Windrivver", "Ankhalab", "Anskuld", "Fezim", "Hahpet", "Nathandem", "Sepret", "Uuthrakt",
                    "Ankhalab", "Anskuld", "Fezim", "Hahpet", "Nathandem", "Sepret", "Uuthrakt", "An", "Chen", "Chi",
                    "Fai", "Jiang", "Jun", "Lian", "Long", "Meng", "On", "Shan", "Shui", "Wen", "Agosto", "Astorio",
                    "Calabra", "Domine", "Falone", "Marivaldi", "Pisacar", "Ramondo"
                    ]


human_tribes = ["Calishite", "Chondathan", "Damaran", "Illuskan", "Mulan", "Rashemi", "Shou", "Turami"]
human_skin_tones = ['Black', 'Brown', 'Beige', 'White', 'Pink', 'Tan', 'Olive']
human_hair_colors = ['Black', 'Brown', 'Blond', 'Red', 'White', 'Grey']
human_hair_types = ['Curly', 'Wavy', 'Straight', 'Flowing', 'Frizzy', 'Spiky', 'Touseled', 'Unkempt']
human_eye_colors = ['Amber', 'Blue', 'Brown', 'Grey', 'Green', 'Hazel']

religion_domains = {
"Boccob": ["Knowledge", "Magic", "Trickery"],
"Corellon Larethian": ["Chaos", "Good", "Protection", "War"],
"Ehlonna": ["Animal", "Good", "Plant", "Sun"],
"Erythnul": ["Chaos", "Evil", "Trickery", "War"],
"Fharlanghn": ["Luck", "Protection", "Travel"],
"Garl Glittergold": ["Good", "Protection", "Trickery"],
"Gruumsh": ["Chaos", "Evil", "Strength"],
"Heironeous": ["Good", "Law", "War"],
"Hextor": ["Destruction", "Evil", "Law", "War"],
"Kord": ["Chaos", "Good Luck", "Strength"],
"Moradin": ["Earth", "Good", "Law", "Protection"],
"Nerull": ["Death", "Evil", "Trickery"],
"Obad Hai": ["Air", "Animal", "Earth", "Fire", "Plant", "Water"],
"Olidammara": ["Chaos", "Luck", "Trickery"],
"Pelor": ["Good", "Healing", "Strength"],
"St. Cuthbert": ["Destruction", "Law", "Protection", "Strength"],
"Vecna": ["Evil", "Knowledge", "Magic"],
"Wee Jas": ["Death", "Law", "Magic"],
"Yondalla": ["Good", "Law", "Protection"],
}


weapon_data = {
"Gauntlet": {"Cost": 2, "Damage (S)": "1d2", "Damage (M)": "1d3", "Critical": 2, "Weight": 1, "Type": "Bludgeoning", "Handed": "One"},
"Dagger": {"Cost": 2, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 2, "Weight": 1, "Type": "Bludgeoning", "Handed": "One"},
"Spiked Gauntlet": {"Cost": 5, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 2, "Weight": 1, "Type": "Piercing", "Handed": "One"},
"Light Mace": {"Cost": 5, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 4, "Type": "Bludgeoning", "Handed": "One"},
"Sickle": {"Cost": 6, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 2, "Type": "Slashing", "Handed": "One"},
"Club": {"Cost": 0, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 3, "Type": "Bludgeoning", "Handed": "One"},
"Heavy Mace": {"Cost": 12, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 2, "Weight": 8, "Type": "Bludgeoning", "Handed": "One"},
"Morningstar": {"Cost": 8, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 2, "Weight": 8, "Type": "Bludgeoning and Piercing", "Handed": "One"},
"Short Spear": {"Cost": 1, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 3, "Type": "Piercing", "Handed": "One"},
"Long Spear": {"Cost": 5, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 3, "Weight": 9, "Type": "Piercing", "Handed": "Two"},
"Quarterstaff": {"Cost": 0, "Damage (S)": "2d6", "Damage (M)": "2d6", "Critical": 2, "Weight": 4, "Type": "Bludgeoning", "Handed": "Two"},
"Spear": {"Cost": 2, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 3, "Weight": 6, "Type": "Piercing", "Handed": "Two"},
"Heavy Crossbow": {"Cost": 50, "Damage (S)": "1d8", "Damage (M)": "1d10", "Critical": 2, "Weight": 8, "Type": "Piercing", "Handed": "One"},
"Light Crossbow": {"Cost": 35, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 2, "Weight": 4, "Type": "Piercing", "Handed": "One"},
"Javelin": {"Cost": 1, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 2, "Type": "Piercing", "Handed": "One"},
"Sling": {"Cost": 0, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 2, "Weight": 0, "Type": "Bludgeoning", "Handed": "One"},
"Throwing Axe": {"Cost": 8, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 2, "Type": "Slashing", "Handed": "One"},
"Light Hammer": {"Cost": 1, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 2, "Weight": 2, "Type": "Bludgeoning", "Handed": "One"},
"Handaxe": {"Cost": 6, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 3, "Weight": 3, "Type": "Slashing", "Handed": "One"},
"Kukri": {"Cost": 8, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 2, "Weight": 2, "Type": "Slashing", "Handed": "One"},
"Light Pick": {"Cost": 4, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 4, "Weight": 3, "Type": "Piercing", "Handed": "One"},
"Sap": {"Cost": 1, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 2, "Type": "Bludgeoning", "Handed": "One"},
"Short Sword": {"Cost": 10, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 2, "Type": "Piercing", "Handed": "One"},
"Battleaxe": {"Cost": 10, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 3, "Weight": 6, "Type": "Slashing", "Handed": "One"},
"Flail": {"Cost": 8, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 2, "Weight": 5, "Type": "Bludgeoning", "Handed": "One"},
"Long Sword": {"Cost": 15, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 2, "Weight": 4, "Type": "Slashing", "Handed": "One"},
"Heavy Pick": {"Cost": 8, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 4, "Weight": 6, "Type": "Piercing", "Handed": "One"},
"Rapier": {"Cost": 20, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 2, "Type": "Piercing", "Handed": "One"},
"Scimitar": {"Cost": 15, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 4, "Type": "Slashing", "Handed": "One"},
"Trident": {"Cost": 15, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 2, "Weight": 4, "Type": "Piercing", "Handed": "One"},
"Warhammer": {"Cost": 12, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 3, "Weight": 5, "Type": "Bludgeoning", "Handed": "One"},
"Falchion": {"Cost": 75, "Damage (S)": "1d6", "Damage (M)": "2d4", "Critical": 2, "Weight": 8, "Type": "Slashing", "Handed": "Two"},
"Glaive": {"Cost": 8, "Damage (S)": "1d8", "Damage (M)": "1d10", "Critical": 3, "Weight": 10, "Type": "Slashing", "Handed": "Two"},
"Greataxe": {"Cost": 20, "Damage (S)": "1d10", "Damage (M)": "1d12", "Critical": 3, "Weight": 12, "Type": "Slashing", "Handed": "Two"},
"Great Club": {"Cost": 5, "Damage (S)": "1d8", "Damage (M)": "1d10", "Critical": 2, "Weight": 8, "Type": "Bludgeoning", "Handed": "Two"},
"Heavy Flail": {"Cost": 15, "Damage (S)": "1d8", "Damage (M)": "1d10", "Critical": 2, "Weight": 10, "Type": "Bludgeoning", "Handed": "Two"},
"Greatsword": {"Cost": 50, "Damage (S)": "1d10", "Damage (M)": "2d6", "Critical": 2, "Weight": 8, "Type": "Slashing", "Handed": "Two"},
"Guisarme": {"Cost": 9, "Damage (S)": "1d6", "Damage (M)": "2d4", "Critical": 3, "Weight": 12, "Type": "Slashing", "Handed": "Two"},
"Halberd": {"Cost": 10, "Damage (S)": "1d8", "Damage (M)": "1d10", "Critical": 3, "Weight": 12, "Type": "Piercing or Slashing", "Handed": "Two"},
"Lance": {"Cost": 10, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 3, "Weight": 10, "Type": "Piercing", "Handed": "Two"},
"Ranseur": {"Cost": 10, "Damage (S)": "1d6", "Damage (M)": "2d4", "Critical": 3, "Weight": 12, "Type": "Piercing", "Handed": "Two"},
"Scythe": {"Cost": 18, "Damage (S)": "1d6", "Damage (M)": "2d4", "Critical": 4, "Weight": 10, "Type": "Piercing or Slashing", "Handed": "Two"},
"Long Bow": {"Cost": 75, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 3, "Weight": 3, "Type": "Piercing", "Handed": "Two"},
"Short Bow": {"Cost": 30, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 3, "Weight": 2, "Type": "Piercing", "Handed": "Two"},
"Kama": {"Cost": 2, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 2, "Type": "Slashing", "Handed": "One"},
"Nunchaku": {"Cost": 2, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 0, "Type": "Bludgeoning", "Handed": "One"},
"Sai": {"Cost": 1, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 2, "Weight": 1, "Type": "Bludgeoning", "Handed": "One"},
"Siangham": {"Cost": 3, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 1, "Type": "Piercing", "Handed": "One"},
"Bastard Sword": {"Cost": 35, "Damage (S)": "1d8", "Damage (M)": "1d10", "Critical": 2, "Weight": 6, "Type": "Slashing", "Handed": "One"},
"Dwarven Waraxe": {"Cost": 30, "Damage (S)": "1d8", "Damage (M)": "1d10", "Critical": 3, "Weight": 8, "Type": "Slashing", "Handed": "One"},
"Whip": {"Cost": 1, "Damage (S)": "1d2", "Damage (M)": "1d3", "Critical": 2, "Weight": 2, "Type": "Slashing", "Handed": "One"},
"Orc Doubleaxe": {"Cost": 60, "Damage (S)": "2d6", "Damage (M)": "2d8", "Critical": 3, "Weight": 15, "Type": "Slashing", "Handed": "Two"},
"Spiked Chain": {"Cost": 25, "Damage (S)": "1d6", "Damage (M)": "2d4", "Critical": 3, "Weight": 10, "Type": "Piercing", "Handed": "Two"},
"Dire Flail": {"Cost": 90, "Damage (S)": "2d6", "Damage (M)": "2d8", "Critical": 2, "Weight": 10, "Type": "Bludgeoning", "Handed": "Two"},
"Gnome Hooked Hammer": {"Cost": 20, "Damage (S)": "2d5", "Damage (M)": "2d7", "Critical": 3.5, "Weight": 6, "Type": "Bludgeoning and piercing", "Handed": "Two"},
"Two Bladed Sword": {"Cost": 100, "Damage (S)": "2d6", "Damage (M)": "2d8", "Critical": 2, "Weight": 10, "Type": "Slashing", "Handed": "Two"},
"Dwarven Urgrosh": {"Cost": 50, "Damage (S)": "2d5", "Damage (M)": "2d7", "Critical": 3, "Weight": 12, "Type": "Slashing or Piercing", "Handed": "Two"},
"Bolas": {"Cost": 5, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 2, "Weight": 2, "Type": "Bludgeoning", "Handed": "One"},
"Hand Crossbow": {"Cost": 100, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 2, "Weight": 2, "Type": "Piercing", "Handed": "One"},
"Heavy Repeating Crossbow": {"Cost": 400, "Damage (S)": "1d8", "Damage (M)": "1d10", "Critical": 2, "Weight": 12, "Type": "Piercing", "Handed": "One"},
"Light Repeating Crossbow": {"Cost": 250, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 2, "Weight": 6, "Type": "Piercing", "Handed": "One"},
"Net": {"Cost": 20, "Damage (S)": "0", "Damage (M)": "0", "Critical": 0, "Weight": 6, "Type": "None", "Handed": "Two"},
"Shuriken": {"Cost": 1, "Damage (S)": "1", "Damage (M)": "1d2", "Critical": 2, "Weight": 0.5, "Type": "Piercing", "Handed": "One"},
"Unarmed": {"Cost": 0, "Damage (S)": "1", "Damage (M)": "1", "Critical": 0, "Weight": 0, "Type": "Bludgeoning", "Handed": "One"}
}
armor_data = {
"None": {"Cost": 0, "Armor Bonus": 0, "Max Dex Bonus": 100, "Armor Check": 0, "Arcane Spell Failure": 0, "Weight": 0, "Class": "None"},
"Padded": {"Cost": 5, "Armor Bonus": 1, "Max Dex Bonus": 8, "Armor Check": 0, "Arcane Spell Failure": 5, "Weight": 10, "Class": "Light"},
"Leather": {"Cost": 10, "Armor Bonus": 2, "Max Dex Bonus": 6, "Armor Check": 0, "Arcane Spell Failure": 10, "Weight": 15, "Class": "Light"},
"Padded Leather": {"Cost": 25, "Armor Bonus": 3, "Max Dex Bonus": 5, "Armor Check": -1, "Arcane Spell Failure": 15, "Weight": 20, "Class": "Light"},
"Chain Shirt": {"Cost": 100, "Armor Bonus": 4, "Max Dex Bonus": 4, "Armor Check": -2, "Arcane Spell Failure": 20, "Weight": 25, "Class": "Light"},
"Hide": {"Cost": 15, "Armor Bonus": 3, "Max Dex Bonus": 4, "Armor Check": 3, "Arcane Spell Failure": 20, "Weight": 25, "Class": "Medium"},
"Scalemail": {"Cost": 50, "Armor Bonus": 4, "Max Dex Bonus": 3, "Armor Check": 4, "Arcane Spell Failure": 25, "Weight": 30, "Class": "Medium"},
"Chainmail": {"Cost": 150, "Armor Bonus": 5, "Max Dex Bonus": 2, "Armor Check": 5, "Arcane Spell Failure": 30, "Weight": 40, "Class": "Medium"},
"Breastplate": {"Cost": 200, "Armor Bonus": 5, "Max Dex Bonus": 3, "Armor Check": -4, "Arcane Spell Failure": 25, "Weight": 30, "Class": "Medium"},
"Splintmail": {"Cost": 200, "Armor Bonus": 6, "Max Dex Bonus": 0, "Armor Check": 7, "Arcane Spell Failure": 40, "Weight": 45, "Class": "Heavy"},
"Bandedmail": {"Cost": 250, "Armor Bonus": 6, "Max Dex Bonus": 1, "Armor Check": 6, "Arcane Spell Failure": 35, "Weight": 35, "Class": "Heavy"},
"Half Plate": {"Cost": 600, "Armor Bonus": 7, "Max Dex Bonus": 0, "Armor Check": 7, "Arcane Spell Failure": 40, "Weight": 50, "Class": "Heavy"},
"Buckler": {"Cost": 15, "Armor Bonus": 1, "Armor Check": 1, "Arcane Spell Failure": 5, "Weight": 5, "Class": "Light"},
"Light Wooden": {"Cost": 3, "Armor Bonus": 1, "Armor Check": 1, "Arcane Spell Failure": 5, "Weight": 5, "Class": "Light"},
"Light Steel": {"Cost": 9, "Armor Bonus": 1, "Armor Check": 1, "Arcane Spell Failure": 5, "Weight": 6, "Class": "Light"},
"Heavy Wooden": {"Cost": 7, "Armor Bonus": 2, "Armor Check": 12, "Arcane Spell Failure": 15, "Weight": 10, "Class": "Heavy"},
"Heavy Steel": {"Cost": 20, "Armor Bonus": 2, "Armor Check": 12, "Arcane Spell Failure": 15, "Weight": 15, "Class": "Heavy"}
}

################################################################################
## Building out Proficiencies
half_elf_skills_list = ["Athletics", "Acrobatics", "Sleight", "Stealth", "Arcana", "History", "Investigation",
                        "Nature", "Religion", "Animal", "Insight", "Medicine", "Perception", "Survival",
                        "Deception", "Intimidation", "Performance", "Persuasion"]
rogue_skills_list = ["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation",
                     "Investigation", "Perception", "Performance", "Persuasion","Sleight (of hand)", "Stealth"]
ranger_skills_list = ["Animal", "Athletics", "Insight", "Investigation", "Nature","Perception", "Stealth", "Survival"]
paladin_skills_list = ["Athletics", "Insight", "Intimidation", "Medicine", "Persuasion", "Religion"]
fighter_skills_list = ["Acrobatics", "Animal", "Athletics", "History", "Insight", "Intimidation","Perception", "Survival"]
druid_skills_list = ["Arcana", "Animal", "Insight", "Medicine", "Nature", "Perception","Religion", "Survival"]
cleric_skills_list = ["History", "Insight", "Medicine", "Persuasion", "Religion"]
barbarian_skills_list = ["Animal", "Athletics", "Intimidation", "Nature", "Perception", "Survival"]
wizard_skills_list = ["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"]

bard_skills_list = ["Athletics", "Acrobatics", "Sleight", "Stealth", "Arcana", "History", "Investigation",
                    "Nature", "Religion", "Animal", "Insight", "Medicine", "Perception", "Survival", "Deception",
                    "Intimidation", "Performance", "Persuasion"]



skill_list = {
"Barbarian": ["Climb", "Craft", "Handle Animal", "Intimidate", "Jump", "Listen", "Ride", "Survival", "Swim"],
"Bard": ["Appraise", "Balance", "Bluff", "Climb", "Concentration", "Craft", "Decipher Script", "Diplomacy", "Disguise", "Escape Artist", "Gather Information", "Hide", "Intimidate", "Jump", "Knowledge (arcana)", "Knowledge (architecture and engineering)", "Knowledge (dungeoneering)", "Knowledge (geography)", "Knowledge (history)", "Knowledge (local)", "Knowledge (nature)", "Knowledge (nobility and royalty)", "Knowledge (religion)", "Knowledge (the planes)", "Listen", "Move Silently", "Perform", "Profession", "Ride", "Search", "Sense Motive", "Sleight of Hand", "Speak Language", "Spellcraft", "Swim", "Tumble", "Use Magic Device"],
"Cleric": ["Concentration", "Craft", "Diplomacy", "Heal", "Knowledge (arcana)", "Knowledge (history)", "Knowledge (religion)", "Knowledge (the planes)", "Profession", "Spellcraft"],
"Druid": ["Concentration", "Craft", "Diplomacy", "Handle Animal", "Heal", "Knowledge (nature)", "Listen", "Profession", "Ride", "Spellcraft", "Spot", "Survival", "Swim"],
"Fighter": ["Climb", "Craft", "Handle Animal", "Intimidate", "Jump", "Ride", "Swim"],
"Monk": ["Balance", "Climb", "Concentration", "Craft", "Diplomacy", "Escape Artist", "Hide", "Jump", "Knowledge (arcana)", "Knowledge (religion)", "Listen", "Move Silently", "Perform", "Profession", "Sense Motive", "Spot", "Swim", "Tumble"],
"Paladin": ["Concentration", "Craft", "Diplomacy", "Handle Animal", "Heal", "Knowledge (nobility and royalty)", "Knowledge (religion)", "Profession", "Ride", "Sense Motive", "Spot", "Swim", "Tumble"],
"Ranger": ["Climb", "Concentration", "Craft", "Handle Animal", "Heal", "Hide", "Jump", "Knowledge (local)", "Listen", "Move Silently", "Profession", "Ride", "Search", "Spot", "Survival", "Swim", "Use Rope"],
"Rogue": ["Appraise", "Balance", "Bluff", "Climb", "Craft", "Decipher Script", "Diplomacy", "Disable Device", "Disguise", "Escape Artist", "Forgery", "Gather Information", "Hide", "Intimidate", "Jump", "Knowledge (local)", "Listen", "Move Silently", "Open Lock", "Perform", "Profession", "Search", "Sense Motive", "Sleight of Hand", "Spot", "Swim", "Tumble", "Use Magic Device", "Use Rope"],
"Sorcerer": ["Bluff", "Concentration", "Craft", "Knowledge (arcana)", "Profession", "Spellcraft"],
"Wizard": ["Concentration", "Craft", "Decipher Script", "Knowledge (Arcana)", "Knowledge (Architecture and Engineering)", "Knowledge (Dungeoneering)", "Knowledge (Geography)", "Knowledge (History)", "Knowledge (Local)", "Knowledge (Nature)", "Knowledge (Nobility and Royalty)", "Knowledge (Religion)", "Knowledge (The Planes)", "Spellcraft", "Profession"],
"Thief": ["Pick Pockets", "Open Locks", "Find/Remove Traps", "Move Silently", "Hide in Shadows",	"Detect Noise",	"Climb Walls", "Read Languages"]
}
class_health = {"Barbarian": 12, "Bard": 6, "Cleric": 8, "Druid": 8, "Fighter": 10, "Monk": 8, "Paladin": 10, "Ranger": 8, "Sorcerer": 4, "Rogue": 6, "Wizard": 4, "Thief": 6}
class_xp = {"Barbarian": 4, "Bard": 6, "Cleric": 2, "Druid": 4, "Fighter": 2, "Monk": 4, "Paladin": 2, "Ranger": 6, "Sorcerer": 2, "Rogue": 8, "Wizard": 2, "Thief": 8}


class_short = [
    "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Paladin", "Ranger", "Rogue", "Wizard"
]

# NPC Class Info - http://www.5esrd.com/gamemastering/monsters-foes/npc/

class_npc = [
    "Acolyte", "Archmage", "Assassin", "Bandit Captain", "Bandit Lord", "Bandit / Pirate", "Berserker", "Black Knight Commander", "City Watch Captain", "Commoner", "Cult Fanatic", "Cult Leader", "Cult Sorcerer", "Cultist", "Devilbound Gnomish Prince", "Druid", "Dwarven Ringmage", "Elvish Veteran Archer", "Ghost Knight", "Gladiator", "Guard", "Half-Red Dragon Veteran", "Knight", "Mage", "Noble", "Corrupted Ogre Chieftain", "Priest", "Ratfolk Rogue", "Scorpion Cultist", "Scout", "Spy", "Thug", "Tribal Warrior", "Veteran", "Wolf Reaver Dwarf"
]

culture_npc = [
    "Babylonian", "Celtic", "Egyptian", "Greek", "Roman", "Sumerian", "English", "French", "German", "Italian", "Norse", "Saxon", "Slavic", "Spanish", "Arabic", "Chineese", "Hebrew", "Hindu", "Japanese", "Mongolian", "Persian", "Congolese", "Etheopian", "Malian", "Algonquin", "Aztec", "Inkan", "Inuit", "Navajo", "Sioux"
]

avg_stats = [
    "   Race        Height  Weight         Lifespan",
    "   ----        ------  ------         --------",
    "   Dwarf       4-5'    150 lbs.         350 years",
    "   Elf         5-6'+   150-170 lbs.     750 years",
    "   Halfling    3-4'    40 lbs.          150 years",
    "   Human       5-6'    130-200 lbs.   < 100 years",
    "   Gnome       3-4'    40 lbs.          350 years",
    "   Half-Elf    5-6'    130-170 lbs.     180 years",
]

abilities = [
    "   Strength      - natural athleticism, bodily power",
    "   Dexterity     - physical agility, reflexes, balance, poise",
    "   Constitution  - health, stamina, vital force",
    "   Intelligence  - mental acuity, information recall, analytical skill",
    "   Wisdom        - awareness, intuition, insight",
    "   Charisma      - confidence, eloquence, leadership",
]


niche_feats = ["Combat Experience (int 13)", "Dodge (dex 13)", "Power Attack (str 13)", "Simple Weapon Proficency (druids, monks, rogues, and wizards)", "Spell Mastery (Wizard)", "Two weapon fighting (Dex 15)"]

feat_list = ["Acrobatic", "Agile", "Alertness", "Animal Affinity", "Armor Proficency", "Athletic", "Blind Fight", "Combat Casting", "Combat Reflexes", "Deceitful", "Deft Hands", "Diligent", "Endurance", "Eschew Materials", "Great Fortitude", "Improved Counterspell", "Improved Initiative", "Improved Unarmed Strike", "Investigator", "Iron Will", "Lightning Reflexes", "Magical Aptitude", "Martial Weapon Proficency", "Negotiator", "Nimble Fingers", "Persuasive", "Point Blank Shot", "Run", "Self Sufficent", "Skill Focus", "Spell Focus", "Spell Penetration", "Stealthy", "Toughness", "Track"]

melee_weapons = ["Club", "Dagger", "Javelin", "Light Mace", "Heavy Mace", "Short Spear", "Sickle", "Spear", "Spiked Gauntlet", "Great Club", "Morningstar", "Quarterstaff", "Scythe"]
ranged_weapons = ["Light Crossbow", "Sling", "Heavy Crossbow"]

armor = ["Padded", "Leather", "Padded Leather", "Chain Shirt", "Hide", "Scalemail", "Chainmail", "Breastplate", "Splintmail", "Bandedmail", "Half Plate"]
shields = ["Light Wooden", "Light Steel", "Heavy Wooden", "Heavy Steel", "Buckler"]

religions = ["Heironeous", "Moradin", "Yondalla", "Ehlonna", "Garl Glittergold", "Pelor", "Corellon Larethian",
             "Kord", "Wee Jas", "St. Cuthbert", "Boccob", "Fharlanghn", "Obad Hai", "Olidammara", "Hextor", "Nerull",
             "Vecna", "Erythnul", "Gruumsh"]
