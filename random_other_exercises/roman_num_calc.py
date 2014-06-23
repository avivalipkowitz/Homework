# exercise that supposedly was a twitter interview question
# build a roman numerals calculator


def main():

	# read in the first roman numeral
	roman_num = raw_input("Which number would you like to convert? ")

	char_list = []

	# split the roman numeral up by character and add each to a list
	# list is necessary because order is important

	def split_roman(roman_num):
		for char in roman_num:
			char_list.append(char)
		print char_list
		return char_list

	def convert_roman_to_arabic(char_list):
		# convert roman numerals to arabic numerals
		for i in range(0, len(char_list)):
			if char_list[i] == "i":
				char_list[i] = 1

			elif char_list[i] == "v":
				char_list[i] = 5

			elif char_list[i] == "x":
				char_list[i] = 10
			
			else:
				print "I can't count higher than 40, pick a smaller number."
				break
		print("char_list is: %r ") % char_list
		return char_list

# char_list = [10, 1, 5]

	def sum_of_arab_nums(char_list):
		sum_list = []
		# add up the value of list to get arabic numerals. check if 1 is in there before other numbers
		if char_list[-2] == 1:
			for i in range(0, -2):
				sum_list.append(char_list[i])
			arab_num = sum(sum_list) + char_list[-1] - char_list[-2]

		else: 
			arab_num = sum(char_list)

		return arab_num



		# if len(char_list) == 1:
		# 	arab_num = char_list[0]


		# if len(char_list) == 1:
		# 	arab_num = char_list[0]

		# if len(char_list) == 2 and char_list[0] == 1:
		# 	arab_num = char_list[1] - char_list[0]
		# else:
		# 	arab_num = sum(char_list)

		# if len(char_list) == 3 and char_list[1] ==1:
		# 	arab_num = char_list[0] + char_list[2] - char_list[1]
		# else: 
		# 	arab_num = sum(char_list)


		# print arab_num
		# return arab_num

	arab_total = sum_of_arab_nums(convert_roman_to_arabic(split_roman(roman_num)))
	# arab_total = sum_of_arab_nums(char_list)
	print("The final total is: ", arab_total)

if __name__=="__main__":
	main()

