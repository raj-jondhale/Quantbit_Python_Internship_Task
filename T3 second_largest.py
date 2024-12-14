#Task 3 Find the second largest number in a list
def secondLargest(arr, n):
    if (n < 2):
        return -1
    large = float('-inf')
    second_large = float('-inf')
    for i in range(n):
        if (arr[i] > large):
            second_large = large
            large = arr[i]
        elif (arr[i] > second_large and arr[i] != large):
            second_large = arr[i]
    return second_large

arr = [10, 20, 4, 45, 99]
n = len(arr)
sL = secondLargest(arr, n)
print("Second largest is", sL) #output 45