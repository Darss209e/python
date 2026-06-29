#inheritance

# class car:
#     def __init__(self, type):
#         self.type= type

    
#     @staticmethod
#     def start():
#         print("car started...")

#     @staticmethod
#     def stop():
#         print("car stopped...")

# class toyatacar(car):
#     def __init__(self , name ,type):
#         super().__init__(type)
#         self.name = name
        

# car1 = toyatacar("prius" , "electric")
# print(car1.type)



        
# class A:
#     varA = "welcome to class A"

# class B:
#     varB = "welcome to class B"
# c1 = C()
# print(c1.varC)
# print(c1.varB)
# print(c1.varA)


# property: it uses method as a function

# class student:
#     def __init__(self, phy,chm, math):
#         self.phy = phy
#         self.chm = chm
#         self.math = math
      

#     @property
#     def percentage(self):
#         return  str((self.phy+ self.chm + self.math)/ 3)+ "%"



# sty1 = student(67 , 78 , 87)
# print(sty1.percentage)

# sty1.phy = 96
# print(sty1.percentage)


class complex:
    def __init__(self, real , img):
        self.real = real
        self.img = img

    def shownum(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self, num2):
        newreal = self.real + num2.real
        newimg = self.img + num2.img
        return complex(newreal , newimg)

        

num1 = complex(1,5)
num1.shownum()

num2 = complex(2,6)
num2.shownum()

num3 = num1 + num2
num3.shownum()


        

        

