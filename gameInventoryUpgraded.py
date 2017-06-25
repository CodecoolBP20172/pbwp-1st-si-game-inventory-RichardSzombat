import operator
import os.path
import os
import csv
from collections import Counter



order="" #define order string
filename="" #define string filename
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} #This is the default inventory
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby'] #This is the default loot
file="export_inventory.csv" #Default export name

"""def display_inventory(inventory):
    print("Inventory : ")
    for item in inventory:
       print(inventory[item],item)
    print("Total number of items : "+str(sum(inventory.values())))"""

def add_to_inventory(inventory,added_items): #Adding dragon_loot
    for item in added_items:            #If we can find the items name in the inventory.keys()
        if item in inventory.keys():
            inventory[item]+=1          #add +1 to the value
        else:
            inventory[item]=1           #else create the key with the value:1
    return inventory

def print_table(inventory,order):   
    while True:
        order=input("Would you like to print the table in order? Type 'count,asc' for ascending order, 'count,desc' for descending or hit enter to leave it unordered :")   
        if order=="":  #if the input is none/enter , leave the inventory unordered
            sorted_inventory=inventory.items()
            break
        if order=="count,asc": #sort ascending
            sorted_inventory=sorted(inventory.items(),key=operator.itemgetter(1),reverse=False)
            break
        if order=="count,desc": #sort,descending
            sorted_inventory=sorted(inventory.items(),key=operator.itemgetter(1),reverse=True)
            break
        else:
            continue

    print("Inventory : ")
    c=("{:>8} {:>15}".format("Count","Item name"))#format header,align right
    print(c)
    print(len(c)*"-") #print header long strips
    
    for key,value in sorted_inventory:
        print("{:>8} {:>15}".format(value,key))#print and format value-key pairs,align right
    print(len(c)*"-")#print header long strips
    print("Total number of items : "+str(sum(inventory.values())))#print total number of items in inventory(sum of values)
    return inventory.items()

def filee_check(filename): #checks if the entered file exists
    if os.path.isfile(filename):
        print("Importable file found!")
        return True
    else:
        print("File not found.")
        return False


def import_inventory(inventory,filename):    
    while True:# while True,add importable file's name
        filename=input("Enter the importable file's name,type 'ListAllCsv' to list all the .csv files in the directory or press 'ENTER' to skip importing : ")
        if filename=="": #If input is enter ,skipping import,returning our current inventory
            print("Importing skipped.")
            return inventory       
        elif filename=="ListAllCsv":  #list all csv files in the directory
            print("")
            path=[] #this will contain the name of the csv file's in the directory
            path.append([x for x in os.listdir() if x.endswith("csv")])  #append .csv file's to our list
            print(*path[0],sep="\n") #print each file in new line
            print("")
            True
        else:
            filename=filename+".csv"   #with this the user doesnt have to type .csv everytime he is is importing
            if filee_check(filename)==True: #checks if the entered file exists
                with open (filename.rstrip()) as imported_items: #if true,open the file
                    reader=csv.reader(imported_items)
                    mylist=list(reader)#create a list from csv file
                    for items in mylist:#for each line in the list
                        for word in items:#for each word in the list
                            if word=="":#if word=="" it means its the end of the file
                                break
                            if word[-2:]=="\n":#if the last 2 chars of the word are "\n" remove the new line tag
                                word=word[:-2]
                            if word in inventory.keys():
                                inventory[word]+=1   
                            #    print("Word found"+word)                
                            else:
                            #    print("Word not found,created : "+word)
                                inventory[word]=1
                    continue
                    
            else:
                continue
def export_inventory(inventory,filename): #Export inventory
    filename=input("Would you like to export ? Type the file's name,hit enter for default value or 'dont save' to skip exporting :")
    if filename=="": #If input is 'nothing'/enter
        filename="export_inventory"
        print("Exporting to default inventory.")
    if filename=="dont save":# if input is dont save,dont export
        print("Exporting skipped.")
        exit()
    else:
        filename=filename+".csv" # if the filename is anything else,export it as .csv file
        c=Counter(inventory)
        c=sorted(c.elements())
        with open(filename, 'w') as f:
            fWriter=csv.writer(f)
            fWriter.writerow(c)
           # [f.write(value*"{},".format(key, value)) for key, value in inventory.items()]
            print("File exported as : " +str(filename)) #wríte value * inventory.keys() in file
            pass

def main():
    add_to_inventory(inv,dragon_loot)
    import_inventory(inv,filename)
    print_table(inv,order)
    print(inv)
    export_inventory(inv,file)

main()