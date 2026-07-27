def add_item(item, cart=[]):
    cart.append(item)
    return cart

print(add_item("apple")) # o/p : ["apple"]
print(add_item("banana")) # o/p : ["apple", "banana"]

# above code is buggy here it the new implementation 

def add_item(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart

print(add_item("apple")) # o/p : ["apple"]
print(add_item("banana")) # o/p : ["banana"]


print(100*'=')

def summarize(*args, **kwargs):
    for i in args:
        print(i)
    for k,v in kwargs.items():
        print(f'{k}:{v}')

#updated code 

def summarize(*args, **kwargs):
    if args:
        print(f'Positional : {args}')
    if kwargs:
        print(f'keyword : {kwargs}')

summarize(1,2,3)
summarize(name="Nammo", role="SDET")


x = 10

def change_x():
    global x
    x = 20
    print("Inside function:", x)

change_x()
print("Outside function:", x)