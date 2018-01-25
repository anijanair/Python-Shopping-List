# make a list
# have a 'HELP' command
# have a 'SHOW' command

shopping_list = []

# give instructions to user

print("What is the item to be added to the shopping list? ")


def show_help():
    print("""
Enter 'DONE' to finish the list
Enter 'HELP' for this help
Enter 'SHOW' to see the current list
""")


show_help()


# print the list
def show_list():
    print("Here's the shopping list: ")
    for item in shopping_list:
        print(item)


# add item to the list
def add_an_item():
    shopping_list.append(new_item)
    print("Added {}. List now has {} items".format(new_item, len(shopping_list)))


# ask for item to be added
while True:
    new_item = input("> ")

    # be able to quit
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue
    else:
        add_an_item()

show_list()





