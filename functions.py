a = [4, 2, 5, 2, 1]

print("Original array:", a)

a.append(6)
print("After append:", a)

a.insert(1, 10)
print("After insert:", a)

a.remove(2)
print("After remove:", a)

a.pop()
print("After pop:", a)

a.sort()
print("After sort:", a)

print("Index of 5:", a.index(5))
print("Count of 2:", a.count(2))
