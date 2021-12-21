# Worksheet One
# 1. Print string input backwards.

fun_string = input('Enter a word: ')
backwards = True
top_number = len(fun_string)
index_number = -1
backword = ''

# The while loop starts at the last index number and adds each backward successive letter to 'backword'
# until it runs out of letters.

while backwards is True:
    if top_number >= 1:
        backword += fun_string[index_number]
        top_number += -1
        index_number += -1
    else:
        backwards = False
        print(backword)


# 2. Capitalize all words entered

some_string = input('Enter some words all lowercase: ')
length_of_string = len(some_string)

final_result = ''

# This for loop starts at the beginning of the user input, automatically capitalizing the first letter and then
# looks for a space before a letter in the string to capitalize the letter after the space.

for index in range(length_of_string):
    if index == 0:
        final_result += some_string[index].capitalize()
    elif index >= 1 and some_string[index - 1] == ' ':
        final_result += some_string[index].capitalize()
    elif index >= 1 and some_string[index] != ' ':
        final_result += some_string[index]
    elif index >= 1 and some_string[index] == ' ':
        final_result += some_string[index]
       
print(final_result)
    

# 3. Compressor

uncompressed_string = input('Enter a series of letters, some repeated: ')
index = 0
compressed_string = uncompressed_string[index]
final_compressed = ''
string_length = len(uncompressed_string)
compressed_yet = False

# The while loop starts at the zero index and keeps comparing letters and puts any that are the same into
# 'compressed_string'. Once it hits a new kind of letter it takes the string length of 'compressed string',
# turns it into a string number and concatenates the number with one letter from 'compressed_string'. Then 
# that is put into 'final_compressed'. If there is only one letter, it will concatenate the one letter without
# a number to 'final_compressed'. It keeps going down the line until the input is exhausted.

while compressed_yet is False:
    index += 1
    if index == len(uncompressed_string):
        final_compressed += str(len(compressed_string)) + compressed_string[0] 
        compressed_string = ''
        compressed_yet = True
    elif uncompressed_string[index] == compressed_string[-1]:
        compressed_string += uncompressed_string[index]
    elif uncompressed_string[index] != compressed_string[-1] and len(compressed_string) == 1:
        final_compressed += compressed_string[0] 
        compressed_string = ''
        compressed_string += uncompressed_string[index]
    elif uncompressed_string[index] != compressed_string[-1]:
        final_compressed += str(len(compressed_string)) + compressed_string[0] 
        compressed_string = ''
        compressed_string += uncompressed_string[index]

print(final_compressed)
        

# 4. Palindrome Checker

palindrome = input('Enter a word a word you believe to be a palindrome: ')
backwards = True
top_number = len(palindrome)
index_number = -1
emordnilap = ''
while backwards is True:
    if top_number >= 1:
        emordnilap += palindrome[index_number]
        top_number += -1
        index_number += -1
    else:
        backwards = False
        print(emordnilap)

# The logic above is exactly the same as making a string backwards. The below logic checks to see if it's a palindrome.

if palindrome == emordnilap:
    print('Congratulations, this is a palindrome!')
else:
    print('Failure! You do not understand the concept!')