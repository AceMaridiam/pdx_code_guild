__author__ = 'Paul Anderson'
__copyright__ = "Copyright 2015"
__version__ = "1.0"
__email__ = "andermation@gmail.com"
__status__ = "Production"

from parkour_db import catalog
from parkour_run_db import runs
import random



class ParkourMove(object):
    def __init__(self, name, level, move_type, take_off):
        self.name = name
        self.level = level
        self.move_type = move_type
        self.take_off = take_off



# gets move name based on move type from users chosen level
def get_level_moves_types(level_moves_list, move_type):
    level_move_types = []
    for level_move in level_moves_list:
        if level_move["move_type"] == move_type:
            level_move_types.append(level_move)

    return level_move_types

# saves users run to db
def save_run():
    user_save = raw_input("Would you like to save this run?  Yes or NO:  ").lower()
    if user_save == "yes" or "y":
        runs[user_name] = {'level': user_level, 'obstacles': user_obsticles_list, 'run': generated_run, 'location': []}
    else:
        main_menu()







