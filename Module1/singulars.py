
name = 'Tyler' # string name
# print(name)

lastName = 'Whitlock' # string lastName
# print(lastName)

homeTown = 'Nephi' # string homeTown
# print(homeTown)

year, month, day = '1991','September','1st' # string year, month, day
# print(f"{month} {day}, {year}")

yearStr = '1991' # string yearStr
yearNum = 1991 # Num yearNum
# print("String :", yearStr) #print
# print("Number:", yearNum) #print

division = yearNum / 89 # division
# print(division)


# print(type(yearStr)) #print type
# print(type(yearNum)) #print type
# print(type(division)) #print type

#create new variable that will calculate the difference between current year and the year of birth
currentYear = 2024 # current year
age = currentYear - yearNum # age
combninedString = name + " " + lastName # combined string
# print("Hi, my name is", combninedString) #print
# print(f"{name} is {age} years old.") #print

remaineder = yearNum % 89 # remainder
# print(remaineder) #print

booleanY, booleanN = True, False # boolean
booleanStrY = 'True'
print(booleanY) #print
print(True)
print(booleanY == True) #print
print(booleanY == booleanStrY) #print


"""
This piece of code is an example of a conditional statement.
The code is checking the value of the variable 'asset' and then
printing the appropriate method to use based on the value of 'asset'.

asset = 'Stock' -> use DDM
asset = 'Bond' -> use PV
else -> use CAPM

This the asset peice is redefined multiple times.  Comment out the values you don't
want to use.

"""
asset = 'Stock'
asset = 'Bond'
asset = 'Real Estate'
if asset == 'Stock':
    print('use DDM')
elif asset == 'Bond':
    print('use PV')
else:
    print('use CAPM')

person = 'Professor'
if not(person == 'Student'):
    print('You Get Paid')

smallCap, midCap, largeCap = 'Small','Mid','Large'
marketCap = 250
var = ''
if marketCap < 250:
    var = smallCap
if marketCap >= 250 and marketCap < 1000:
    var = midCap
if marketCap >= 1000:
    var = largeCap
print(var)

yearsinSchool = 4
person = 'Student'
if person == 'Student':
    if yearsinSchool == 4 or yearsinSchool >= 5:
        print('Senior')
    else:
        print('Not Senior')
else:
    print("Not a Student")