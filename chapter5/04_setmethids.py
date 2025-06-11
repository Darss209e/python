s = {1, 2}
s.add(3)
print(s)  # {1, 2, 3}

s.remove(2)
print(s)  # {1, 3}

s.discard(4)  # No error even though 4 is not in the set
print(s)  # {1, 3}

item = s.pop()
print(item)  # Could be 1 or 3

s.clear()
print(s)  # set()

a = {1, 2}
b = {2, 3}
print(a.union(b))  # {1, 2, 3}

print(a.intersection(b))  # {2}

print(a.difference(b))  # {1}

print(a.symmetric_difference(b))  # {1, 3}
