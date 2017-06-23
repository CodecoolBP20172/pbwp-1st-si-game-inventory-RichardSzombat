import operator
order=""
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
    print(sorted_inventory)
    return inventory.items()

def import_inventory(inventory,filename):
#    print(inventory)
    
    with open (filename) as imported_items:
        mylist=imported_items.read().splitlines()
        for items in mylist:
            for word in items.split(','):
                if word[-2:]=="\n":
                    word=word[:-2]
                if word in inventory.keys():
                    inventory[word]+=1                   
                else:
                    inventory[word]=1
  #  print (inventory)
def export_inventory(inv,filename):
    file=input("Enter the filename.csv :")
    if file=="":
        file="export_inventory.csv"
    else:
        file=file+".csv"
    with open(file, 'w') as f:
        [f.write(value*'{0},'.format(key, value)) for key, value in inv.items()]


add_to_inventory(inv,dragon_loot)
import_inventory(inv,"import_inventory.csv")
print_table(inv,order)
export_inventory(inv,file)