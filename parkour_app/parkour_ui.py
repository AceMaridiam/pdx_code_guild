from parkour_modules import get_level_moves_types, main_menu, get_moves_for_advanced_level, get_moves_for_beginner_level, get_moves_for_intermediate_level
from parkour_run_db import runs
from parkour_db import catalog
import random




# main_menu()

# def make_run():
user_name = raw_input("Enter a user name:  ")
user_level = raw_input("Beginner (B) | Intermediate (I) | Advanced (A)\n"
                       "*****  What is your level?  ******\n"
                       ">>  ").lower()



# level_moves_list is a list of moves (dictionaries)
if user_level == "beginner" or user_level == "b":
    level_moves_list = get_moves_for_beginner_level()
elif user_level == "intermediate" or user_level == "i":
    level_moves_list = get_moves_for_intermediate_level()
elif user_level == "advanced" or user_level == "a":
    level_moves_list = get_moves_for_advanced_level()
else:
    print "That is not an option. Try again."



# store list of move names from level_moves_list
level_moves_names = []
for move_option in level_moves_list:
    level_moves_names.append(move_option['name'])

# takes in users obstacles
user_obsticles_list = raw_input("Create a list of obstacles, seperated by comma.\n"
                                "Obstacles: Vault, Bar, Wall, Ground\n"
                                ">>  ").lower().split(', ')


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
        new_run = raw_input("Would you like to make a 'New Run' run, or 'Exit'?").lower()
        if new_run == "new run":
            main_menu()
        else:
            print "Until the Next Run, Train Hard!"
            exit()

# prints number of moves in current level directory
print "list of moves: {}".format(len(level_moves_list))
# prints how many moves are in users list
print generated_run_output


save_run()

################### code tests ###################


