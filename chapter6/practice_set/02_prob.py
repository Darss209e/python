p1= "click this"
p2="buy now"
p3="amke a lot of money"
p4="subscribe"

message=input("enter yor message here :")

if(p1 in message  or p2 in message or p3 in message or p4 in message):
    print("this is a spam message")

else:
    print("this is not a spam message")
    
