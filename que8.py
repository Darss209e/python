a = int(input("enter your first num"))
b = int(input("enter your second num"))
c = int(input("enter your third num"))

if(a>=b and a>=c):
    print("first num is largest",a)
elif(b>=c):
    print("second num is largest",b)
else: 
    print("third num is largest",c)
