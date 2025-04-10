
def add_item_to_inv(item):
    inv = open("GroceryInventoryList.csv", "a")
    inv.write(item + "\n")
    inv.close()

def remove_item_from_inv(item):
    inv = open("GroceryInventoryList.csv", "r")
    lines = inv.readlines()

    inv = open("GroceryInventoryList.csv", "w")
    for line in lines:
        if line.strip().lower() != item:
            inv.write(line)
    inv.close()

def print_inv():
    inv = open("GroceryInventoryList.csv", "r")
    print(inv.read())
    inv.close()

def check_or_create_inv_file():
    print("Looking for file...")
    try: 
        inv = open("GroceryInventoryList.csv", "r")
        print("File found")
    except FileNotFoundError:
        print("File not detected, creating file...")
        inv = open("GroceryInventoryList.csv", "w")
        pass
        inv.close()

def check_or_create_groclist_file():
    print("\nLooking for file...")
    try: 
        list = open("GroceriesList.csv", "r")
        print("File found")
    except FileNotFoundError:
        print("File not detected, creating file...")
        list = open("GroceriesList.csv", "w")
        pass
        list.close()


def add_item_to_groclist(item):
    inv = open("GroceriesList.csv", "a")
    inv.write(item + "\n")
    inv.close()


def user_action_question():
    global user_action
    user_action = input("\nSelect '+' to add item, '-' to remove item, 'v' to view inventory, or 'q' to quit\n")
    if user_action == 'v':
        user_print_list()
    elif user_action == '+':
        if_plus()
    elif user_action == '-':
        if_minus()
    elif user_action == 'q':
        exit


def user_print_list():
    print("\nInventory:")
    print_inv()
    user_action_question()
    

def if_plus():
    user_item_to_add = input("\nWhat item would you like to add?\n")
    add_item_to_inv(user_item_to_add.strip().lower())
    print("\n" + user_item_to_add.strip().lower() + " added to inventory.\n")
    add_another_item = input("Would you like to add another item?\ny/n: ")
    if add_another_item == 'y':
        if_plus()
    user_action_question()



def if_minus():
    user_item_to_remove = input("\nWhat item would you like to remove?\n")
    remove_item_from_inv(user_item_to_remove.strip().lower())
    print("\n" + user_item_to_remove.strip().lower() + " removed.\n")
    add_to_groc_list = input("Would you like to add " + user_item_to_remove + " to your grocery list?\ny/n: ")
    if add_to_groc_list == 'y':
        check_or_create_groclist_file()
        add_item_to_groclist(user_item_to_remove)
        print("Item added to grocery list.\n")
    elif add_to_groc_list == 'n':
        user_action_question()
    else:
        print("invalid response")


#PROGRAM START
print("\n--- Grocery Inventory Manager ---")
check_or_create_inv_file()
user_action_question()

