# using built in function

arr = [10, 20, 30, 40, 50]

arr.reverse()

print("Reversed array:", arr)

# using without built in function

arr = [10, 20, 30, 40, 50]
rev = []

for i in range(len(arr) - 1, -1, -1):
    rev.append(arr[i])

print("Reversed array:", rev)
