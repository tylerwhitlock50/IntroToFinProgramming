aString = 'HomeAlone'
print((aString =="HomeAlone") == "True")
#print(aString.contains('Home'))
#print( True if (aString == 'HomeAlone') else False)
print("omeAlo" in aString)


def function(aVariable):
    if aVariable + 25 == "50":
            return "Arithmetics"
    if aVariable in ["250", "25", "52"]:
            return "Contains"
    return "String"

print( function(25))