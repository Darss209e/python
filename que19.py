def square(x):
    return(x*x)

def iseven(x):
    return(x%2== 0)

print(square(8))
print(iseven(9))

list = [square(x) for x in range(100) if iseven(x)]
print(list)