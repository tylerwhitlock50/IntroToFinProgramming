###########################################
###############PART 1######################
###########################################

#1 Open the File in Append Mode
f = open("myfile.txt", "a")
#2 Read the file
line = f.read()
#3 Split the line
vars = line.split(",")
#4 Create a new line with the first 3 variables
line = "{},{},{}\n".format(vars[0],vars[1],vars[2])
#5 Read the rest of the lines
lines = f.readlines[1:]
#6 Write the new line and the rest of the lines
f.writelines(lines)
#7 Write a new line
f.write("\n")

###########################################
###############PART 2######################
###########################################

#8 Close the file
f.close()
#9 Open the file in read mode
f = open("myfile.txt", "r")
#10 Write a new line
f.writelines(["Python","Rules", "FinTech","To The Moon" ])
#11 Open the file in write mode
f = open("myfile.txt", "w")
#12 Remove whitespace
line = line.strip()
#13 Write the lines seperated by new lines
f.writelines(["Python,Rules\n", "FinTech,To The Moon\n" ])
#14 Close the file
f.close()
