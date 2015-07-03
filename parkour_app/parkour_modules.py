__author__ = 'Paul Anderson'
__copyright__ = "Copyright 2015"
__version__ = "1.0"
__email__ = "andermation@gmail.com"
__status__ = "Production"

from parkour_run_db import runs
from parkour_db import catalog
import webbrowser
import time


class ParkourMove(object):
    def __init__(self, name, level, move_type, take_off):
        self.name = name
        self.level = level
        self.move_type = move_type
        self.take_off = take_off


#main menu for game
def main_menu():
    user_choice = int(raw_input("Welcome to the run generator for Parkour and Free Running.\n\n"
                                "\tTo start a run, type: 1\n\n"
                                "\tWhat Parkour? and what is the difference between \n\tParkour and Free Running? \n\n\tto get learned! type: 2 >  "))

    if user_choice == 1:
        pass
    elif user_choice == 2:
        print "\nMany people mistakenly think that Parkour and Free Running are the same thing. \n" \
              "Parkour is an individual sport; by training Parkour you aim to gain a mind-body connection which you have never previously experienced. \n" \
              "Free Running is the art of movement; adding personality and expression into what you do."
        time.sleep(1)
        answer = raw_input("Do you want to know more? (Y/N): ".lower())
        if answer == 'yes' or answer == 'y':
            print "You're browser is opening"
            time.sleep(3)
            webbrowser.open('http://iontams.com/2012/03/13/parkour-vs-free-running/')
            time.sleep(3)
            main_menu()
        elif answer == 'no' or answer == 'n':
            pass
        else:
            print "Not a valid answer!"
        pass



# gets move name based on move type from users chosen level
def get_level_moves_types(level_moves_list, move_type):
    level_move_types = []
    for level_move in level_moves_list:
        if level_move["move_type"] == move_type:
            level_move_types.append(level_move)

    return level_move_types


def user_obsticles_list_checker():
    user_obsticles_list = raw_input("Create a list of obstacles, seperated by comma.\n"
                                "Obstacles: Vault, Bar, Wall, Ground\n"
                                ">>  ").lower().split(', ')
    for item in user_obsticles_list:
        if item == "vault" or item == "bar" or item == "wall" or item == "ground":
            return user_obsticles_list
        else:
            print "Not a valid answer!"
            main_menu()


# Choose user level one
def get_moves_for_beginner_level():
    user_level_one = 1
    level_moves_list = []
    for move in catalog.itervalues():
        if move['level'] == user_level_one:
            level_moves_list.append(move)
    return level_moves_list

# Choose user level two and one
def get_moves_for_intermediate_level():
    user_level_one = 1
    user_level_two = 2
    level_moves_list = []
    for move in catalog.itervalues():
        if move['level'] == user_level_one:
            level_moves_list.append(move)
        elif move['level'] == user_level_two:
            level_moves_list.append(move)
    return level_moves_list

# Choose user level three, two, and one
def get_moves_for_advanced_level():
    user_level_one = 1
    user_level_two = 2
    user_level_three = 3
    level_moves_list = []
    for move in catalog.itervalues():
        if move['level'] == user_level_one:
            level_moves_list.append(move)
        elif move['level'] == user_level_two:
            level_moves_list.append(move)
        elif move['level'] == user_level_three:
            level_moves_list.append(move)
    return level_moves_list








