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
# problem 10 :- Replace , with .
# **************************************
# import string
# your_string = input('enter your string:--')
# print('your string is :-- ', your_string)
# lower_case = set(your_string.lower())
# lower_case.remove(" ")
# print(lower_case == set(string.ascii_lowercase))
# **************************************
# problem 11 :- Removing spaces
# **************************************
# your_string = input('enter your string:--')
# print('your string is :-- ', your_string)
# new_str = ''
# for char in your_string:
#     if char != " ":
#         new_str += char
# print('spaces removed string is ', new_str)

# **************************************
# problem 12 :- finding a matching in string prefix
# **************************************

# your_string = input('enter your string:--')
# print('your string is :-- ', your_string)
# prefix = input('enter your prefix string:--')
# print('your prefix string is :-- ', prefix)
# print(your_string[:len(prefix)] == prefix)

# **************************************
# problem 13 :- finding a matching in string suffix
# **************************************
# your_string = input('enter your string:--')
# print('your string is :-- ', your_string)
# suffix = input('enter your prefix string:--')
# print('your prefix string is :-- ', suffix)
# print(your_string[-len(suffix):] == suffix)

# **************************************
# problem 14 :- reversing words in string
# **************************************

# your_string = input('enter your string:--')
# print('your string is :-- ', your_string)
# words_list = your_string.split(' ')
# new_string = ''
# for word in words_list:
#     reversed_word = ''.join(reversed(word))
#     swapped_case = reversed_word.swapcase()
#     new_string += swapped_case + ' '
# new_string.rstrip()
# print(new_string)

# **************************************
# problem 15 :- printing the count of repeated characters.
# **************************************

# your_string = input('enter your string:--')
# print('your string is :-- ', your_string)
#
# repeated_count = 0
# repeated_chars = []
# for char in your_string:
#     if (your_string.count(char) > 1) and (char not in repeated_chars):
#         repeated_count += 1
#         repeated_chars.append(char)
#
# print(repeated_count)
# rep_char = (' '.join(repeated_chars))
# print(rep_char)

# **************************************
# problem 16 :- convert a string to lower case and sort in alphabetical
# **************************************

# your_string = input('enter your string:--')
# print('your string is :-- ', your_string)
# words_list = your_string.split(' ')
# print('wors in yor sting are:--', words_list)
# new_string = ''
# for word in words_list:
#     sorted_word = ''.join(sorted(word))
#     print('sorted:--', sorted_word)
#     new_string += sorted_word + ' '
# new_string.rstrip()
# print(new_string.lower())

# **************************************
# problem 17 :- lists multiplying values
# **************************************
# your_list = [1, 2, 3]
# factor = 2
# print('your list is :-- ', your_list)
# for i in range(len(your_list)):
#     your_list[i] *= factor
# print(your_list)

# **************************************
# problem 18 :-removing spaces and ,
# **************************************

# l = [1, 2, 3, 4]
# result = ''
# for num in l:
#     result += str(num)
# print(' '.join(result))

# **************************************
# problem 19 :- largest and smalles values in list
# **************************************
# lis = [3, 4, 5, 6]
# print(max(lis), min(lis))

# **************************************
# problem 20 :- check if the string is empty or not
# **************************************

# lis = []
# if len(lis) == 0:
#     print('Empty')
# else:
#     print('Not Empty')
#     print(lis)

# **************************************
# problem 21 :- printing values and indices
# **************************************
# lis = [1, 2, 3, 4]
# if len(lis) == 0:
#     print('empty string ')
# for i,elem in enumerate(lis):
#     print(elem, i)
# **************************************
# problem 22 :- Removing a element from list
# **************************************

# lis = ['a','b','c','d','a']
# print('here is your list :-- ',lis)
# element_to_remove = 'a'
# print('you are removing ', element_to_remove, ' element from list')
# print(lis)
# if len(lis) == 0:
#     print('empty')
# elif element_to_remove not in lis:
#     print(' element to remove is not available in list')
# else:
#     for i in range(lis.count(element_to_remove)):
#      lis.remove(element_to_remove)
#     print(lis)

# **************************************
# problem 23 :- removing duplicates
# **************************************

# lis = [1,2,3,4,1,2,3,4]
# no_dup = list(dict.fromkeys(lis))
# print(no_dup)

# **************************************
# problem 24 :- count the values graeter than 3
# **************************************

# lis = [1,2,3,4,5,6]
# count = 0
# for i in lis:
#     if i > 3:
#         count += 1
# print(count)

# **************************************
# problem 25 :- intersection of sets
# **************************************

# s1 = {1,2,3,4,5,6,7,8,9,10}
# s2 = {2,5,6,11,13,14,12}
# s3 = s1.intersection(s2)
# print(s3)

# **************************************
# problem 26 :- lista - list b
# **************************************
# l1 = [1,2,3,4,5,6,7,8,9,10]
# l2 = [2,5,6,11,13,14,12]
# print(set(l1) - set(l2))

# **************************************
# problem 27 :-  distance between co-ordinates in x and y
# **************************************
# x = [-3, -4, -5]
# y = [2, 0, -4]
# xd = {'a': x[0], 'b': x[1], 'c': x[2]}
# yd = {'d': y[0], 'e': y[1], 'f': y[2]}
# AB = (((yd['d'] - xd['a']) ** 2) + ((yd['e'] - xd['b']) ** 2) + ((yd['f'] - xd['c']) ** 2)) ** 0.5
# print(float(AB))

# **************************************
# problem 28 :-  intersection of lists
# **************************************

# l1 = [4,5,6]
# l2 = [1,2,3]
# l3 = set(l1).intersection(set(l2))
# print(list(l3))

# **************************************
# problem 29 :-  second largest value in list
# **************************************

# lis = [1,0.5]
# if len(lis) > 1 :
#     first_largest = max(lis)
#     lis.remove(first_largest)
#     print(max(lis))
# else:
#     print('none')

# **************************************
# problem 30 :-  second smallest value in list
# **************************************
# lis = [1,2,3,4]
# if len(lis) > 1 :
#     first_largest = min(lis)
#     lis.remove(first_largest)
#     print(min(lis))
# else:
#     print('none')

# **************************************
# problem 31 :-  count frequency of elements in list
# **************************************

# lis = [1,2,3,3,4,4,5,5,5,6,6,7,8]
# freq_dict = {}
# for elem in lis:
#     if elem not in freq_dict:
#         freq_dict[elem] = 1
#     else:
#         freq_dict[elem] += 1
# print(freq_dict)

# **************************************
# problem 32 :-  flattened or concatenating lists into single
# **************************************

# l = [[1,2,3],4,5,6,[7,8,9]]
# flat_list = []
# for elem in l:
#     if isinstance(elem, list):
#         for nested_elem in elem:
#             flat_list.append(nested_elem)
#     else:
#         flat_list.append(elem)
# print(flat_list)

# **************************************
# problem 33 :-  permutation of a list
# **************************************

# import itertools
# lis = [1,2,3,4]
# permutations = list(itertools.permutations(lis))
# for permutations in permutations:
#     print(permutations)

# **************************************
# problem 34 :-  dict keys present
# **************************************

# dictionary = {'a': 1, 'b': 2, 'c': 3}
# key1 = 'a'
# if key1 in dictionary:
#     print('True')
# else:
#     print('False')

# **************************************
# problem 35 :- updating dictionary
# **************************************

# dictionary = {'January': 45, 'February': 56, 'March': 67}
# dictionary1 = {'January': 67}
# n= dictionary.keys()
# for i in dictionary1.keys():
#     if i in dictionary:
#         print(dictionary)
#     else:
#         dictionary.update(dictionary1)
#         print(dictionary)
#         print('the key value exists in the dictionary')

# **************************************
# problem 36 :- merge or concatenate two dictionaries
# **************************************

# dict1 = {'January': 45, 'February': 56, 'March': 67}
# dict2 = {'April': 23, 'May': 57, 'June': 62}
# dict1.update(dict2)
# print(dict1)

# **************************************
# problem 37 :- checks values i dictionary are equal
# **************************************

# dictionary = {'a': 1, 'b': 1, 'c': 1}
# val = len(set(dictionary.values()))
# set does not allow duplicates.
# if val == 0:
#     print('Empty')
# elif val == 1:
#     print('True')
# else:
#     print('False')

# **************************************
# problem 38 :- largest value in dictionary
# **************************************

# dictionary = {'a': 1, 'b': 2, 'c': 3}
# if len(dictionary) == 0:
#     print('Dictionary is empty')
# else:
#     print(max(dictionary.values()))

# **************************************
# problem 39 :- smallest value in dictionary
# **************************************

# dictionary = {'a': 1, 'b': 2, 'c': 3}
# if len(dictionary) == 0:
#     print('Dictionary is empty')
# else:
#     print(min(dictionary.values()))

# **************************************
# problem 40 :- count of values in dictionary
# **************************************
# dict1 = {'a': 4, 'b': 4, 'c': 2,'d': 7, 'e': 4, 'f': 2,'g': 7, 'h': 7}
# freq_dict = {}
# cou = dict1.values()
# for elem in cou:
#     if elem not in freq_dict:
#         freq_dict[elem] = 1
#     else:
#         freq_dict[elem] += 1
# print(freq_dict)

# **************************************
# problem 41 :-nested dictionaries into a single dictionary
# **************************************

# l = [['a',1],['b',2],['c',3],['d',4]]
# print(dict(l))

# **************************************
# problem 42 :-max value from sum of dict values in a list
# **************************************
# my_dicti = {'a': [1,2,3],'b': [4,0,-4],'c': [3,5,9],'d': [45,12,100]}
# sov = [sum(my_dicti['a']),sum(my_dicti['b']),sum(my_dicti['c']),sum(my_dicti['d'])]
# print(max(sov))

# **************************************
# problem 43 :- count of values in strings by mapping to a dictionary
# **************************************

# stri_ng = 'Excellent'
# freq_dict = {}
# for elem in stri_ng.lower():
#     if elem.isalpha():
#         if elem not in freq_dict:
#             freq_dict[elem] = 1
#         else:
#             freq_dict[elem] += 1
# print(freq_dict)

# **************************************
# problem 44 :- sorting list values in dictionary
# **************************************

# d = {'a': [4,3,2],'b': [5,3,7],'c': [1,9,10],'d': [3,4,1]}
# for list_value in d.values():
#     list_value.sort()
# print(d)

# **************************************
# problem 45 :- dictionary key values to lists
# **************************************

# d = {'a': 1, 'b':2, 'c':3}
# new_list = []
# for key, value in d.items():
#     new_list.append([key,value])
# print(new_list)

# **************************************
# problem 46 :- ckeck positive/negative/zero
# **************************************

# a = int(input('enter a number'))
# if a == 0:
#     print('Zero ', 0)
# elif a % 2 == 0:
#     print('Even')
# else:
#     print('odd')

# **************************************
# problem 47 :- print vowel consonants in a string
# **************************************


# s = 'Rank : 1'
# if len(s) == 0:
#     print('empty string')
# else:
#     for char in s.lower():
#         if char in ('a','e','i','o','u'):
#             print(f"{char} is a vowel")
#         elif not char.isalpha():
#             print(f"{char} is a not a letter")
#         else:
#             print(f"{char} is a consonant")

# **************************************
# problem 48 :- max of three numbers
# **************************************

# s = (1,2,3)
# print(max(s))
# a = 17
# b = 8
# c = 6
#
# se = (a,b,c)
# print(max(se))
# if a > b and a > c:
#     print(a)
# elif b > c and b > a:
#     print(b)
# else:
#     print(c)

# **************************************
# problem 49 :- min of three numbers
# **************************************

# s = (1,2,3)
# print(min(s))
# a = 1
# b = 0
# c = 6
#
# se = (a,b,c)
# print(min(se))
# if a < b and a < c:
#     print(a)
# elif b < c and b < a:
#     print(b)
# else:
#     print(c)

# **************************************
# problem 50 :- seasons
# **************************************

# print({'season_num':'season'})
# print({1:'spring'})
# print({2:'summer'})
# print({3:'fall'})
# print({4:'winter'})
#
# enter_your_season_number = int(input('enter_your_season_number:--'))
# print('enter_your_season_number is :-- ',enter_your_season_number)
# if enter_your_season_number == 1:
#     print('your enter_your_season_number season is :-- spring')
# elif enter_your_season_number == 2:
#     print('your enter_your_season_number season is :-- summer')
# elif enter_your_season_number == 3:
#     print('your enter_your_season_number season is :-- fall')
# elif enter_your_season_number == 4:
#     print('your enter_your_season_number season is :-- winter')
# else:
#     print('please enter a valid number')

# **************************************
# problem 51 :- if all are equal
# **************************************
# a=1
# b=1
# c=1
# s = (a,b,c)
# if a == b == c:
#     print(s)
#     print('Equal')
# else:
#     print(s)
#     print('Not Equal')

