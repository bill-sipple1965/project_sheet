import random
from tools_data import *


input_class = ''
input_race = ''

#############
# Functions #
#############


def start_fn():
    menu = "MENU" \
        "\n1) (C)reate Character / NPC" \
        "\n2) (Q)uit\n"
    print(menu)
    option = input("Choose an option:\n")
    if option is ('Q', 'q','2'):
        quit()
    elif option is ('C', 'c', ''):
        if option in ("C", "c", "1"):

            print("")
            gender_fn()
            print("")
            abilities_fn()
            print("")
            name_fn()
            print("")
#            save_fn()
        else:
            start_fn()
def name_fn():
    global char_name
    global player_name
    global player_name
    char_name = ""
    player_name = ""
    while not player_name:
        player_name = input("Player's Name:? \n")
    while not char_name:
        char_name = input("Enter Character Name: ")

def gender_fn():
    global char_gender
    print("Available Genders Include:")
    print("  (R)andom")
    print("  (M)ale")
    print("  (F)emale")
    char_gender = input("Enter character gender [R]: \n")
    if char_gender in ("R", "r", "Random", "random", ""):
        char_gender = random.choice("MF")
    if char_gender in ("M", "m", "Male", "male"):
        char_gender = "Male"
    elif char_gender in ("F", "f", "Female", "female"):
        char_gender = "Female"
    else:
        print("Gender not available")
        gender_fn()


def abilities_fn():
    d6 = lambda: random.randint(1, 6)

    def roll_att():
        rollout = (d6(), d6(), d6(), d6())
        return sum(rollout) - min(rollout)

    def strength():
        global abl_str
        abl_str = int(input("Enter the score to use for Strength: "))
        if abl_str not in abl_scores:
            print("Score not valid")
            strength()
        else:
            abl_scores.remove(abl_str)

    def dexterity():
        print("Remaining Scores: ", abl_scores)
        global abl_dex
        abl_dex = int(input("Enter the score to use for Dexterity: "))
        if abl_dex not in abl_scores:
            print("Score not valid")
            dexterity()
        else:
            abl_scores.remove(abl_dex)

    def constitution():
        print("Remaining Scores: ", abl_scores)
        global abl_con
        abl_con = int(input("Enter the score to use for Constitution: "))
        if abl_con not in abl_scores:
            print("Score not valid")
            constitution()
        else:
            abl_scores.remove(abl_con)

    def intelligence():
        print("Remaining Scores: ", abl_scores)
        global abl_int
        abl_int = int(input("Enter the score to use for Intelligence: "))
        if abl_int not in abl_scores:
            print("Score not valid")
            intelligence()
        else:
            abl_scores.remove(abl_int)

    def wisdom():
        print("Remaining Scores: ", abl_scores)
        global abl_wis
        abl_wis = int(input("Enter the score to use for Wisdom: "))
        if abl_wis not in abl_scores:
            print("Score not valid")
            wisdom()
        else:
            abl_scores.remove(abl_wis)

    def charisma():
        print("Remaining Scores: ", abl_scores)
        global abl_cha
        abl_cha = int(input("Enter the score to use for Charisma: "))
        if abl_cha not in abl_scores:
            print("Score not valid")
            charisma()
        else:
            abl_scores.remove(abl_cha)

    def assign():
        rnd_assign = input("\nDo you want to randomly assign stat rolls? [Y]: \n")
        if rnd_assign in ("Y", "y", "Yes", "yes", ""):
            random.shuffle(abl_scores)
            global abl_str
            global abl_dex
            global abl_int
            global abl_con
            global abl_wis
            global abl_cha
            abl_str = random.choice(abl_scores)
            abl_scores.remove(abl_str)
            abl_dex = random.choice(abl_scores)
            abl_scores.remove(abl_dex)
            abl_con = random.choice(abl_scores)
            abl_scores.remove(abl_con)
            abl_int = random.choice(abl_scores)
            abl_scores.remove(abl_int)
            abl_wis = random.choice(abl_scores)
            abl_scores.remove(abl_wis)
            abl_cha = random.choice(abl_scores)
        elif rnd_assign in ("N", "n", "No", "no"):
            strength()
            dexterity()
            constitution()
            intelligence()
            wisdom()
            charisma()
        else:
            print("Invalid choice")
            assign()
    print("Rolling random ability scores...\n")
    score1 = roll_att()
    score2 = roll_att()
    score3 = roll_att()
    score4 = roll_att()
    score5 = roll_att()
    score6 = roll_att()
    abl_scores = [score1, score2, score3, score4, score5, score6]
    print("  Your Rolled Scores Are: ", abl_scores)
    reroll = input("  Do you want to (C)ontinue or (R)eroll? [C]: \n")
    if reroll in ("C", "c", "Continue", "continue", ""):
        assign()
        print("The Scores You Assigned Were:")
        print("   Strength:     ", abl_str)
        print("   Dexterity:    ", abl_dex)
        print("   Constitution: ", abl_con)
        print("   Intelligence: ", abl_int)
        print("   Wisdom:       ", abl_wis)
        print("   Charisma:     ", abl_cha)
        choice = input("Do you want to (C)ontinue, Re(A)ssign, or (R)eroll? [C]: \n")
        if choice in ("R", "r", "Reroll", "reroll"):
            abilities_fn()
        elif choice in ("A", "a", "Reassign", "reassign", "ReAssign"):
            assign()
        else:
            pass
    else:
        abilities_fn()


    global rolled_stats
    rolled_stats = {'str': abl_str, 'dex': abl_dex, 'con': abl_con, 'int': abl_int, 'wis': abl_wis, 'cha': abl_cha }
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

    print("\nYour rolled ability scores allow your character to be any of the following:\n")  # Output a valid race
    for char_race in valid_race_list:
        print("  ", '{}{}'.format(char_race, race_desc[char_race]))


def race_fn():
    global char_race
    print("  (R)andom")
    char_race = input("\nEnter Your Race (effects age, height, weight) [R]:\n ")
    if char_race in valid_race_list:
        pass
    elif char_race in ("R", "r", "Random", "random", ""):
        char_race = (random.choice(valid_race_list))
    else:
        print("Race not available")
        race_fn()





##########
# Script #
##########

start_fn()
name_fn()
gender_fn()
abilities_fn()
race_fn()
