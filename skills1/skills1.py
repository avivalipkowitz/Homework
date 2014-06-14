# Things you should be able to do.

num_list = [1,2,3,4,5,6,7,8,9,10,11,12]
animals = ['cat', 'dog', 'turtle', 'elephant', 'hippo']



# Write a function that takes a list and returns a new list with only the odd numbers.
# DONE

# def all_odd(some_list):
    
#     return some_list[::2]


# odd_list = all_odd(num_list)
# print odd_list

# odd_list = all_odd(animals)
# print odd_list

# # Write a function that takes a list and returns a new list with only the even numbers.
# DONE 
# def all_even(some_list):
#      return some_list[1::2]

# even_list = all_even(num_list)
# print even_list

# even_list = all_even(animals)
# print even_list


# # Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
# # DONE
# def long_words(word_list):
#     long_words_list = []
    
#     for word in word_list:
#         word_length = len(word)
#         if word_length >= 4:
#             long_words_list.append(word)
#     return long_words_list

# long_words_list = long_words(animals)
# print long_words_list

# # Write a function that finds the smallest element in a list of integers and returns it.
# # DONE
# def smallest(some_list):
#     some_list.sort()
#     return some_list[0]
     
# smallest_int = smallest(num_list)
# print smallest_int


# # Write a function that finds the largest element in a list of integers and returns it.
# def largest(some_list):
#     some_list.sort()
#     return some_list[-1]

# biggest_int = largest(num_list)
# print biggest_int
     

# # Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
# DONE
# new_list = []

# def halvesies(some_list):
#     for num in some_list:
#         num = (num/2.0)
#         new_list.append(num)
#     return new_list

# halvesies_list = halvesies(num_list)
#print halvesies(num_list)


# # Write a function that takes a list of words and returns a list of all the lengths of those words.
# DONE!!!!!

# word_length_list = []
# def word_lengths(word_list):
#     for word in word_list:
#         word.split()
#         word_length = len(word)
#         word_length_list.append(word_length)
#     return word_length_list

# lengths = word_lengths(animals)
# print lengths



# # Write a function (using iteration) that sums all the numbers in a list.
# DONE!!!

# def sum_numbers(numbers):
#     sum_of_numbers = 0
#     for num in numbers:
#         sum_of_numbers = sum_of_numbers + num
#     return sum_of_numbers

# total_sum = sum_numbers(num_list)
# print total_sum



# # Write a function that multiplies all the numbers in a list together.
# DONE

# def mult_numbers(numbers):
#     prod_of_numbers = 1
#     for num in numbers:
#         prod_of_numbers = prod_of_numbers * num
#     return prod_of_numbers

# total_prod = mult_numbers(num_list)
# print total_prod

# # Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
# DONE

# def join_strings(string_list):
#     joined_string = ""
#     for word in string_list:
#         joined_string = joined_string + word
#     return joined_string

# final_joined_string = join_strings(animals)
# print final_joined_string

# # Write a function that takes a list of integers and returns the average (without using the avg method)
# DONE!

# def average(numbers):
#     num_sum = 0
#     for num in numbers:
#         num_sum = num_sum + num
#     num_av = num_sum/(len(numbers))

#     return num_av
 
# number_average = average(num_list)
# print number_average
