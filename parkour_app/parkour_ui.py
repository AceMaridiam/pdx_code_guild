from parkour_modules import catalog
import random
import types


# Allows user to choose level
user_level = raw_input("Beginner (B) | Intermediate (I) | Advanced (A)\n"
                       "*****  What is your level?  ******\n"
                       ">>  ").lower()

# assigns number value to user_level
if user_level == "beginner":
    user_level = 1
elif user_level == "intermediate":
    user_level = 2
elif user_level == "advanced":
    user_level = 3

# stores list of moves from chosen level
level_moves_list = []

# store list of move names from level_moves_list
level_moves_names = []

def get_level_moves_types(level_moves_list, move_type):
    level_move_types = []
    for level_move in level_moves_list:
        if level_move["move_type"] == move_type:
            level_move_types.append(level_move)

    return level_move_types

# loops through catalog to find moves based off user_level
for move in catalog.itervalues():
    if move['level'] == user_level:
        level_moves_list.append(move)

for move_option in level_moves_list:
    level_moves_names.append(move_option['name'])

# takes in users obstacles
user_input = raw_input("Create a list of obstacles.\n"
                       "AKA:Vault, Rail, Platform, Jump, Wall\n"
                       ">>  ").lower().split(', ')

#
generated_run = []
for input in user_input:
    moves_by_type = get_level_moves_types(level_moves_list, input)
    random_move_name = random.choice(moves_by_type)['name']
    generated_run.append("{} the {}".format(random_move_name, input))

print ', '.join(generated_run)





