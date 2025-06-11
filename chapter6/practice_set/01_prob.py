mark1=int(input("enter marks in 1:"))
mark2=int(input("enter marks in 2:"))
mark3=int(input("enter marks in 3:"))

total_percentage = ((mark1 + mark2+mark3)*100)/300

if(total_percentage>=40 and mark1>=33 and mark2>=33 and mark3>=33):
    print("congrats !! you passed the test",total_percentage)

elif(total_percentage<40):
    print("soory better luck next year!",total_percentage)
      