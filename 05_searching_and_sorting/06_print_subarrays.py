def print_subarrays(arr):

    n = len(arr)
    
    for i in range(n): # starting index of subarray
        for j in range(i, n): # ending index of subarray
            for k in range(i, j+1): # Elements within subarray
                print(arr[k],end="", sep="," )
            print()
        print()


arr = [2, 4, 6, 8, 10]
print_subarrays(arr)
