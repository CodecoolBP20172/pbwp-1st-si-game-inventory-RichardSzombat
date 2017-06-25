# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification
import operator
from pathlib import Path
import os.path
import os
import csv
from collections import Counter

mylist = list()
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12, }
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
exporting = "export_inventory.csv"
importing = "test_inventory.csv"

# Displays the inventory.


def display_inventory(inventory):
    print("Inventory : ")
    for item in inventory:
       print(inventory[item], item)
    print("Total number of items : " + str(sum(inventory.values())))


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory.keys():
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory

# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory)
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order


def print_table(inventory, order=None):
    while True:
        if order is None:
            sorted_inventory = inventory.items()
            break
        if order == "count,asc":
            sorted_inventory = sorted(
                inventory.items(), key=operator.itemgetter(1), reverse=False)
            break
        if order == "count,desc":
            sorted_inventory = sorted(
                inventory.items(), key=operator.itemgetter(1), reverse=True)
            break
        else:
            continue

    print("Inventory : ")
    c = ("{:>8} {:>15}".format("Count", "Item name"))
    print(c)
    print(len(c) * "-")

    for key, value in sorted_inventory:
        print("{:>8} {:>15}".format(value, key))
    print(len(c) * "-")
    print("Total number of items : " + str(sum(inventory.values())))
    return inventory.items()


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename):
    with open(filename) as imported_items:
        reader = csv.reader(imported_items)
        mylist = list(reader)
        for items in mylist:
            for word in items:
                if word == "":
                    break
                if word[-2:] == "\n":
                    word = word[:-2]
                if word in inventory.keys():
                    inventory[word] += 1
                else:
                    inventory[word] = 1



# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).
def export_inventory(inventory, filename):
    c=Counter(inventory)
    c=sorted(c.elements())
    with open(filename, 'w') as f:
        fWriter=csv.writer(f)
        fWriter.writerow(c)
        pass
           # [f.write(value*"{},".format(key)) for key, value in inventory.items()]


#display_inventory(inv)
add_to_inventory(inv, dragon_loot)
import_inventory(inv, "import_inventory.csv")
print_table(inv,"count,desc")
export_inventory(inv, "export_inventory.csv")
