# exercise that supposedly was a twitter interview question
# build a roman numerals calculator

# read in the first roman numeral
roman_num = raw_input("Whhich number would you like to convert? ")

char_list = []

# split the roman numeral up by character and add each to a list
# list is necessary because order is important
for char in roman_num:
	char.split()
	char_list.append(char)
	print char_list

# # convert roman numerals to arabic numerals
# for char in char_list:
# 	if char == "i":
# 		char = 1
# 	if char == "v":
# 		char = 5
# 	if char == "x":
# 		char = 10
# 	else:
# 		print "I can't count higher than 40, pick a smaller number."
# 		break
# 	print char_list

char_list = [10, 1, 5]

# add up the value of list to get arabic numerals. check if 1 is in there before other numbers
if len(char_list) == 1:
	arab_num = char_list[0]

if len(char_list) == 2 and char_list[0] == 1:
	arab_num = char_list[1] - char_list[0]
else:
	arab_num = sum(char_list)

if len(char_list) == 3 and char_list[1] ==1:
	arab_num = char_list[0] + char_list[2] - char_list[1]
else: 
	arab_num = sum(char_list)

print arab_num
