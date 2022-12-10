#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary)i):
    list_ord = list(a_dictionary.keys())
    list_ord.sort()
    fo ii in list_ord:
        print("{}: {}.".format(i, a_dictionary.get(i)))
