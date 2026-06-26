class student:
    college_name = "MECW"
    
    def __init__(self , fullname, marks):
        self.name = fullname        
        self.marks = marks

    def welcome(self):
        print("welcome student,",self.name)

    def get_marks(self):
        return self.marks

s1 = student("darsh",78)
s1.welcome()
print(s1.get_marks())




     