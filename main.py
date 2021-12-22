# # Worksheet One
# # 1. Print string input backwards.

# fun_string = input('Enter a word: ')
# backwards = True
# top_number = len(fun_string)
# index_number = -1
# backword = ''

# # The while loop starts at the last index number and adds each backward successive letter to 'backword'
# # until it runs out of letters.

# while backwards is True:
#     if top_number >= 1:
#         backword += fun_string[index_number]
#         top_number += -1
#         index_number += -1
#     else:
#         backwards = False
#         print(backword)


# # 2. Capitalize all words entered

# some_string = input('Enter some words all lowercase: ')
# length_of_string = len(some_string)

# final_result = ''

# # This for loop starts at the beginning of the user input, automatically capitalizing the first letter and then
# # looks for a space before a letter in the string to capitalize the letter after the space.

# for index in range(length_of_string):
#     if index == 0:
#         final_result += some_string[index].capitalize()
#     elif index >= 1 and some_string[index - 1] == ' ':
#         final_result += some_string[index].capitalize()
#     elif index >= 1 and some_string[index] != ' ':
#         final_result += some_string[index]
#     elif index >= 1 and some_string[index] == ' ':
#         final_result += some_string[index]
       
# print(final_result)
    

# # 3. Compressor

# uncompressed_string = input('Enter a series of letters, some repeated: ')
# index = 0
# compressed_string = uncompressed_string[index]
# final_compressed = ''
# string_length = len(uncompressed_string)
# compressed_yet = False

# # The while loop starts at the zero index and keeps comparing letters and puts any that are the same into
# # 'compressed_string'. Once it hits a new kind of letter it takes the string length of 'compressed string',
# # turns it into a string number and concatenates the number with one letter from 'compressed_string'. Then 
# # that is put into 'final_compressed'. If there is only one letter, it will concatenate the one letter without
# # a number to 'final_compressed'. It keeps going down the line until the input is exhausted.

# while compressed_yet is False:
#     index += 1
#     if index == len(uncompressed_string):
#         final_compressed += str(len(compressed_string)) + compressed_string[0] 
#         compressed_string = ''
#         compressed_yet = True
#     elif uncompressed_string[index] == compressed_string[-1]:
#         compressed_string += uncompressed_string[index]
#     elif uncompressed_string[index] != compressed_string[-1] and len(compressed_string) == 1:
#         final_compressed += compressed_string[0] 
#         compressed_string = ''
#         compressed_string += uncompressed_string[index]
#     elif uncompressed_string[index] != compressed_string[-1]:
#         final_compressed += str(len(compressed_string)) + compressed_string[0] 
#         compressed_string = ''
#         compressed_string += uncompressed_string[index]

# print(final_compressed)
        

# # 4. Palindrome Checker

# palindrome = input('Enter a word a word you believe to be a palindrome: ')
# backwards = True
# top_number = len(palindrome)
# index_number = -1
# emordnilap = ''
# while backwards is True:
#     if top_number >= 1:
#         emordnilap += palindrome[index_number]
#         top_number += -1
#         index_number += -1
#     else:
#         backwards = False
#         print(emordnilap)

# # The logic above is exactly the same as making a string backwards. The below logic checks to see if it's a palindrome.

# if palindrome == emordnilap:
#     print('Congratulations, this is a palindrome!')
# else:
#     print('Failure! You do not understand the concept!')


# # Worksheet Two

# # 1. Happy Numbers

# user_happy_input = input('Please enter any number: ')
# original_input = user_happy_input
# is_happy_or_no = False
# happy_or_sad = int(user_happy_input)

# # The while loop checks to see if an entered number is a happy number. If the sum of the squares of each digit equal 1,
# # the number is considered happy. If the number loops around (as far as I know always hitting 4 at some point), it is 
# # considered a sad number. 
# # This code puts the answers to the exponents in a list, then adds the list together and repeats until a 1 or 4 is hit.

# while is_happy_or_no is False:
#     index = 0
#     new_number_list = []
#     if happy_or_sad == 1:
#         is_happy_or_no = True
#         print(f'{original_input} is a happy number!')
#     elif happy_or_sad >= 10:
#         for number in user_happy_input:
#             equation = (int(user_happy_input[index]) * int(user_happy_input[index]))
#             index += 1
#             new_number_list.append(equation)
#         happy_or_sad = 0
#         index = 0
#         for number in new_number_list:
#             happy_or_sad += new_number_list[index]
#             index += 1
#         user_happy_input = str(happy_or_sad)
#     elif user_happy_input == '4':
#         is_happy_or_no = True
#         print(f'{original_input} is a sad number...')
#     elif len(user_happy_input) == 1 and happy_or_sad != 1:
#         index = 0
#         happy_or_sad = (int(user_happy_input[index]) * int(user_happy_input[index]))
#         user_happy_input = str(happy_or_sad)


# # 2 Prime Numbers 1 - 100

# # Used simple moduluses to find primes larger than 10 and hardcoded the primes less than 10.

# for number in range(1, 101):
#     if number < 10 and (number == 2 or number == 3 or number == 5 or number == 7):
#         print(number)
#     elif number >= 10 and (number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0):
#         continue
#     elif number >= 10 and (number % 2 != 0 or number % 3 != 0 or number % 5 != 0 or number % 7 != 0):
#         print(number)
        







