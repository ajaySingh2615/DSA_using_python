def linear_search_algo(l1, key):

    for i in range(len(l1)):
        if l1[i] == key:
            return i
            break
    
    return -1

l1 = [10, 50, 30, 70, 80, 60, 20, 90, 40]
key = 20

result = linear_search_algo(l1, key)

if result:
    print(f"{key} found at index {result+1}")
else:
    print(f"No match found")


