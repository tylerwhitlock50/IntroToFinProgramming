###########################################
###############PART 1######################
###########################################
#1
numbers = [] #empty list
#2
my_list = [2, 6, 10, 4, 8] #list with 5 elements
#3
my_list.append(1) #add 1 to the end of the list
my_list.append(3) #add 3 to the end of the list
my_list.append(5) #add 5 to the end of the list
#4
value = my_list[1] #get the second element of the list
#5
my_list.remove(3) #remove 3 from the list
#6
my_list.sort() #sort the list
#7
my_list.reverse() #reverse the list
#8
v2 = len(my_list) #get the length of the list
#9
v3 = my_list.pop(0) #remove the first element of the list
#10
my_list.insert(0, 7) #insert 7 at the beginning of the list
###########################################
###############PART 2######################
###########################################
#11
v4 = my_list.index(10) #get the index of 10 in the list
#12
v5 = my_list[1:4] #get a sublist from index 1 to 3
#13
v6 = my_list + new_list #combine two lists NOTE: new_list is not defined
#14
my_list.clear() #clear the list
#15
p1 = combined_list.pop(4) #remove the last element of the list NOTE: combined_list is not defined
#16
v7 = combined_list[:3]  #get the first 3 elements of the list NOTE: combined_list is not defined
#17
v8 = added_list[3:7] #get a sublist from index 3 to 6 NOTE: added_list is not defined
#19
v9 = added_list[0::2] #get every other element starting from index 0 NOTE: added_list is not defined
#20
v10 = sum(added_list) #get the sum of all elements in the list NOTE: added_list is not defined
