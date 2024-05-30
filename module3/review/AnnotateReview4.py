###########################################
###############PART 1######################
###########################################
#1 Print an empty string if x is greater than 0, otherwise print an empty string
x = 5
if x > 0:
    print("")
else:
    print("")

#2 Print an empty string if y is greater than 0, print an empty string if y is equal to 0, otherwise print an empty string
y = -3
if y > 0:
    print("")
elif y == 0:
    print("")
else:
    print("")

#3 Print an empty string if a and b are both True, otherwise print an empty string
a = True
b = False
if a and b:
    print("")
else:
    print("")

#4 Print an empty string if a or b are both True, otherwise print an empty string
if a or b:
    print("")
else:
    print("")

#5 Print an empty string if a is False, otherwise print an empty string
if not a:
    print("")
else:
    print("")
   
#6 Print an empty string if num is greater than 0 and num is even, otherwise print an empty string
num = 25
if num > 0 and num % 2 == 0:
    print("")

#7 Print an empty string if the word "hello" contains the letters "h", "e", and "o", otherwise print an empty string
word = "hello"
if "h" in word and "e" in word and "o" in word:
    print("")

#8 Print empty strings based on the following conditions:
# If the score is greater than or equal to 90, print an empty string
# If the score is greater than or equal to 80, print an empty string
# If the score is greater than or equal to 70, print an empty string
# Otherwise, print an empty string
scores = [80, 75, 90, 95]
for score in scores:
    if score >= 90:
        print("")
    elif score >= 80:
        print("")
    elif score >= 70:
        print("")
    else:
        print("")

###########################################
###############PART 2######################
###########################################
#9 Print the numbers 1 through 5 using a while loop
i = 1 
while i <= 5:
    print(i)
    i += 1

#10 Print the odd numbers 1, 3, and 5 using a for loop
nums = [1, 2, 3, 4, 5]
for num in nums:
    if num % 2 == 0:
        continue
    print(num)

   
#11 Print the numbers 1, 2, and 3 using a for loop
for num in nums:
    if num == 4:
        break
    print(num)


#12 Print an empty string if all the numbers in the list are even
num_list = [2, 4, 6, 8, 10]
if all(i % 2 == 0 for i in num_list):
    print("")

#13 Print an empty string if any of the numbers in the list are divisible by 3
if any(i % 3 == 0 for i in num_list):
    print("")

z = 10 #define Z
# Print and empty string if x is less than y and y is less than z
if x < y < z:
    print("") #Added the empty string

#14 Print an empty string if x is not equal to y    
x = "hello"
y = "world"
if x != y:
    print("")

#15 Print an empty string if age is >= 18
age = 30
if age >= 18:
    print("")