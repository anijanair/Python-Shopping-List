# make a list
shopping_list = []

# give instructions to user
print("What is the item to be added to the shopping list?")
print("Enter 'DONE' to finish the list")

# ask for item to be added
while True:
    new_item = input("> ")

    # be able to quit
    if new_item == 'DONE':
        break

    # add item to the list
    shopping_list.append(new_item)

# print the list
print("Here's the shopping list: ")
for item in shopping_list:
    print(item)