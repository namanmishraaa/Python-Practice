class Computer:

    def config(self):
        print("i5, 16gb, 1tb")


# a = 5 #this is an integer
com1 = Computer()
com2 = Computer()

Computer.config(com1)
Computer.config(com2)

com1.config()      
com1.config() 

print(type(com1))