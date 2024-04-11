# reverse an list

def reverse_list(list1):

    start = 0
    end = len(list1)-1

    while(start < end):
        temp = list1[start]
        list1[start] = list1[end]
        list1[end] = temp

        start+=1
        end-=1


list1 = [2, 4, 6, 8, 10]

reverse_list(list1)
print(list1)