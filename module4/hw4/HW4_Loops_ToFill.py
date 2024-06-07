## FILL IN THE EXERCISE BELOW ##
## YOU MAY RUN HW4_LOOPS_TEST.PY TO CHECK YOUR SCORE OUT OF 10 ##

# Q1 (1 point)
# Create a function, exampleOne, which takes one integer as an input parameter.
# Using a loop, populate an array with all values from 0 up to that integer.
# Example Input Parameter: 5
# Example Output: [0, 1, 2, 3, 4]

def exampleOne(n):
    result = []
    for i in range(0,n):
        result.append(i)
    return result


# Q2 (1 point):
# Create a function, exampleTwo, which takes two integers as input parameters.
# Return an array with all values from the first integer to the second integer.
# Example Input Parameter: 2, 5
# Example Output: [2, 3, 4]

def exampleTwo(n,m):
    result = []
    for i in range(n,m):
        result.append(i)
    return result

# Q3 (1 point):
# Create a function, exampleThree, which takes two integers as input parameters.
# Return an array with all values from the first integer to the second integer, skipping every other number.
# Example Input Parameter: 2, 10
# Example Output: [2, 4, 6, 8]

def exampleThree(n,m):
    result = []
    for i in range(n,m,2):
        result.append(i)
    return result

# Q4 (2 points):
# Create a function, exampleFour, which takes an input array
# Using a loop, populate a new array with all values from the input array, starting at the 2nd element, multiplied by the previous element
# Example Input Parameter: [2,3,4,5]
# Example Output: [6,12,20]

def exampleFour(arr):
    result = []
    for i in range(1,len(arr)):
        result.append(arr[i]*arr[i-1])
    return result

# Q5 (2 points):
# Create a function, exampleFive, which takes an input array
# Using a loop, populate a new array with all values from the input array that are even (hint: % operator)
# Example Input Parameter: [2, 3, 4, 5]
# Example Output: [2, 4]

def exampleFive(arr):
    result = []
    for i in arr:
        if i%2 == 0:
            result.append(i)
    return result

# Q6 (3 points):
# Create a function, exampleSix, which takes two input arrays
# If the two arrays are equal in length, populate a new array with all values from the first input array multiplied by the second
# If the two arrays are not equal in length, return "!Array Mismatch!"

def exampleSix(arr1,arr2):
    result = []
    if len(arr1) == len(arr2):
        for i in range(0,len(arr1)):
            result.append(arr1[i]*arr2[i])
        return result
    else:
        return "!Array Mismatch!"