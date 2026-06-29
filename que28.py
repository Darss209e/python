class employee:
    def __init__(self , role , dept , salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showdetails(self):
        print("role =",self.role)
        print("dept = ",self.dept)
        print("salary = ",self.salary)

class engineer(employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age 
        super().__init__("engineer","IT","75000")

E1 = employee("accountant.", "finance", "50,000")
E1.showdetails()
        
eng1 = engineer("darsh", 21)
eng1.showdetails() 