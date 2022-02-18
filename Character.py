# Friday 18. Feb 2022
# Day 1 first game project

# Ok, first try on something I don't really know what gonna be. I have some ideas, to make
# something really basic, in form of turnbased RPG. This means, a whole bunch of random
# number generators (HP, Attack, Defense stats vs same opposing stats etc). 
# First I think I just have to try make a lvl 1 character, with it's base stats. When the lvl 
# 1 char have reached the experience points treshold for reaching lvl 2, it should levl up, then
# based on rng within a range, should get more HP, Attack, Defense. More stats would be nice, 
# but have to start "easy".

import random

job_alternatives = ["Warrior", "White Mage", "Paladin"]

#main_job = random.choice(job_alternatives)
main_character = input("Hello traveler. Tell me your name: ")

# Choose a job
print(*job_alternatives, sep = ", ")
job_chosen = input("Which job do you want to have? (WAR, WHM, PLD): ")

if job_chosen.upper() == "WAR":
    main_job = "Warrior"
elif job_chosen.upper() == "WHM":
    main_job = "White Mage"
elif job_chosen.upper() == "PLD":
    main_job = "Paladin"

# Multipliers for different jobs. This will be added to the characters base stats. 
def job_multiplier_hp(main_job):
    multiplier = 0
    if main_job == "Warrior":
        multiplier = 2
    elif main_job == "White Mage":
        multiplier = 1
    elif main_job == "Paladin":
        multiplier = 3
    return multiplier

def job_multiplier_mp(main_job):
    multiplier = 0
    if main_job == "Warrior":
        multiplier = 0
    elif main_job == "White Mage":
        multiplier = 5
    elif main_job == "Paladin":
        multiplier = 2
    return multiplier

def job_multiplier_atk(main_job):
    multiplier = 0
    if main_job == "Warrior":
        multiplier = 5
    elif main_job == "White Mage":
        multiplier = 1
    elif main_job == "Paladin":
        multiplier = 2
    return multiplier

def job_multiplier_def(main_job):
    multiplier = 0
    if main_job == "Warrior":
        multiplier = 2
    elif main_job == "White Mage":
        multiplier = 1
    elif main_job == "Paladin":
        multiplier = 5
    return multiplier

def job_multiplier_mpow(main_job):
    multiplier = 0
    if main_job == "Warrior":
        multiplier = 0
    elif main_job == "White Mage":
        multiplier = 5
    elif main_job == "Paladin":
        multiplier = 2
    return multiplier


#print(job_multiplier_def("Warrior"))
#print(job_multiplier_def("White Mage"))
#print(job_multiplier_def("Paladin"))

# Base stats. 
main_char_lvl = 1
main_stat_hp = random.choice(range(100, 110)) * job_multiplier_hp(main_job)
main_stat_mp = random.choice(range(40, 50)) * job_multiplier_mp(main_job)
main_stat_atk = random.choice(range(1, 5)) * job_multiplier_atk(main_job)
main_stat_def = random.choice(range(1, 5)) * job_multiplier_def(main_job)
main_stat_mpow = random.choice(range(1, 5)) * job_multiplier_mpow(main_job)


# Introduction
print("\n")
print("""\n\t
        Welcome, {name} the {job}!

        Your base stats will be as following:
        Level: {level}
        HP: {hp}
        MP: {mp}
        Atk: {atk}
        Def: {deff}
        M.Pow: {mpow}
        \n
    """.format(name=main_character.title(), job=main_job, level=main_char_lvl, 
        hp=main_stat_hp, mp=main_stat_mp, atk=main_stat_atk, deff=main_stat_def,
        mpow=main_stat_mpow))
