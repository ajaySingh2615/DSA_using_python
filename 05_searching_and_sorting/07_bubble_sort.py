# Bubble Sort

def bubble_sort(arr):

    for i in range(0, len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp


arr = [5, 4, 1, 3, 2]
bubble_sort(arr)
print(arr)