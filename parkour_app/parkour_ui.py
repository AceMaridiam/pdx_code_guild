from parkour_modules import catalog, get_level_moves_types, save_run
import parkour_modules
from parkour_run_db import runs
import random


# main menu for game
# def main_menu():
#     print "Welcome to the run generator for Parkour and Free Running."
#     user_name = raw_input("Enter a user name:  ")
#     user_level = raw_input("Beginner (B) | Intermediate (I) | Advanced (A)\n"
#                        "*****  What is your level?  ******\n"
#                        ">>  ").lower()
#
#     return user_name, user_level

user_name = raw_input("Enter a user name:  ")
user_level = raw_input("Beginner (B) | Intermediate (I) | Advanced (A)\n"
                       "*****  What is your level?  ******\n"
                       ">>  ").lower()


# assigns number value to user_level
if user_level == "beginner" or user_level == "b":
    user_level = 1
elif user_level == "intermediate" or user_level == "i":
    user_level = 2
elif user_level == "advanced" or user_level == "a":
    user_level = len(catalog)
else:
    print "That is not an option. Try again."
    user_level_input()

# stores list of moves from chosen level
level_moves_list = []

# store list of move names from level_moves_list
level_moves_names = []

# loops through catalog to find moves based off user_level
for move in catalog.itervalues():
    if move['level'] == user_level:
        level_moves_list.append(move)

for move_option in level_moves_list:
    level_moves_names.append(move_option['name'])

# takes in users obstacles
user_obsticles_list = raw_input("Create a list of obstacles.\n"
                       "AKA: Vault, Rail, Platform, Jump, Wall\n"
                       ">>  ").lower().split(', ')

#
generated_run = []
for input in user_obsticles_list:
    moves_by_type = get_level_moves_types(level_moves_list, input)
    random_move_name = random.choice(moves_by_type)['name']
    generated_run.append("{} the {}".format(random_move_name, input))

# def generated_run_output():
if len(user_obsticles_list) == 1:
    generated_run_output = "There is one move in your run.\n{}".format(', '.join(generated_run))
else:
    generated_run_output = "You have {} moves in your run\n{}".format(len(generated_run), ', '.join(generated_run))

# saves users run to db
def save_run():
    user_save = raw_input("Would you like to save this run?  Yes or NO:  ").lower()
    if user_save == "yes" or "y":
        runs[user_name] = {'level': user_level, 'obstacles': user_obsticles_list, 'run': generated_run, 'location': []}
    else:
        main_menu()


# prints number of moves in current level directory
print "list of moves: {}".format(len(level_moves_list))
# prints how many moves are in users list
print generated_run_output


save_run()
print "{}'s run data has been stored.".format(user_name)
print runs
