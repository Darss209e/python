class student:
    def __init__(self , name, marks):
        self.name = name
        self.marks = marks
    @staticmethod
    def hello():
        print("hello")

    def average(self):
        sum = 0
        for val in self.marks:
            sum+= val
        print("hi" , self.name, "your avg score is :", sum/3)

s1 = student("darsh",[12,34,56])
s1.average()
s1.hello()

        
