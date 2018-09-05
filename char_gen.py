import random, os, re
from tools_data import *
# from name_info import player_name, gender


def roll_dice(roll):
    values = [int(x) for x in re.findall(r'\d+', roll)]
    drop = 0
    if 'D' in roll:
        drop = values[2]
    top_rolls = sorted(list(random.randint(1, values[1]) for _ in range(values[0])))
    return sum(top_rolls[drop:])


d6 = lambda: random.randint(1, 6)


def roll_att():
    rollout = (d6(), d6(), d6(), d6())
    return sum(rollout) - min(rollout)


def rollout_attributes():
    return {
        'str': roll_att(),
        'dex': roll_att(),
        'con': roll_att(),
        'int': roll_att(),
        'wis': roll_att(),
        'cha': roll_att()
    }


def attributes_are_valid(attributes):
    over_fifteen = filter(lambda attr: attr >= 15, attributes.values())
    return len(list(over_fifteen)) >= 2


def main():
    attributes = rollout_attributes()
    while not attributes_are_valid(attributes):
        attributes = rollout_attributes()

    rolled_stats = rollout_attributes()
    global valid_race_list
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

    os.system('clear')

    # This is the formula for Ability Modifiers.
    # str_mod = (Strength - 10) // 2
    # dex_mod = (Dexterity - 10) // 2
    # con_mod = (Constitution - 10) // 2
    # int_mod = (Intelligence - 10) // 2
    # wis_mod = (Wisdom - 10) // 2
    # cha_mod = (Charisma - 10) // 2
    # ArmorClass = Dexterity + 10
    # ProficiencyBonus = str("+2")
    # PassivePerception = 10 + wis_mod
    # AC = dex_mod + 10

    modifiers = {}
    for attribute, value in attributes.items():
        modifiers[attribute + '_mod'] = (value - 10) // 2

    rolled_stats.update(modifiers)
    print('\nScores with Modifiers:\n')
    print('''\
    str: {str} ({str_mod:+d})
    dex: {dex} ({dex_mod:+d})
    con: {con} ({con_mod:+d})
    int: {int} ({int_mod:+d})
    wis: {wis} ({wis_mod:+d})
    cha: {cha} ({cha_mod:+d})\
        '''.format(**rolled_stats))

    reroll = input("\n  Do you want to (C)ontinue or (R)eroll? [C]: \n")
    if reroll in ("R", "r", "Reroll", "reroll"):
        os.system('clear')
        main()
    else:
        races()


def races():
    print("Your rolled ability scores allow your character to be any of the following:\n")  # Output a valid race
    for char_race in valid_race_list:
        print("  ", '{} {}'.format(char_race, race_desc[char_race]))

    user_race = input('\n  Choose a Race from the list above:\n')
    if user_race in valid_race_list:
        chosen_race = '{}_race()'.format(user_race.lower()) ## lowercase to use for function calls
        eval(chosen_race) ## move to the chosen race function
    else:
        os.system('clear')
        print('oops')
        races()


def dwarf_race():
    print('Dwarf Race Function = Delete this notice after testing')


def elf_race():
    print('Elf Race Function = Delete this notice after testing')


def half_elf_race():
    print('Half Elf Race Function = Delete this notice after testing')


def halfling_race():
    print('Halfling Race Function = Delete this notice after testing')


def gnome_race():
    print('Gnome Race Function = Delete this notice after testing')


def human_race():
    print('Human Race Function = Delete this notice after testing')


def classes():
    print('Classes Function')


if __name__ == '__main__':
    main()


