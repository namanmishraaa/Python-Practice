def add_item(item, cart=[]):
    cart.append(item)
    return cart

print(add_item("apple")) # o/p : ["apple"]
print(add_item("banana")) # o/p : ["apple", "banana"]