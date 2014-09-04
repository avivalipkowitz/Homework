# Using ruby 1.8.7

# Get user input
calc_string = ARGV[0]
calc_item_string_list = calc_string.split
puts calc_item_string_list
calc_item_int_list = []


# create a function that transforms string to ascii, then to int and operators
# also needs to check that the string is not actually a letter or some other invalid character
# def atoi(string):


# check for appropriate number of arguments
if calc_item_string_list.length < 3
	puts "not enough arguments"
end


for item in calc_item_string_list
	length = item.length
	# have a separate loop for numbers that are greater than 9 or less than 0
	if length > 1
		if item == "**"
			calc_item_int_list << item
		else
			item_sublist = item.split(//)
			negative = false
			i = 1
			item_total = 0
			for unit in item_sublist
				# check for invalid numbers
				if unit[0] < 42 or unit[0] > 57
					puts "invalid number"
					return "invalid number"
				# check for negative numbers
				elsif unit == "-"
					negative = true

				else
					#check for decimal, adjust "length" if necessary
					if item.include? "."
						decimal_index = item.rindex('.')
						dec_dist_from_end = length - decimal_index
						length -= dec_dist_from_end
					end
					ascii_unit = unit[0]
					#check for decimal
					if ascii_unit == 46
						i += 0
					# else convert ascii to integer or float
					else
						# if it's negative, that '-' should not be included in length
						if negative
							length -= 1
						end
						int_unit = ascii_unit - 48
						item_total += int_unit * 10 ** (length - i)
						i += 1
						puts "item_total = #{item_total}"
					end
				end
			end
			
			if negative == true
				item = item_total * -1
			else
				item = item_total
			end

			calc_item_int_list << item
			puts "calc_item_int_list is"
			puts calc_item_int_list
		end

	elsif length == 1
		
		# check for invalid numbers
		if item[0] < 42 or item[0] > 57
			puts "invalid number"
			break
		# convert string numbers to integers
		elsif item[0] >= 48 and item[0] <= 57:
			puts "item is #{item}"
			ascii_item = item[0]
			puts "ascii_item is #{ascii_item}"
			int_item = ascii_item - 48
			puts "int_item = #{int_item}"
			item = int_item
			calc_item_int_list << item
			puts "calc_item_int_list is"
			puts calc_item_int_list
		elsif item[0] > 41 and item[0] < 48
			calc_item_int_list << item
			puts "calc_item_int_list is"
			puts calc_item_int_list

		end
	
	end
	
end


# make an operation sublist
calc_sublist1 = []
calc_sublist2 = []

# add all numbers to a sublist, until you hit an operator. 
# at that point, get the sum/product/diff etc, and put that number in a second sublist
# the last item in calc_item_int_list will be an operator, 
# so that can be tagged onto the end of calc_sublist2 automatically in the next step
for item in calc_item_int_list[0..-1]:
	puts "item is #{item}"
	if item.is_a?(String) == false
		calc_sublist1 << item
		puts "calc_sublist1 is"
		puts calc_sublist1
	elsif item == "+"
		sum = 0
		for sublist_item in calc_sublist1
			sum += sublist_item
		end
		calc_sublist2 << sum
		calc_sublist1 = []
		puts "sum calc_sublist2 is"
		puts calc_sublist2
	



	# need to pick up here in the morning--this difference function isn't working yet


	elsif item == "-"
		diff = calc_sublist1[0]
		for sublist_item in calc_sublist1[1..-1]
			diff -= sublist_item
		end
		calc_sublist2 << diff
		calc_sublist1 = []
		puts "diff calc_sublist2 is"
		puts calc_sublist2
	elsif item == "*"
		prod = 1
		for sublist_item in calc_sublist1
			prod = prod * sublist_item
		end
		calc_sublist2 << prod
		calc_sublist1 = []
		puts "prod calc_sublist2 is"
		puts calc_sublist2
	elsif item == "/"
		quot = calc_sublist1[0]
		for sublist_item in calc_sublist1[1..-1]
			quot = quot/sublist_item
		end
		calc_sublist2 << quot
		calc_sublist1 = []
		puts "quot calc_sublist2 is"
		puts calc_sublist2
	elsif item == "**"
		exp = calc_sublist1[0]
		for sublist_item in calc_sublist1[1..-1]
			exp = exp ** sublist_item
		end
		calc_sublist2 << exp
		calc_sublist1 = []
		puts "exp calc_sublist2 is"
		puts calc_sublist2
	end
end

# append last item (operator) to calc_sublist2
calc_sublist2 << calc_item_int_list[-1]	
puts "second calc_sublist2 is"
puts calc_sublist2

# check length of calc_sublist2, to see if more calculation is needed
if calc_sublist2.length == 2
	puts "ANSWER: #{calc_sublist2[0]}"
elsif calc_sublist2.length > 2
	if calc_sublist2[-1] == "+"
		sum = 0
		for item in calc_sublist2[0...-1]
			sum += item
		end
		puts "ANSWER: #{sum}"
	elsif calc_sublist2[-1] == "-"
		diff = calc_sublist2[0]
		for item in calc_sublist2[1...-1]
			diff -= item
		end
		puts "ANSWER: #{diff}"
	elsif calc_sublist2[-1] == "*"
		prod = 1
		for item in calc_sublist2[0...-1]
			prod = prod * item
		end
		puts "ANSWER: #{prod}"
	elsif calc_sublist2[-1] == "/"
		quot = calc_sublist2[0]
		for item in calc_sublist2[1...-1]
			quot = quot/item
		end
		puts "ANSWER: #{quot}"
	elsif calc_sublist2[-1] == "**"
		exp = calc_sublist2[0]
		for item in calc_sublist2[1...-1]
			exp = exp ** item
		end
		puts "ANSWER: #{exp}"
	end
end











# # perform calculations
# if operator == "+"
# 	puts num1 + num2
# elsif operator == "-"
# 	puts num1 - num2
# elsif operator == "*"
# 	puts num1 * num2
# elsif operator == "/"
# 	puts num1 / num2
# else
# 	puts "I don't know"
# end


