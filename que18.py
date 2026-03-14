arr = [4, 5, 1, 2, 1, 4, 5]
freq = {}

for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1

for i in arr:
    if freq[i]==1:
        print(i)
        break