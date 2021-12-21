# 1. Print string input backwards.

fun_string = input('Enter a word: ')
backwards = True
top_number = len(fun_string)
index_number = -1
backword = ''
while backwards is True:
    if top_number >= 1:
        backword += fun_string[index_number]
        top_number += -1
        index_number += -1
    else:
        backwards = False
        print(backword)


# # 2. Capitalize all words entered

# some_string = input('Enter some words: ')
# length_of_string = len(some_string)

# final_result = ''

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
    

# 3. Compressor

uncompressed_string = input('Enter a series of letters, some repeated: ')
index = 0
compressed_string = uncompressed_string[index]
string_length = len(uncompressed_string)
compressed_yet = False

while compressed_yet is False:
    index += 1
    if uncompressed_string[index] == compressed_string[-1]:
        compressed_string += uncompressed_string[index]
    # elif uncompressed_string[index] == compressed_string[-1]:
        # figure out how to add number and remove superfluous letters.

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

# if palindrome == emordnilap:
#     print('Congratulations, this is a palindrome!')
# else:
#     print('Failure! You do not understand the concept!')