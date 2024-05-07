

class Student:
    
    school = 'Telusko'

    def __init__(self, mark1, mark2, mark3):
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def get_mark1(self):
        return self.mark1
    
    def set_mark1(self):
        self.mark1 = mark1

    def avg(self):
        return (self.mark1 + self.mark2 + self.mark3) / 3

    @classmethod
    def info(cls): #class method
        return cls.school

student1 = Student(23,45,40)        
student2 = Student(43,35,20)        

print(f"Average mark of Student1 :{student1.avg}")
print(f"Average mark of Student2 :{student2.avg}")

print(student1.info())