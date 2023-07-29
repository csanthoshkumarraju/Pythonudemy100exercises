# Pythonudemy100exercises

# **************************************
# problem 1 :- length of a string
# **************************************
# your_name = input('enter your name:--')
# your_string = input('enter your string:--')
# print('Length of your name is :-- ', len(your_name))
# print('Length of your string is :-- ', len(your_string))
# **************************************
# problem 2 :- index of a string
# **************************************
# your_string = input('enter your string:--')
# print('your string is :-- ', your_string)
# print('Length of your string is :-- ', len(your_string))
# your_index_number = int(input('enter your index number:--'))
# if len(your_string) == 0:
#     print('Empty String')
# elif len(your_string) < your_index_number:
#     print('your index number', your_index_number, 'of', your_string, ' is out of range')
# elif len(your_string) == your_index_number:
#     print('your index number', your_index_number, 'of', your_string, ' is out of range')
# elif len(your_string) > your_index_number:
#     print('The character of' + your_string + ' at ', your_index_number, ' is ', your_string[your_index_number])
# else:
#     print('Please give correct details')
# **************************************
# problem 3 :- reverse of a string
# **************************************
# your_string = input('enter your string:--')
# print('your string is :-- ', your_string)
# if len(your_string) == 0:
#     print('Length of your string', your_string, 'is :-- ', len(your_string))
#     print(your_string)
# else:
#     print('Reverse of your string ', your_string, 'is', your_string[::-1])

# a = 'hcbv'
# print("".join(reversed(a)))
# **************************************
# problem 4 :- first and last 3 characters of a string
# **************************************
# your_string = input('enter your string:--')
# print('your string is :-- ', your_string)
# print('Length of your string', your_string, 'is :-- ', len(your_string))
# len_gth = len(your_string)
# ind_ex = len_gth - 3
# if len(your_string) < 6:
#     print('')
#     print("Length of your string is less than 5")
# else:
#     print('first and last 3 characters of your string', your_string, 'is :-- ', your_string[0:3]+ your_string[ind_ex:])
# **************************************
# problem 5 :- even indices of a string
# **************************************
# your_string = input('enter your string:--')
# print('your string is :-- ', your_string)
# print('Length of your string', your_string, 'is :-- ', len(your_string))
# lent = len(your_string)
# if lent < 2:
#     print('Lengthy of your string is 0 or 1 :--', your_string)
# else:
#     print('The string', your_string, 'without the characters located at even indexes is :--', your_string[1:lent:2])
# **************************************
# problem 6 :- numbers contains in  a string
# **************************************
# your_string = input('enter your string:--')
# print('your string is :-- ', your_string)
# print('numbers contains in  a string ', your_string, ' :-- ', your_string.isdigit())
# **************************************
# problem 7 :- without characters at index in  a string
# **************************************
# your_string = input('enter your string:--')
# print('your string is :-- ', your_string)
# print('Length of your string is :-- ', len(your_string))
# your_index_number = int(input('enter your index number:--'))
# print('your index number is :--', your_index_number)
# if len(your_string) == 0:
#      print('Empty String')
#      print('your string is :-- ', your_string)
# elif len(your_string) < your_index_number:
#     print('your index number', your_index_number, 'of', your_string, ' is out of range')
#     print('your string is :-- ', your_string)
# elif len(your_string) == your_index_number:
#     print('your index number', your_index_number, 'of', your_string, ' is out of range')
#     print('your string is :-- ', your_string)
# elif len(your_string) > your_index_number:
#      ind = your_string[your_index_number]
#      # remo = your_string.replace(ind, "")
#      remo = your_string[:your_index_number] + your_string[your_index_number+1:]
#      print('without characters at index', your_index_number, 'in  a string ', your_string, ' is:--', remo)
# else:
#     print('Please give correct details')
# **************************************
# problem 8 :- without characters at index in  a string
# **************************************
# your_string = input('enter your string:--')
# if len(your_string) == 0:
#     print('your string is empty')
# print('your string is :-- ', your_string)
# curr_char = input('enter a current character from your_string which need to be replaced:--')
# print('your curr_char from your_string', your_string, 'is :-- ', curr_char)
# new_char = input('enter a new character for your_string to replace with:--')
# print('your new_char replacing to the string', your_string, 'is :-- ', new_char)
# if len(new_char) == 0:
#     print('new character for your_string to replace is empty')
# elif curr_char not in your_string:
#     print(your_string)
# else:
#     remo = your_string.replace(curr_char, new_char)
#     print('Your replaced string from:-- ', your_string, ' to:-- ', remo, ' by replacing ', 'current character :--', curr_char, 'with new character', new_char, 'is:--', remo)

# **************************************
# problem 9 :- Replace , with . from a string
# **************************************
# your_string = input('enter your string:--')
# print('your string is :-- ', your_string)
# remo = your_string.replace(',', '.')
# print('your replaced string from , to . is :--', remo)

# **************************************
# problem 9 :- Replace , with .
# **************************************
# import string
# your_string = input('enter your string:--')
# print('your string is :-- ', your_string)
# lower_case = set(your_string.lower())
# lower_case.remove(" ")
# print(lower_case == set(string.ascii_lowercase))
# **************************************
# problem 9 :- Removing spaces
# **************************************
# your_string = input('enter your string:--')
# print('your string is :-- ', your_string)
# new_str = ''
# for char in your_string:
#     if char != " ":
#         new_str += char
# print('spaces removed string is ', new_str)

# **************************************
# problem 10 :- finding a matching in string prefix
# **************************************

# your_string = input('enter your string:--')
# print('your string is :-- ', your_string)
# prefix = input('enter your prefix string:--')
# print('your prefix string is :-- ', prefix)
# print(your_string[:len(prefix)] == prefix)

# **************************************
# problem 11 :- finding a matching in string suffix
# **************************************
# your_string = input('enter your string:--')
# print('your string is :-- ', your_string)
# suffix = input('enter your prefix string:--')
# print('your prefix string is :-- ', suffix)
# print(your_string[-len(suffix):] == suffix)


