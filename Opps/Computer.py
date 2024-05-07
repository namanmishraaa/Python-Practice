class Computer:

    def __init__(self, ):
        self.name = "Naman"    
        self.age = 15

    def update(self):
        self.age = 36

    def compare(self, other):
        # if self.age == other.age:
        #     return True
        # else:
        #     return False
        return self.age == other.age

c1 = Computer()
c2 = Computer()

c1.name = "Ichigo"
c1.age = 17

Computer.update(c2)
c1.update()

if c1.compare(c2):
    print("They are same")
else :
    print("They are different")


print(f"Name: {c1.name} \nAge :{c1.age}")
print(f"Name: {c2.name} \nAge :{c2.age}")
# print(id(c1))
# print(id(c2))