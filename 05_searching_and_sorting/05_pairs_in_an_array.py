# pairs in an array

def pairs_in_array(arr):

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            print(f"({arr[i]},{arr[j]})", end="")
        print()

arr = [2, 4, 6, 8, 10]

pairs_in_array(arr)
