import operator
from pathlib import Path
import os.path
import os



order=""
filename=""
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
file="export_inventory.csv"

def display_inventory(inventory):
    print("Inventory : ")
    for item in inventory:
       print(inventory[item],item)
    print("Total number of items : "+str(sum(inventory.values())))

def add_to_inventory(inventory,added_items):
    for item in added_items:
        if item in inventory.keys():
            inventory[item]+=1
        else:
            inventory[item]=1   
    return inventory

def print_table(inventory,order):
    while True:
        order=input("Would you like to print the table in order? Type 'count,asc' for ascending order, 'count,desc' for descending or hit enter to leave it unordered :")   
        if order=="":
            sorted_inventory=inventory.items()
            break
        if order=="count,asc":
            sorted_inventory=sorted(inventory.items(),key=operator.itemgetter(1),reverse=False)
            break
        if order=="count,desc":
            sorted_inventory=sorted(inventory.items(),key=operator.itemgetter(1),reverse=True)
            break
        else:
            continue

    print("Inventory : ")
    c=("{:>8} {:>15}".format("Count","Item name"))
    print(c)
    print(len(c)*"-")
    
    for key,value in sorted_inventory:
        print("{:>8} {:>15}".format(value,key))
    print(len(c)*"-")
    print("Total number of items : "+str(sum(inventory.values())))
    return inventory.items()

def filee_check(filename):
    if os.path.isfile(filename):
        print("Importable file found!")
        return True
    else:
        print("File not found.")
        return False


def file_check(filename):
    imported=filename+".csv"
    print(imported)
    try:
        with open(imported,"r") as file :
            filename=imported
            return filename
    except IOError:
        print("File not found.")


def import_inventory(inventory,filename):    
    while True:
        filename=input("Enter the importable file's name,type 'ListAllCsv' to list all the .csv files in the directory or press 'ENTER' to skip importing : ")
        if filename=="":
            print("Importing skipped.")
            return inventory       
        elif filename=="ListAllCsv":
            print([x for x in os.listdir() if x.endswith('.csv')])
            True
        else:
            filename=filename+".csv"
            if filee_check(filename)==True:
               with open (filename) as imported_items:
                mylist=imported_items.read().splitlines()
                for items in mylist:
                    for word in items.split(','):
                        if word=="":
                            break
                        if word[-2:]=="\n":
                            word=word[:-2]
                        if word in inventory.keys():
                            inventory[word]+=1                   
                        else:
                            inventory[word]=1
                return inventory
            else:
                continue
  #  print (inventory)
def export_inventory(inv,filename):
    filename=input("Would you like to export ? Type the file's name,hit enter for default value or 'dont save' to skip exporting :")
    if filename=="":
        filename="export_inventory"
        print("Exporting to default inventory.")
    if filename=="dont save":
        print("Exporting skipped.")
        exit()
    else:
        filename=filename+".csv"
        with open(filename, 'w') as f:
            [f.write(value*'{0},'.format(key, value)) for key, value in inv.items()]
            print("File exported as : " +str(filename))

def main():
    add_to_inventory(inv,dragon_loot)
    import_inventory(inv,filename)
    print_table(inv,order)
    export_inventory(inv,file)

main()