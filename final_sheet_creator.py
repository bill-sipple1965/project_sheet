#!/usr/bin/env python3
import random
from tools_data import *
from prettytable import PrettyTable
import os
import re


input_class = ''
input_race = ''


def list_to_string(list):
    return ', '.join(str(x) for x in list)


d6 = lambda: random.randint(1, 6)


def roll_att():
    rollout = (d6(), d6(), d6(), d6())
    return sum(rollout) - min(rollout)


def rollout_attributes():
    return [
        roll_att(),
        roll_att(),
        roll_att(),
        roll_att(),
        roll_att(),
        roll_att()
    ]


def attributes_are_valid(attributes):
    over_fifteen = filter(lambda attr: attr >= 15, attributes)
    return len(list(over_fifteen)) >= 2


def assign_attributes(attribute_list):
    attribute_dict = dict()
    name_list = {'str', 'dex', 'int', 'wis', 'con', 'cha'}
    full_attrib = []
    for attr in attribute_list:
        while True:
            check_attrib = input('Die roll = {}, \nassign this to?: {}\n'.format(attr, name_list))
            if check_attrib in name_list and check_attrib not in attribute_dict.keys():
                attribute_dict[check_attrib] = attr
                name_list.remove(check_attrib)
            if check_attrib == 'str':
                full_attrib = 'Strength'
            elif check_attrib == 'dex':
                full_attrib = 'Dexterity'
            elif check_attrib == 'wis':
                full_attrib = 'Wisdom'
            elif check_attrib == 'con':
                full_attrib = 'Constitution'
            elif check_attrib == 'cha':
                full_attrib = 'Charisma'
            elif check_attrib == 'int':
                full_attrib = 'Intelligence'
            break

        print(attr, 'Has been assigned to', full_attrib)

    return attribute_dict


def get_race_stats():  # grabs info from the user
    attributes = rollout_attributes()

    while not attributes_are_valid(attributes):
        attributes = rollout_attributes()

    print('#' * 39)
    print('### Character Generator for AD&D 2e ###')
    print('#' * 39 + '\n')
    player_name = input("Player's Name:? \n")
    print('Welcome to your Character Creator . . . ', player_name)
    print("\n\nChoose your character's gender:")
    print("  (R)andom")
    print("  (M)ale")
    print("  (F)emale")
    gender = input("Enter character gender [R]: ")
    if gender in ("R", "r", "Random", "random", ""):
        gender = random.choice("MF")
        pass
    if gender in ("M", "m", "Male", "male"):
        gender = "Male"
        pass
    elif gender in ("F", "f", "Female", "female"):
        gender = "Female"
        pass
    print('')
    print('\nRolling ability scores\n')
    print(attributes)


    rolled_stats = assign_attributes(attributes)
    valid_race_list = []

    for race in sorted(race_list):  # Loop through all races dictionary

        valid_counter = 0  # Set valid_counter for attribute stat checks for a race
        for stat in sorted(race_list[race]):  # Loop through a race stats dictionary
            if rolled_stats[stat] >= race_list[race][stat][0] and rolled_stats[stat] <= race_list[race][stat][1]:
                # Do bounds checking of rolled stats to race min/max
                valid_counter += 1  # if rolled stat is in bounds increment valid_counter

        if valid_counter == len(
                rolled_stats):  # if valid_counter equals size of rolled_stats we have a valid race to rolled stats
            valid_race_list.append(race)

    #os.system('clear')
    print("\nYour rolled ability scores allow your character to be any of the following:")  # Output a valid race
    for race in valid_race_list:
        print('{}{}'.format(race, race_desc[race]))


#    os.system('clear')
    user_input = str.title(input('Select a Race\n\n[Enter] for random\n'))
    user_race = user_input

    str_stat = rolled_stats['str']
    dex_stat = rolled_stats['dex']
    con_stat = rolled_stats['con']
    int_stat = rolled_stats['int']
    wis_stat = rolled_stats['wis']
    cha_stat = rolled_stats['cha']


    ud = {}

    def roll_dice(roll):
        values = [int(x) for x in re.findall(r'\d+', roll)]
        drop = 0
        if 'D' in roll:
            drop = values[2]
        top_rolls = sorted(list(random.randint(1, values[1]) for _ in range(values[0])))
        return sum(top_rolls[drop:])

    def pb(skill):
        return (ud[skill] - 10) // 2

    def add_list(list, source, times=1):
        if 'x' in ud[list]:
            ud[list].pop(0)
        for i in range(times):
            ud[list].append(random.choice(source))
        while len(ud[list]) != len(set(ud[list])):
            ud[list].pop()
            ud[list].append(random.choice(source))
        return

    ud['Languages'] = ['Common']
    ud['Feats'] = ['x']
    ud['Skills'] = ['x']
    ud['Domains'] = ['x']
    ud['Forbidden Schools'] = ['x']
    ud['Alignment'] = random.choice(alignment1) + random.choice(alignment2)
    ud['School'] = ''
    ud['Familiar'] = ''
    ud['Armor'] = 'None'
    ud['Shield'] = 'None'
    ud['Weapon'] = 'Unarmed'
    ud['Religion'] = 'None'
    ud['str'] = str_stat
    ud['dex'] = dex_stat
    ud['con'] = con_stat
    ud['int'] = int_stat
    ud['wis'] = wis_stat
    ud['cha'] = cha_stat
    str_adj = ud['str']
    dex_adj = ud['dex']
    con_adj = ud['con']
    int_adj = ud['int']
    wis_adj = ud['wis']
    cha_adj = ud['cha']
    str_stat_adj = 'str{}'.format(str_adj)  ## This replaces the str1-18 in the strength_stats
    dex_stat_adj = 'dex{}'.format(dex_adj)  ## This replaces the dex1-19 in the dexterity_stats
    con_stat_adj = 'con{}'.format(con_adj)  ## This replaces the cond1-19 in the constitution_stats
    int_stat_adj = 'int{}'.format(int_adj)
    wis_stat_adj = 'wis{}'.format(wis_adj)
    cha_stat_adj = 'cha{}'.format(cha_adj)

    if user_race == 'Dwarf':
        ud['first_name'] = '{}'.format(random.choice(dwarf_first_names))
        ud['last_name'] = '{}'.format(random.choice(dwarf_last_names))
        ud['clan'] = '{}'.format(random.choice(dwarf_clans))
#        ud['Name'] = '{} {}, of the clan {}'.format(ud['first_name'], ud['last_name'], ud['clan'])
        ud['table_name'] = '{} {}'.format(ud['first_name'], ud['last_name'])
        if random.random() > 0.8:
            ud['Religion'] = 'Moradin'
#        ud['Age'] = int(random.normalvariate(80, 10))
        ud['Height'] = roll_dice('2d4') + 45
        ud['Weight'] = 130 + roll_dice('2d6') * (ud['Height'] - 45)
        ud['height'] = str(ud['Height'])
        ud['weight'] = str(ud['Weight'])
        ud['con'] + 1
        ud['cha'] - 1
        ud['Languages'].append('Dwarven')
        ud['Size'] = 1
        ud['Skin Tone'] = random.choice(dwarf_skin_tones)
        ud['Hair Color'] = random.choice(dwarf_hair_colors)
        ud['Hair Type'] = random.choice(dwarf_hair_types)
        ud['Eye Color'] = random.choice(dwarf_eye_colors)
        ud['fam'] = '{}'.format(random.choice(dwarf_last_names))
        ud['home'] = '{}'.format(random.choice(dwarf_home_land))
        ud['age_base'] = roll_dice('5d6') + 100
        ud['age_max'] = roll_dice('4d100') + 350
        ud['age'] = '{}'.format(str(ud['age_base'])) + '({})'.format(str(ud['age_max']))
        ud['siblings'] = roll_dice('2d10')
        rank = int(ud['siblings']) // 3
        ud['birth_rank'] = str(rank)
        ud['social_class'] = '{}'.format(random.choice(social_class_list))
        ud['level'] = '1'
        ud['XP'] = '0'

    if user_race == 'Elf':
        ud['first_name'] = '{}'.format(random.choice(elf_first_names))
        ud['last_name'] = '{}'.format(random.choice(elf_last_names))
        ud['clan'] = '{}'.format(random.choice(elf_clans))
#        ud['Name'] = '{} {}, of the clan {}'.format(ud['first_name'], ud['last_name'], ud['clan'])
        ud['table_name'] = '{} {}'.format(ud['first_name'], ud['last_name'])
        if random.random() > 0.8:
            ud['Religion'] = 'Corellon Larethian'
#        ud['Age'] = int(random.normalvariate(140, 10))
        ud['Height'] = roll_dice('2d6') + 58
        ud['Weight'] = 85 + roll_dice('1d6') * (ud['Height'] - 58)
        ud['height'] = str(ud['Height'])
        ud['weight'] = str(ud['Weight'])
        ud['dex'] + 1
        ud['con'] - 1
        ud['Languages'].append('Elven')
        ud['Size'] = 1
        ud['Skin Tone'] = random.choice(elf_skin_tones)
        ud['Hair Color'] = random.choice(elf_hair_colors)
        ud['Hair Type'] = random.choice(elf_hair_types)
        ud['Eye Color'] = random.choice(elf_eye_colors)
        ud['age_base'] = roll_dice('5d6') + 100
        ud['age_max'] = roll_dice('4d100') + 350
        ud['age'] = '{}'.format(str(ud['age_base'])) + '({})'.format(str(ud['age_max']))
        ud['fam'] = '{}'.format(random.choice(elf_last_names))
        ud['home'] = '{}'.format(random.choice(elven_home_land))
        ud['siblings'] = roll_dice('2d10')
        rank = int(ud['siblings']) // 3
        ud['birth_rank'] = str(rank)
        ud['social_class'] = '{}'.format(random.choice(social_class_list))
        ud['level'] = '1'
        ud['XP'] = '0'


    if user_race == 'Halfling':
        ud['first_name'] = '{}'.format(random.choice(halfling_first_names))
        ud['last_name'] = '{}'.format(random.choice(halfling_last_names))
        ud['clan'] = '{}'.format(random.choice(gnome_clans))
#        ud['Name'] = '{} {}, of the clan {}'.format(ud['first_name'], ud['last_name'], ud['clan'])
        ud['table_name'] = '{} {}'.format(ud['first_name'], ud['last_name'])
        ud['Alignment'] = random.choice(alignment1) + random.choice(alignment2)
#        ud['Age'] = int(random.normalvariate(25, 2))
        ud['age_base'] = roll_dice('3d4') + 20
        ud['age_max'] = roll_dice('1d100') + 100
        ud['age'] = '{}'.format(str(ud['age_base'])) + '({})'.format(str(ud['age_max']))
        ud['Height'] = roll_dice('2d4') + 32
        ud['Weight'] = 30 + roll_dice('1d1') * (ud['Height'] - 32)
        ud['height'] = str(ud['Height'])
        ud['weight'] = str(ud['Weight'])
        ud['dex'] + 1
        ud['str'] - 1
        ud['Languages'].append('Halfling')
        ud['Size'] = 2
        ud['Skin Tone'] = random.choice(halfling_skin_tones)
        ud['Hair Color'] = 'Black'
        ud['Hair Type'] = 'Straight'
        ud['Eye Color'] = random.choice(['Brown', 'Black'])
        ud['fam'] = '{}'.format(random.choice(halfling_last_names))
        ud['home'] = '{}'.format(random.choice(dwarf_home_land))
        ud['siblings'] = roll_dice('2d10')
        rank = int(ud['siblings']) // 3
        ud['birth_rank'] = str(rank)
        ud['social_class'] = '{}'.format(random.choice(social_class_list))
        ud['level'] = '1'
        ud['XP'] = '0'

    if user_race == 'Gnome':
        ud['first_name'] = '{}'.format(random.choice(gnome_first_names))
        ud['last_name'] = '{}'.format(random.choice(gnome_last_names))
        ud['clan'] = '{}'.format(random.choice(gnome_clans))
#        ud['Name'] = '{} {}, of the clan {}'.format(ud['first_name'], ud['last_name'], ud['clan'])
        ud['table_name'] = '{} {}'.format(ud['first_name'], ud['last_name'])
#        ud['Name'] = '{} "{}" {}, of the clan {}'.format(random.choice(gnome_first_names),
#                                                         random.choice(gnome_nick_names),
#                                                         random.choice(gnome_last_names), random.choice(gnome_clans))
        ud['Alignment'] = random.choice(alignment1) + random.choice(
            alignment2 + ['Good'])  # good is listed twice, since gnomes tend to be good.
#        ud['Age'] = int(random.normalvariate(140, 20))
#        ud['home'] = '{}'.format(random.choice(dwarf_home_land))
        ud['age_base'] = roll_dice('3d12') + 60
        ud['age_max'] = roll_dice('3d100') + 200
        ud['age'] = '{}'.format(str(ud['age_base'])) + '({})'.format(str(ud['age_max']))
        ud['Height'] = roll_dice('2d4') + 36
        ud['Weight'] = 40 + roll_dice('1d6') * (ud['Height'] - 36)
        ud['height'] = str(ud['Height'])
        ud['weight'] = str(ud['Weight'])
        ud['con'] + 1
        ud['str'] - 1
        ud['Languages'].append('Gnome')
        ud['Size'] = 2
        ud['Skin Tone'] = random.choice(['Deep Tan', 'Woody Brown'])
        ud['Hair Color'] = random.choice(['Blonde', 'White', 'Grey'])
        ud['Hair Type'] = random.choice(['Curly', 'Wavy', 'Straight'])
        ud['Eye Color'] = random.choice(gnome_eye_colors)
        ud['fam'] = '{}'.format(random.choice(gnome_last_names))
        ud['home'] = '{}'.format(random.choice(dwarf_home_land))
        ud['siblings'] = roll_dice('2d10')
        rank = int(ud['siblings']) // 3
        ud['birth_rank'] = str(rank)
        ud['social_class'] = '{}'.format(random.choice(social_class_list))
        ud['level'] = '1'
        ud['XP'] = '0'

    if user_race == 'Half-Elf':
        ud['first_name'] = '{}'.format(random.choice(elf_first_names))
        ud['last_name'] = '{}'.format(random.choice(human_last_names))
        ud['clan'] = '{}'.format(random.choice(human_tribes))
        ud['table_name'] = '{} {}'.format(ud['first_name'], ud['last_name'])

        ud['Tribe'] = ud['clan']
        #ud['Name'] = '{} {}'.format(random.choice(list(human_first_names[ud['Tribe']]) + list(elf_first_names)),
        #                            random.choice(list(human_first_names[ud['Tribe']]) + list(elf_last_names)))
        #if random.random() > 0.5:
        #    ud['Name'] += ' of the clan ' + ud['Tribe']
#        ud['Name'] = '{} {}, of the clan {}'.format(ud['first_name'], ud['last_name'], ud['clan'])
#        ud['Age'] = int(random.normalvariate(80, 20))
        ud['age_base'] = roll_dice('1d6') + 15
        ud['age_max'] = roll_dice('3d20') + 125
        ud['age'] = '{}'.format(str(ud['age_base'])) + '({})'.format(str(ud['age_max']))
        ud['Height'] = roll_dice('2d8') + 55
        ud['Weight'] = 100 + roll_dice('2d4') * (ud['Height'] - 55)
        ud['height'] = str(ud['Height'])
        ud['weight'] = str(ud['Weight'])
        ud['Languages'].append('Elven')
        ud['Size'] = 1
        ud['Skin Tone'] = random.choice(half_elf_skin_tones)
        ud['Hair Color'] = random.choice(half_elf_hair_colors)
        ud['Hair Type'] = random.choice(half_elf_hair_types)
        ud['Eye Color'] = random.choice(half_elf_eye_colors)
        ud['home'] = '{}'.format(random.choice(elven_home_land))
        ud['fam'] = '{}'.format(random.choice(human_last_names))
        ud['siblings'] = roll_dice('2d10')
        rank = int(ud['siblings']) // 3
        ud['birth_rank'] = str(rank)
        ud['social_class'] = '{}'.format(random.choice(social_class_list))
        ud['level'] = '1'
        ud['XP'] = '0'


    if user_race == 'Human':
        ud['first_name'] = '{}'.format(random.choice(elf_first_names))
        ud['last_name'] = '{}'.format(random.choice(human_last_names))
        ud['clan'] = '{}'.format(random.choice(human_tribes))
        ud['table_name'] = '{} {}'.format(ud['first_name'], ud['last_name'])
        ud['Tribe'] = ud['clan']
#        ud['Tribe'] = random.choice(human_tribes)
#        ud['Age'] = int(random.normalvariate(25, 4))
        ud['Height'] = roll_dice('2d4') + 58
        ud['Weight'] = 120 + roll_dice('2d6') * (ud['Height'] - 58)
        ud['height'] = str(ud['Height'])
        ud['weight'] = str(ud['Weight'])
#        ud['Name'] = '{} {} of the clan {}'.format(random.choice(list(human_first_names[ud['Tribe']])),
#                                                   random.choice(list(human_last_names[ud['Tribe']])), ud['Tribe'])
#        ud['Name'] = '{} {}, of the clan {}'.format(ud['first_name'], ud['last_name'], ud['clan'])
        ud['home'] = 'Realm of Forever'
        ud['age_base'] = roll_dice('1d4') + 15
        ud['age_max'] = roll_dice('2d20') + 90
        ud['age'] = '{}'.format(str(ud['age_base'])) + '({})'.format(str(ud['age_max']))
        ud['Size'] = 1
        ud['Skin Tone'] = random.choice(human_skin_tones)
        ud['Hair Color'] = random.choice(human_hair_colors)
        ud['Hair Type'] = random.choice(human_hair_types)
        ud['Eye Color'] = random.choice(human_eye_colors)
        ud['fam'] = '{}'.format(random.choice(human_last_names))
        ud['siblings'] = roll_dice('2d10')
        rank = int(ud['siblings']) // 3
        ud['birth_rank'] = str(rank)
        ud['social_class'] = '{}'.format(random.choice(social_class_list))
        ud['level'] = '1'
        ud['XP'] = '0'
        ud['Languages'].append('Native Language')

    def validate_race_to_class(race):
        classes_temp_dict = class_list

        for class_validation_item in classes_temp_dict:
            valid_class_counter = 0

            permits_list = classes_temp_dict[class_validation_item]['permit']
            del classes_temp_dict[class_validation_item]['permit']

            for class_att in classes_temp_dict[class_validation_item]:
                if rolled_stats[class_att] >= classes_temp_dict[class_validation_item][class_att]:
                    valid_class_counter += 1
            if valid_class_counter == 6 and (race in permits_list or 'all' in permits_list):


                if 'Cleric' in class_validation_item:
                    print(class_list2['Cleric']['desc'])
                if 'Thief' in class_validation_item:
                    print(class_list2['Thief']['desc'])
                if 'Ranger' in class_validation_item:
                    print(class_list2['Ranger']['desc'])
                if 'Paladin' in class_validation_item:
                    print(class_list2['Paladin']['desc'])
                if 'Fighter' in class_validation_item:
                    print(class_list2['Fighter']['desc'])
                if 'Mage' in class_validation_item:
                    print(class_list2['Mage']['desc'])
                if 'Druid' in class_validation_item:
                    print(class_list2['Druid']['desc'])
                if 'Bard' in class_validation_item:
                    print(class_list2['Bard']['desc'])
                if 'Wizard' in class_validation_item:
                    print(class_list2['Wizard']['desc'])

    validate_race_to_class(user_input.lower())

    print('\nYour stats and race allow you to be any of the above:\n')

    input_class = input('\nChoose your class:\n')
    user_class =  input_class
    skill_points = class_xp[user_class] + int_stat
    ud['Health'] = class_health[user_class] + con_stat

    if user_class == 'Barbarian':
        ud['Weapon'] = random.choice(melee_weapons)
        ud['Shield'] = random.choice(shields)
        ud['Armor'] = random.choice(barbarian_armor)
        ud['Alignment'] = random.choice(alignment1[0:2]) + random.choice(alignment2)
        ud['Religion'] = random.choice(['Kord', 'Obad Hai', 'Erythnul'] + religions)
        ud['Gold'] = roll_dice('4d4') * 10

    if user_class == 'Bard':
        ud['Weapon'] = random.choice(bard_weapons)
        ud['Shield'] = random.choice(list(armor_data.keys())[12:16])
        ud['Armor'] = random.choice(list(armor_data.keys()))
        ud['Alignment'] = random.choice(alignment1[1:3]) + random.choice(alignment2)
        if 'Chaotic' in ud['Alignment']:
            ud['Religion'] = 'Olidammara'
        elif random.random() > 0.5:
            ud['Religion'] = random.choice(['Pelor', 'Corellon Larethian'])
        ud['Gold'] = roll_dice('4d4') * 10

    if user_class == 'Cleric':
        ud['Religion'] = random.choice(
            religions)
        x = religion_alignments[ud['Religion']]
        if x % 3 != 0 and (x + 1) < 10 and random.random() > 0.5:
            x += 1
        elif (x + 3) < 10 and random.random() > 0.5:
            x += 3
        else:
            if x % 3 != 0 and (x - 1) > 0 and random.random() > 0.5:
                x -= 1
            elif (x - 3) > 0 and random.random() > 0.5:
                x -= 3
        ud['Alignment'] = religion_table[x]
        ud['Weapon'] = religion_weapons[ud['Religion']]
        ud['Armor'] = random.choice(cleric_armor)
        ud['Shield'] = random.choice(shields)
        add_list('Domains', religion_domains[ud['Religion']], 2)
        ud['Languages'].append(random.choice(['Celestial', 'Abyssal', 'Infernal']))
        if 'War' in ud['Domains']:
            ud['Feats'].append('Weapon Focus')
        ud['Gold'] = roll_dice('5d4') * 10

    if user_class == 'Druid':
        if random.random() > 0.5:
            ud['Shield'] = 'Light Wooden'
            ud['Weapon'] = 'Unarmed'
        else:
            ud['Shield'] = 'Heavy Wooden'
            ud['Weapon'] = random.choice(druid_weapons)
        ud['Armor'] = random.choice(['Padded', 'Leather', 'Hide'])
        ud['Religion'] = random.choice(religions)
        ud['Alignment'] = religion_table[int(random.choice('24568'))]
        ud['Languages'].append('Druidic')
        ud['Languages'].append('Sylvan')
        ud['Animal Companion'] = random.choice(druid_companions)
        ud['Gold'] = roll_dice('2d4') * 10

    if user_class == 'Fighter':
        ud['Weapon'] = random.choice(list(weapon_data.keys()))
        ud['Shield'] = random.choice(shields)
        ud['Armor'] = random.choice(armor)
        ud['Religion'] = random.choice(fighter_religions)
        ud['Gold'] = roll_dice('6d4') * 10
        add_list('Feats', feat_list)
        ud['hitpoints'] = random.randint(1, 10)

    if user_class == 'Paladin':
        ud['Armor'] = random.choice(armor)
        ud['Shield'] = random.choice(shields)
        ud['Weapon'] = random.choice(list(weapon_data.keys()))
        ud['Alignment'] = 'Lawful Good'
        ud['Religion'] = random.choice(['Heironeous', 'Pelor'] + religions)
        ud['Gold'] = roll_dice('6d4') * 10

    if user_class == 'Ranger':
        ud['Armor'] = armor[random.randint(0, 3)]
        ud['Shield'] = shields[random.randint(0, 3)]
        ud['Weapon'] = random.choice(ranged_weapons)
        ud['Favored Enemy'] = random.choice(ranger_favored_enemies)
        ud['Feats'].append('Track')
        ud['Religion'] = random.choice(['Ehlonna', 'Obad Hai'] + religions)
        ud['Gold'] = roll_dice('6d4') * 10

    if user_class == 'Rogue':
        ud['Armor'] = armor[random.randint(0, 3)]
        ud['Weapon'] = random.choice(rogue_weapons)
        ud['Religion'] = random.choice(religions)
        ud['Gold'] = roll_dice('5d4') * 10

    if user_class == 'Wizard':
        ud['Weapon'] = random.choice(wizard_weapons)
        ud['Feats'].append('Scribe Scroll')
        if random.random() > 0.8:
            ud['Feats'].append('Spell Mastery')
        ud['Religion'] = random.choice(['Nerull', 'Boccob'] + religions)
        ud['Familiar'] = random.choice(familiars)
        if ud['Familiar'] == 'Toad':
            ud['Health'] = 7 + pb('con')
        if random.random() > 0.7:
            ud['Languages'].pop()
            ud['Languages'].append('Draconic')
        ud['School'] = random.choice(list(wizard_schools.keys()))
        add_list('Forbidden Schools', list(wizard_schools.keys()), wizard_schools[ud['School']])
        ud['Gold'] = roll_dice('3d4') * 10

    if pb('int') > 1:
        add_list('Languages', generic_language_list)

    ud.setdefault('ac', 10 + armor_data[ud['Armor']]['Armor Bonus'] + armor_data[ud['Shield']]['Armor Bonus'])

    if skill_points < 1:
        skill_points = 1
    if user_race == 'Human':
        skill_points += 1
    if skill_points > len(skill_list[user_class]):
        skill_points = len(skill_list[input_class]) - 1
    if ud['str'] > 12 and random.random() > 0.4 and skill_points > 0:
        ud['Skills'].append('Power Attack')
        skill_points -= 1
    if ud['dex'] > 12 and random.random() > 0.3 and skill_points > 0:
        ud['Skills'].append('Dodge')
        skill_points -= 1
    if ud['int'] > 12 and random.random() > 0.4 and skill_points > 0:
        ud['Skills'].append('Combat Experience')
        skill_points -= 1
    if ud['dex'] > 14 and random.random() > 0.2 and skill_points > 0:
        ud['Skills'].append('Two Weapon Fighting')
        skill_points -= 1
    if weapon_data[ud['Weapon']]['Handed'] != 1:
        ud['Shield'] = 'None'

    add_list('Skills', skill_list[user_class], skill_points)
    add_list('Feats', feat_list)

    if ud['Alignment'] == 'Neutral Neutral':
        ud['Alignment'] = 'True Neutral'

    ud['af'] = armor_data[ud['Armor']]['Arcane Spell Failure']

    ud['player_name'] = player_name
    ud['gender'] = gender
    ud['race'] = user_race
    ud['class'] = user_class
    rope = 'rope (hemp; {} ft.), '.format(random.randint(1, 50))
    sack = 'sack (empty; {}), '.format(random.randint(1, 5))
    string = 'string ({} ft.), '.format(random.randint(1, 50))
    rations = 'rations ({} days), '.format(random.randint(2, 7))
    torches = 'torches ({})'.format(random.randint(1, 5))


    if ud['gender'] == 'Male':
        ud['data1'] = '{} is a {}{} {} {}'.format(ud['table_name'], random.choice(char_who), ud['race'], ud['class'],
                                                  random.choice(char_from))
        ud['data2'] = '{} and {}'.format(random.choice(male_char_issues), random.choice(male_char_issues))
    elif ud['gender'] == 'Female':
        ud['data1'] = '{} is a {}{} {} {}'.format(ud['table_name'], random.choice(char_who), ud['race'], ud['class'],
                                                  random.choice(char_from))
        ud['data2'] = '{} and {}'.format(random.choice(fem_char_issues), random.choice(fem_char_issues))

    os.system('clear')
    ################################################################################################################
    ################################################################################################################
    ################################################################################################################
    gen_info = PrettyTable()
    gen_info.field_names = ["################################", "###############################",
                            "##############################"]
    gen_info.align["################################"] = "l"
    gen_info.align["###############################"] = "l"
    gen_info.align["##############################"] = "l"
    gen_info.add_row(['Character Name: ' + ud['table_name'], " ", " "])
    gen_info.add_row(['Alignment: ' + ud['Alignment'], 'Race: ' + ud['race'], 'Class: ' + ud['class']])
    gen_info.add_row(["Player Name: " + 'None', 'Family: ' + ud['fam'], 'Clan: ' + ud['clan']])
    gen_info.add_row(['Homeland: ' + ud['home'], "Leige/Patron: ____________", 'Religion: ' + ud['Religion']])
    gen_info.add_row(['Sex: ' + ud['gender'], 'Age:(Max): ' + ud['age'], 'Social Class: ' + ud['social_class']])
    gen_info.add_row(['Height: ' + ud['height'] + '"', 'Weight: ' + ud['weight'] + ' lbs.',
                      '# Siblings: ' + str(ud['siblings'])])
    gen_info.add_row(['==============','==============','Birth Rank: ' + ud['birth_rank']])
    gen_info.add_row(['Hair: ' + ud['Hair Color'], 'Eyes: ' + ud['Eye Color'], "Skin Tone: " + ud['Skin Tone']])
    gen_info.add_row(["==============", "==============", "=============="])
    gen_info.add_row(['Level: ' + ud['level'], 'Exp: ' + ud['XP'], 'Gold: {} gp'.format(ud['Gold'])])
    gen_info.add_row(["==============", "==============", "=============="])
    gen_info.add_row(
        ["################################", "###############################", "##############################"])
    print(gen_info)

    ################################################################################################################
    ################################################################################################################
    ################################################################################################################
    race_info = PrettyTable()
    race_info.field_names = [
        "A quick description outlining your " + ud['race'] + " Character                                     "]
    race_info.align[
        "A quick description outlining your " + ud['race'] + " Character                                     "] = "l"
    race_info.add_row(
        ["###################################################################################################"])
    race_info.add_row([ud['data1']])
    race_info.add_row([ud['data2']])
    race_info.add_row(
        ["###################################################################################################"])
    print(race_info)
    ################################################################################################################
    ################################################################################################################
    ################################################################################################################
    print("#" * 103)
    print(' ' * 45 + 'ABILITIES')



    str_mod = PrettyTable()
    str_mod.field_names = ["  Strength  ", " Hit Prob ", " Damage Adj  ", " Weight Allow ",
                           " Max Press ", " Open Doors ", " BB / LG "]
    str_mod.add_row([strength_stats[str_stat_adj]['Str'],
                     strength_stats[str_stat_adj]['Hit Prob'],
                     strength_stats[str_stat_adj]['Dam Adj'],
                     strength_stats[str_stat_adj]['Wt Allow'],
                     strength_stats[str_stat_adj]['Max Press'],
                     strength_stats[str_stat_adj]['Open Doors'],
                     strength_stats[str_stat_adj]['BB LG']])
    print(str_mod)

    ################################################################################################################
    ################################################################################################################
    ################################################################################################################

    dex_mod = PrettyTable()
    dex_mod.field_names = [" Dexterity  ", "       Reaction Adj       ",
                           "     Missle Attack Adj      ", "       Defense Adj      "]
    dex_mod.add_row([dexterity_stats[dex_stat_adj]['Dex'],
                     dexterity_stats[dex_stat_adj]['Reaction Adj'],
                     dexterity_stats[dex_stat_adj]['Missle Attack Adj'],
                     dexterity_stats[dex_stat_adj]['Defense Adj']])

    print(dex_mod)
    ################################################################################################################
    ################################################################################################################
    ################################################################################################################

    con_mod = PrettyTable()
    con_mod.field_names = ["Constitution", " HP Adj  ", " System Shock ", "  Resurrection Survival   ",
                           "Poison Save",
                           "Regeneration"]
    con_mod.add_row([constitution_stats[con_stat_adj]['Con'],
                     constitution_stats[con_stat_adj]['HP Adj'],
                     constitution_stats[con_stat_adj]['System Shock'],
                     constitution_stats[con_stat_adj]['Resurrection Survival'],
                     constitution_stats[con_stat_adj]['Poison Save'],
                     constitution_stats[con_stat_adj]['Regeneration']])
    print(con_mod)
    ################################################################################################################
    ################################################################################################################
    ################################################################################################################

    int_mod = PrettyTable()
    int_mod.field_names = ['Intelligence', '  Languages ', ' Spell Level ', ' Learn Spells ',
                           'Max Spells/Level', 'Illusion Immunity']
    int_mod.add_row([intelligence_stats[int_stat_adj]['Int'],
                     intelligence_stats[int_stat_adj]['Languages'],
                     intelligence_stats[int_stat_adj]['Spell Level'],
                     intelligence_stats[int_stat_adj]['Learn Spells'],
                     intelligence_stats[int_stat_adj]['Max Spells/Level'],
                     intelligence_stats[int_stat_adj]['Illusion Immunity']])
    print(int_mod)
    ################################################################################################################
    ################################################################################################################
    ################################################################################################################

    wis_mod = PrettyTable()
    wis_mod.field_names = ["   Wisdom   ", "   Magical Defense Adj   ", "   Bonus Spells   ", " Spell Failure ",
                           " Spell Immunity  "]
    wis_mod.add_row([wisdom_stats[wis_stat_adj]['Wis'],
                     wisdom_stats[wis_stat_adj]['Magical Defense Adj'],
                     wisdom_stats[wis_stat_adj]['Bonus Spells'],
                     wisdom_stats[wis_stat_adj]['Spell Failure'],
                     wisdom_stats[wis_stat_adj]['Spell Immunity']
                     ])
    print(wis_mod)
    ################################################################################################################
    ################################################################################################################
    ################################################################################################################

    cha_mod = PrettyTable()
    cha_mod.field_names = ["  Charisma  ", "       Max Henchmen       ", "       Loyalty Base       ",
                           "       Reaction Adj       "]
    cha_mod.add_row([charisma_stats[cha_stat_adj]['Cha'],
                     charisma_stats[cha_stat_adj]['Max Henchmen'],
                     charisma_stats[cha_stat_adj]['Loyalty Base'],
                     charisma_stats[cha_stat_adj]['Reaction Adj']
                     ])
    print(cha_mod)


    print('Items: Backpack (common), bedroll, flint & steel,\n       ' + rope + sack + string + rations + torches + '\n')
    if user_race is 'Dwarf':
        language_list = dwarven_language_list
    elif user_race is 'Elf':
        language_list = elven_language_list
    elif user_race is 'Half-Elf':
        language_list = half_elf_language_list
    elif user_race is 'Halfling':
        language_list = halfling_language_list
    elif user_race is 'Human':
        language_list = human_language_list
    elif user_race is 'Gnome':
        language_list = gnome_language_list
    else:
        language_list = generic_language_list

    num_lang = intelligence_stats[int_stat_adj]['Languages']
    for lang in range(num_lang - 2):
        random_lang = random.choice(language_list)
        language_list.remove(random_lang)
        ud['Languages'].append(random_lang)

    print('Languages: {}'.format(list_to_string(ud['Languages'])))
    print('Feat(s): {} \n'.format(list_to_string(ud['Feats'])))

    print('School: '
          '{}\nForbidden Schools: '
          '{}\nFamiliar: '
          '{}\n\n'.format(ud['School'],
                          list_to_string(ud['Forbidden Schools']),
                          ud['Familiar']) * int(user_class == 'Wizard'),
          end='')

    print(
        'Familiar: ''{}\n\n'.format(ud['Familiar']) * (int(user_class == 'wizard' or user_class == 'Sorcerer')), end='')

    print('Domains: {}\n\n'.format(list_to_string(ud['Domains'])) * int(user_class == 'Cleric'), end='')
    print('Weapon: {} ({} Handed | Damage: {}, {} | Critical Multiplier: {}x)'.format(ud['Weapon'],
                                                                                      weapon_data[ud['Weapon']][
                                                                                          'Handed'],
                                                                                      weapon_data[ud['Weapon']][
                                                                                          'Damage (M)'],
                                                                                      weapon_data[ud['Weapon']]['Type'],
                                                                                      weapon_data[ud['Weapon']][
                                                                                          'Critical']))

    print('Armor: {}'.format(ud['Armor']))
    print('Shield: {}'.format(ud['Shield']))
    print('Armor Class: {}\nArcane Spell Failure Chance: {}%'.format(ud['ac'], ud['af']))
    print('THAC0: (20)')
    ud['hp'] = ud['hitpoints'] + int(constitution_stats[con_stat_adj]['HP Adj'])
    print('Hit Points: ' + str(ud['hp']))


if __name__ == '__main__':

    get_race_stats()

