###########################################
###############PART 1######################
###########################################
#1

#Print the numbers from 1 to 20, but only the odd numbers
for num in range(1,20,2):
     print(num)

#2
#Add a key 'age' to the dictionary with the value 35
dict.update({'age': 35})

#3
#Print the last 5 elements of the array, but only the even numbers
array = [1,2,3,4,5,6,7,8]
for num in array[-5::2]:
    print(num)

#4
#Get the value of the key 'name' in the dictionary
dict.get('name')

#5
#Get the keys of the dictionary
dict.keys()

#6
dict = {'a': 1, 'b': 2, 'c': 3}
for k,v in dict.items():
    print(k,v)

#7
#Remove the key 'age' from the dictionary and return its value
dict.pop('age')

#8
#Create a dictionary with the following key-value pairs: 'name': 'John', 'age': 34, 'job': 'Developer'
dict = {'name': 'John', 'age': 34, 'job': 'Developer'}

#9
#Add a key 'location' to the dictionary with the value 'Berlin'
dict['location'] = 'Berlin'

#10
#Print the numbers from 0 to 99
for num in range(100):
    print(num)

###########################################
###############PART 2######################
###########################################
#11
#Clear the dictionary
dict.clear()

#12
#Print the letters of the word 'word', but stop when you reach the letter 'o'
for letter in 'word':
    if letter == 'o':
        break
    print(letter)

#13
#Print the last 2 elements of the array
array = [1,2,3,4,5,6,7,8]
for num in array[-2:]:
    print(num)

#14
#Print the letters of the word 'word', but skip the letter 'o'
for letter in 'word':
    if letter == 'o':
        continue
    print(letter)

#15
#Increment the variable 'num' until it reaches 5 using a while loop
num = 0
while num < 5:
    num += 1

#16
#Print the multiplication table from 1 to 9
for i in range(1,10):
    for j in range(1,10):
        print(i*j)

#17
#Get the items of the dictionary as a list of tuples
dict.items()

#18
#Check if the key 'name' is in the dictionary
'name' in dict

#19
#Print the numbers from 1 to 9
for num in range(1,10):
    print(num)

#20
#Get the values of the dictionary
dict.values()

