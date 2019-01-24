''' A program that uses a binary_search method to find an item in a list. This function helps search a list faster than a just a value in list statement. '''

def binary_search(array, target):
    min = 0
    max = len(array) - 1
    found = False
    while (min <= max and not found):
        midpoint = (min+max)//2
        if array[midpoint]==target:
            found = True
        else:
            if target < array[midpoint]:
                max = midpoint-1
            else:
                min = midpoint+1
    return found
 

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
