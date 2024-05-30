## FILL IN THE EXERCISE BELOW ##
## YOU MAY RUN HW3_LC_TEST.PY TO CHECK YOUR SCORE OUT OF 10 ##

# Q1 (1 Point)
# Prompt: Please create a function, exampleOne, which takes two input parameters.
# Return True if these parameters are equal to each other
# Return False if these parameters are not equal to each other
def exampleOne(p1,p2):
    return p1 == p2



# Q2 (1 point):
# Prompt: Please create a fucntion, exampleTwo, which takes three input parameters
# Return True if none of these parameters equal each other
# Return False if not

def exampleTwo(p1,p2,p3):
    return p1 != p2 and p1 != p3 and p2 != p3



# Q3 (1 point)
# Prompt: Please create a function, exampleThree, which takes two input parameters: an array and an integer
# Return True if the integer is greater than, or equal to, the length of the array
# Return False if the array is smaller than the length of the array

def exampleThree(arr, num):
    return num >= len(arr)

exampleThree = lambda arr, num: num >= len(arr)



# Q4 (2 point)
# Prompt: Please create a function, exampleFour, which takes three input parameters
# Return True if either first is different from second or second is same as third
# Otherwise, return False

# def exampleFour(p1,p2,p3):
#     return p1 != p2 or p2 == p3

exampleFour = lambda p1, p2, p3: p1 != p2 or p2 == p3


# Q5 (2 points)
# Prompt: Please create a function, exampleFive, which takes two input parameters
# Return True if first param is part of second param
# Return False if second param is part of first param
# Return 0 otherwise

# def exampleFive(p1,p2):
#     if p1 in p2:
#         return True
#     elif p2 in p1:
#         return False
#     else:
#         return 0
    
exampleFive = lambda p1, p2: True if p1 in p2 else (False if p2 in p1 else 0)




# Q6 (3 points)
# Prompt: Please create a function, exampleSix, which takes three input parameters: 2 arrays, and 1 string
# Return "Both" if the string is in both arrays
# Return "First" if the string in only in the first array
# Return "Second" if the string is only in the second array
# Return "Neither" if the string is in neither arrays

# def exampleSix(arr1,arr2,str):
#     if str in arr1 and str in arr2:
#         return "Both"
#     elif str in arr1:
#         return "First"
#     elif str in arr2:
#         return "Second"
#     else:
#         return "Neither"
    
exampleSix = lambda arr1, arr2, string: "Both" if string in arr1 and string in arr2 else ("First" if string in arr1 else ("Second" if string in arr2 else "Neither"))
