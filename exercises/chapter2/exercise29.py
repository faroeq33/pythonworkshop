items = ['apple', 'orange', 'banana']
quantity = [5, 3, 2]

orders = zip(items, quantity)
# print(type(orders))
# list method mutates orders and turns it into a list

# print(dict(orders))

fruitInventory = dict(
    zip(items, quantity)
)

print(fruitInventory)
