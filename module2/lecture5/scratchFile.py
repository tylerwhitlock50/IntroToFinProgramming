text = "Utah man am I"
textArray = text.split()
print(textArray)
print(textArray[0], textArray[3])

print(textArray.index('I'))
print(textArray.index('Utah'))
print(textArray[0])

textArray.append('!')   
print(textArray)
print(type(textArray))

text2 = "Utes are the best! We love Utah"
textArray2 = text2.split()

textArray3 = textArray + textArray2
print(textArray3)

listOfLists = [textArray, textArray2]
print(listOfLists)

#print last 10 letters of text2
print(text2[-10:])
#print middle 10 letters of text2  
print(text2[5:15])

returned_var = textArray2.pop(2)

textArray2.insert(2, 'the')
textArray2.remove('the')
print(textArray2)
print(returned_var)

stringVar = 'WE LOVE UtAH' 
for char in stringVar:
    print(char.capitalize())
listVar = list(stringVar.upper()) #convert each character to a list element
print(listVar)
listVar.pop(4)
listVar.remove('W')

print(listVar)

print(listVar.count('E'))


firstNames = ['John', 'Jane', 'Jim', 'Jill']
lastnames = ['Sniff,', 'Snuff', 'Snork', 'Snorkle']

names = []
for name in zip(firstNames, lastnames):
    print(f"First name:{name[0]}\nLast name:{name[1]}")
    names.append(name)

print(names)

for i in range(0, 10000, 100):
    print(i)