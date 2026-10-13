def occurence(arr,val):
      count = 0
      
      for i in arr:
          if i == val:
              count += 1
      
      return("Occurrence of", element, "is:", count)

arr = [10, 20, 10, 30, 10, 40, 20]

element = int(input("Enter element to count: "))
print(occurence(arr,element))
