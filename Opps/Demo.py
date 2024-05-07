class Computer:

    def __init__(self, cpu, ram):
        # print("inside init method")
        self.cpu = cpu
        self.ram = ram
        
    def config(self):
        print(f'config is {self.cpu} with ram {self.ram}')


com1 = Computer('i5', 16)
com2 = Computer('Ryzen 5', 32)

# Computer.config(com1)
# Computer.config(com2)

com1.config()      
com1.config() 

print(type(com1))

a = 5 #this is an integer
a.bit_length()