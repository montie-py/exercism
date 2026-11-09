"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

def find_sublist(biglist, target):
    target_str = ',' + ','.join(map(str, target)) + ','
    biglist_str = ',' + ','.join(map(str, biglist)) + ','
    return biglist_str.find(target_str)


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL

    if (not list_one) or (find_sublist(list_two, list_one) > -1):
        return SUBLIST

    if (not list_two) or (find_sublist(list_one, list_two) > -1):
        return SUPERLIST

    

    return UNEQUAL
        
