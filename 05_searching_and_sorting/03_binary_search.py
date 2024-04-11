def binary_search_algo(l1, element):

    low = 0
    high = len(l1)-1

    while(low <= high):
        
        # mid
        mid = low + (high - low) // 2

        # if element is present at the middle
        if l1[mid] == element:
            return mid
        
        # if element is smallest than middle element, search in left side
        elif l1[mid] > element:
            high = mid - 1
        
        # if element is largest than middle element, search in right side
        else:
            low = mid + 1
        
    # if element is not present in the list
    return -1
            


l1 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
element = 20

result = binary_search_algo(l1, element)
if result != -1:
    print(f"{element} is found at index {result+1}")
else:
    print(f"No match found")    
