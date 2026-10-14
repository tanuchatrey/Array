def sort_by(arr):
    # standard sorting function
    return arr.sort()

if __name__ == "__main__":
    arr = [0, 1, 2, 0, 1, 2]
    sort_by(arr)
    
    for num in arr:
        print(num, end=" ")
