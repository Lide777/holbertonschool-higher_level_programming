#!/usr/bin/python3
def print_element_at_index(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        print("Index out of range")
    else:
        print("{:d}".format(my_list[idx]))
