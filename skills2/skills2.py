
string1 = "I do not like green eggs and ham."
list1 = [2, 5, 12, 6, 1, -5, 8, 5, 6, -2, 2, 27]
list2 = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
words = ["I", "do", "not", "like", "green", "eggs", "and", "ham", "I", "do", "not", "like", "them", "San", "I", "am"]

more_words = ['cat', 'dog', 'turtle', 'kangaroo']
more_words2 = ['cat', 'turtle', 'fish', 'peacock', 'elephant', 'lion']


# """
# Write a function that takes a string and produces a dictionary with
# all distinct elements as the keys, and the number of each element as
# the value
# Bonus: do the same for a file (i.e. twain.txt)
# """
# word_list = []
# word_count_dict = {}
# def count_unique(string1):
# 	word_list = string1.split()
# 	for word in word_list:
# 		if word_count_dict.get(word, "None") == "None":
# 			word_count_dict[word] = 1
# 		else:
# 			word_count_dict[word] += 1
# 	return word_count_dict

# word_list = count_unique(string1)
# print word_count_dict

	

# """
# Given two lists, (without using the keyword 'in' or the method 'index')
# return a list of all common items shared between both lists
# """
# full_list = []
# common_list = []

# def common_items(list1, list2):
#     full_list = list1 + list2
#     for item in full_list:
#     	if full_list.count(item) > 1:
#     		common_list.append(item)
#     for item in common_list:
#     	if common_list.count(item) > 1:
#     		common_list.remove(item)
#     for item in common_list:
#     	if common_list.count(item) > 1:
#     		common_list.remove(item)
#     return common_list

# common_items_list = common_items(list1, list2)
# print common_items_list

    



# """
# Given two lists, (without using the keyword 'in' or the method 'index')
# return a list of all common items shared between both lists. This time,
# use a dictionary as part of your solution.
# """
# def common_items2(list1, list2):
# 	common_dict = {}
# 	common_list = []
# 	for item in list1:
# 		common_dict[item] = list2

# 	for key, value in common_dict.iteritems():
# 		for i in range(0, len(list2)):
# 			if key == list2[i]:
# 				common_list.append(list2[i])
# 	return common_list

# common_items = common_items2(list1, list2)
# print common_items

# """
# Given a list of numbers, return list of number pairs that sum to zero
# """
# def sum_zero(list1):
#     sum_dict = {}
#     sum_list = []
#     for item in list1:
#     	sum_dict[item] = list1
#     print sum_dict

#     for k, v in sum_dict.iteritems():
#     	for i in range(0, len(list1)):
#     		if k == -1 * list1[i]:
#     			sum_list.append((k, list1[i]))

#     return sum_list


# sum_zero_list = sum_zero(list1)
# print sum_zero_list



# """
# Given a list of words, return a list of words with duplicates removed
# """
# def find_duplicates(words):
# 	unique_list = []
# 	duplicates_list = []
# 	for word in words:
# 		if word in unique_list:
# 			if word in duplicates_list:
# 				pass
# 			else:
# 				duplicates_list.append(word)
# 		else:
# 			unique_list.append(word)

# 	return duplicates_list

# duplicates = find_duplicates(words)
# print duplicates
   
# """
# Given a list of words, print the words in ascending order of length
# Bonus: do it on a file instead of the list provided
# Bonus: print the words in alphabetical order in ascending order of length
# """

# def word_length(words):
# 	word_length_dict = {}
# 	word_length_list = []
# 	for word in words:
# 		word_length_dict[word] = len(word)

# 	for i in range(1,len(word_length_dict)):
# 		for key, value in word_length_dict.iteritems():
# 			if word_length_dict[key] == i:
# 				word_length_list.append(key)
# 		i += 1

# 	return word_length_list

# word_length_list = word_length(words)
# print word_length_list


"""
Here's a table of English to Pirate translations
English     Pirate

sir         matey
hotel       fleabag inn
student     swabbie
boy         matey
madam       proud beauty
professor   foul blaggart
restaurant  galley
your        yer
excuse      arr
students    swabbies
are         be
lawyer      foul blaggart
the         th'
restroom    head
my          me
hello       avast
is          be
man         matey

Write a program that asks the user to type in a sentence and then
print the sentece translated to pirate.
"""
def main():

	input_sentence = raw_input("What would you like to translate? ")
	word_list = []


	def piratize(input_sentence):

		input_sentence.split()
		for i in range(0,):
			if input_sentence[i] == "sir":
				input_sentence[i] = "matey"
			if input_sentence[i] == "hotel":
				input_sentence[i] = "fleabag inn"
			if input_sentence[i] == "student":
				input_sentence[i] = "swabbie"
			if input_sentence[i] == "boy":
				input_sentence[i] = "matey"
			if input_sentence[i] == "madam":
				input_sentence[i] = "porud beauty"
			if input_sentence[i] == "professor":
				input_sentence[i] = "foul braggart"
			if input_sentence[i] == "retaurant":
				input_sentence[i] = "galley"
			if input_sentence[i] == "your":
				input_sentence[i] = "yer"
			if input_sentence[i] == "are":
				input_sentence[i] = "be"
			if input_sentence[i] == "the":
				input_sentence[i] = "th'"
			if input_sentence[i] == "my":
				input_sentence[i] = "me"
			if input_sentence[i] == "is":
				input_sentence[i] = "be"

		print input_sentence
		return input_sentence
	translation = piratize(input_sentence)
	print translation

if __name__ == "__main__":
	main()










