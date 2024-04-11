# find the largest number in given list

def largest_number(numbers):
    
    # check if list is empty
    if not numbers: 
        return None
    
    # Initialize the maximum number with the first element of the list
    maximum_number = numbers[0]

    # Iterate thought entire list to check the largest element from element 2
    for i in range(1, len(numbers)):
        if maximum_number < numbers[i]:
            maximum_number = numbers[i]
    
    return maximum_number


l1 = [10, 50, 30, 70, 80, 60, 20, 90, 40]

number = largest_number(l1)

if number == None:
    print(f"List is empty")
else:
    print(f"Largest number is : {number}")
