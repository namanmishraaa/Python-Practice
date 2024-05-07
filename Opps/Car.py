

class Car:

    wheels = 4 #Class variable/ Static variable
    def __init__(self):   
        self.mil = 10    #instance variable
        self.com = "BMW" #instance variable


c1 = Car()
c2 = Car()


print(f'Car1 variable {c1.com, c1.mil, c1.wheels}')
print(f'Car2 variable {c2.com, c2.mil, c2.wheels}') 