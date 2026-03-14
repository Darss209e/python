arr = [1, 2, 2, 3, 1, 4, 2]
dict ={}

for i in arr:
    if i in dict:
        dict[i] +=1
    else:
        dict[i]=1


print(dict)
