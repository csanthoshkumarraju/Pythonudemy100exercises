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
import math

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

# **************************************
# problem 52 :- days in a months
# **************************************

# month = 'February'
# month_31d = ('January','March','May','July','August','october','December')
# month_30_days = ('April','June','September','November')
# if month in month_31d:
#     print(f"{month} has :-- 31 days")
# elif month in month_30_days:
#     print(f"{month} has :-- 30 days")
# elif month == 'February':
#     print(print(f"{month} has :-- 28 days"))
# else:
#     print('please give name of a month')

# **************************************
# problem 53 :- incraesing or decreasing order
# **************************************
# a = 5
# b = 2
# c = 3
# print(a,b,c)
# if a > b > c :
#     print('Decreasing order')
# elif a < b < c :
#     print('Increasing order')
# else:
#     print('none')

# **************************************
# problem 54 :- quadratic equation
# **************************************
# import math
# a= 3
# b= 4
# c= 5
#
# descr = b**2 - 4*a*c
# if descr < 0:
#     print('complex roots')
# elif descr == 0:
#     r = -b/(2*a)
#     print(2)
# else:
#     r1 = (-b - math.sqrt(descr))/(2*a)
#     r2 = (-b + math.sqrt(descr))/(2*a)
#     print(r1, r2)

# **************************************
# problem 55 :- leap year
# **************************************

# year = int(input('enter your year:--'))
# if year % 4 == 0:
#     print(year,'is a leap year')
# else:
#     print(year,'is Not a leap year')

# **************************************
# problem 56 :- calculator
# **************************************

# v1 = int(input('Please enter the first value: - '))
# v2 = int(input('Please enter the first value: - '))
# print('Great! Now enter the operation')
# print( ' these are the available options')
# print('1 - Addition')
# print('2 - Subtraction')
# print('3 - Multiplication')
# print('4 - Division')
# print('5 - Integer division')
# print('6 - Modulo/remainder')
# operation = int(input('enter a operator number :--'))
# if operation == 1:
#     print(v1, ' + ', v2, '=', v1+v2)
# elif operation == 2:
#     print(v1, ' - ', v2, '=', v1-v2)
# elif operation == 3:
#     print(v1, ' * ', v2, '=', v1*v2)
# elif operation == 4:
#     print(v1, ' / ', v2, '=', v1/v2)
# elif operation == 5:
#     print(v1, ' ** ', v2, '=', v1**v2)
# elif operation == 6:
#     print(v1, ' // ', v2, '=', v1//v2)
# elif operation == 7:
#     print(v1, ' % ', v2, '=', v1%v2)
# else:
#     print('please enter a valid operator')
#
# **************************************
# problem 57 :- rock scissors paper game
# **************************************
# import random
# game = ['Paper','Rock','Scissors']
# computer = game[random.randint(0, 2)]
# print('===========welcome to the game=============')
# print('please enter Rock,Paper, or Scissors below')
# your_choice = input('enter a value from Rock,Paper, or Scissors')
# print(your_choice)
# print('computer choice :--',computer)
# if computer.lower() == your_choice.lower:
#     print('tie please try again')
# elif computer == 'Rock':
#     print('you lose! computer won please try again')
# else:
#     print('Congrats You WON')

# **************************************
# problem 58 :- first positive 15 integers
# **************************************
# i = 1
# for i in range(i, 16):
#     print(i)

# **************************************
# problem 59 :- reverse of number
# **************************************

# n = int(input('enter a number'))
# for i in range(n,0,-1):
#     print(i)

# **************************************
# problem 60 :- print sum of first non - negative numbers
# **************************************

# sum_of_first_numbers = int(input(' enter a value sum_of_first_numbers'))
# print('your value is :--' ,sum_of_first_numbers)
# sum_of_values = (sum_of_first_numbers/2) * (1 + sum_of_first_numbers)
# print('sum of first of your value is:--')
# print(int(sum_of_values))
#
# **************************************
# problem 61 :- multiplication table
# **************************************
# num = int(input('enter a number for your multiplication table'))
# i = int(input('enter times of your number value :--'))
# for a in range(0,i + 1):
#     print(num, ' * ', a, ' = ', num * a)

# **************************************
# problem 62 :- alphabetical order
# **************************************
# for i in range(65,91):
#     print(chr(i))
#
# **************************************
# problem 63 :- print first 1 st 100 even numbers
# **************************************
# n = int(input('enter the first count of even numbers'))
# print('the first ', n, ' even numbers are:--')
# for i in range(1, n+1):
#     print(i * 2)

# **************************************
# problem 64 :- factorial
# **************************************
# i = int(input('enter a number for your factorial :--'))
# factorial= 1
# for i in range(2,i+1):
#     factorial *= i
# print(factorial)

# **************************************
# problem 65 :- prime number
# **************************************
# pn = int(input('enter your number:--'))
# if pn == 1 or pn == 0:
#     print(pn, 'is not a prime number')
# elif pn == 2:
#     print(pn, 'is a prime number')
# else:
#     for i in range(2,pn):
#         if pn % i == 0:
#             print(pn, 'is not a prime number')
#             break
#     else:
#         print(pn, 'is a prime number')

# **************************************
# problem 66 :- print a pattern
# **************************************
# n = int(input('enter your number'))
# for i in range(1,n+1):
#     print ('*' * i)

# **************************************
# problem 67 :- reverse of a digit
# **************************************

# d = int(input('enter your digit:--'))
# print('Your digit is :--', d)
# st = str(d)
# print('Reverse digit of your number is :--', st[::-1])

# **************************************
# problem 68 :- reverse of a string
# **************************************

# st =input('enter your string:--')
# print('Your string is :--', st)
# print('Reverse digit of your number is :--', st[::-1])

# **************************************
# problem 69 :- half pyramid
# **************************************
# num_rows = int(input('enter the number of rows:--'))
# k = (2 * num_rows) - 2
# for i in range(0,num_rows):
#     for j in range(0, k):
#         print('', end=' ')
#     k = k -2
#     for j in range(0, i+1):
#         print('*', end=' ')
#     print('')

# **************************************
# problem 70 :- floyd's triangle
# **************************************

# num_rows = int(input('enter the number of rows:--'))
# count = 1
# for i in range(1,num_rows +1):
#     for j in range(0, i):
#         print(count, end=' ')
#         count += 1
#     print()

# **************************************
# problem 71 :- triangular letters pattern
# **************************************

# num_rows = int(input('enter the number of rows:--'))
# for i in range(0,num_rows):
#     print(chr(65 + i) * (i + 1))

# **************************************
# problem 72 :- diamond
# **************************************

# height = int(input('enter the diamonds height (an odd number)'))
# if height % 2 ==0:
#     print('please enter an odd value for the height (number of rows')
# else:
#     middle_rows = (height + 2) // 2
#     for i in range(middle_rows):
#         print(' ' * (middle_rows - i), '*' * (i*2 + 1))
#     for i in range(middle_rows-2,-1,-1):
#         print(' ' * (middle_rows - i), '*' * (i*2 + 1))

# **************************************
# problem 73 :- sum of a list
# **************************************

# l = [1,2,3,4]
# print(sum(l))

# **************************************
# problem 74 :- financial number
# **************************************

# def fibonacci(n):
#     if n == 0 or n ==1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# v = fibonacci(9)
# print(v)
# **************************************
# problem 75 :- factorial
# **************************************
# i = int(input('enter a number for your factorial :--'))
# factorial= 1
# for i in range(2,i+1):
#     factorial *= i
# print(factorial)

# **************************************
# problem 76 :- sum of a digit in i a digit
# **************************************
# def sum_of_digits(number):
#     if number == 0:
#         return 0
#     else:
#         return (number%10) + sum_of_digits(number // 10)
# print(sum_of_digits(12))

# **************************************
# problem 77 :- power of a number
# **************************************
# a = int(input('enter your number'))
# b = int(input('enter your power/times for number number'))
# print(a ** b)

# **************************************
# problem 78 :-  gcd
# **************************************
# def find_gcd(a,b):
#     if b == 0:
#         return a
#     else:
#         return find_gcd(b, a%b)
# print(find_gcd(60,48))

# **************************************
# problem 79 :-  palindrome
# **************************************
# string = input('enter your string')
# print('your string is :--',string)
# rev = string[::-1]
# print('reverse of your string is :--',rev)
# if string.lower() == rev.lower():
#     print(string, 'is a palindrome')
# else:
#     print(string, 'is not a palindrome')

# **************************************
# problem 80 :-  vowels in a string
# **************************************

# def count_vowels(string):
#     string = string.lower()
#
#     if not string:
#         return 0
#     elif string[0] in ('a','e','i','o','u'):
#         return 1+ count_vowels(string[1:])
#     else:
#         return count_vowels(string[1:])
# print(count_vowels('aeioubchjmdshjfbsh'))

# **************************************
# problem 81 :- pattern
# **************************************

# def patt(n):
#     if n==1:
#         print('*')
#     else:
#         print('*' * n)
#         patt(n -1)
# print(patt(9))
# **************************************
# problem 82 :- int to binary
# **************************************
# def int_bin(decnum):
#     if decnum ==0:
#         return '0'
#     else:
#         return (int_bin(decnum // 2)+str(decnum%2)).lstrip('0')
# print(int_bin(12))

# **************************************
# problem 83 :- binary search
# **************************************

# def bns(seq,low,high,elem):
#     if low > high:
#         return -1
#     else:
#         middle = (low + high) // 2
#         if elem == seq[middle]:
#             return middle
#         elif elem < seq[middle]:
#             return bns(seq,low,middle - 1 ,elem)
#         else:
#             return bns(seq,middle + 1,high,elem)
# print(bns(1,2,3,4))

# **************************************
# problem 84 :- read text a file
# **************************************
# python file is created in next tab.
# filer = "pythonfiles.txt"
# file_content =[]
# with open(filer) as file:
#     for line in file:
#         file_content.append(line)
# print(file_content)

# **************************************
# problem 85 :- print the first n lines
# **************************************

# file_path = "pythonfiles.txt"
# n = int(input('how many lines would you like to read:'))
# with open(file_path) as file:
#     lines = file.readlines()
#     num_lines = len(lines)
#     if num_lines < n:
#         print(f"please enter a valid value. the file has {num_lines} lines")
#     else:
#         for i in range(n):
#             print(lines[i].strip())
#

# **************************************
# problem 86 :- print the last n lines
# **************************************
# file_path = "pythonfiles.txt"
# n = int(input('how many last lines would you like to read:'))
# with open(file_path) as file:
#     lines = file.readlines()
#     num_lines = len(lines)
#     if num_lines < n:
#         print(f"please enter a valid value. the file has {num_lines} lines")
#     else:
#         for i in range(-n,0):
#             print(lines[i].strip())

# **************************************
# problem 87 :- longest word in a text file
# **************************************

# file_path = "pythonfiles.txt"
# longest_word = ''
# with open(file_path) as file:
#       for word in file:
#           if len(word) > len(longest_word):
#               longest_word = word
# print(longest_word)

# **************************************
# problem 88 :- frequency of words in a file into a dictionary
# **************************************
# file_path = "pythonfiles.txt"
# freq_dict = {}
# with open(file_path) as file:
#        for word in file:
#            word = word.strip('\n')
#            if word not in freq_dict:
#                freq_dict[word] =1
#            else:
#                freq_dict[word] +=1
# print(freq_dict)


# **************************************
# problem 89 :- list in a file to separate line
# **************************************
# file_path = "pythonfiles.txt"
# my_list = [1,2,3,4,5]
# with open(file_path,'w') as file:
#        for word in my_list:
#            file.write(str(word) + '\n')
#

# **************************************
# problem 90 :- length of characters in file
# **************************************
# file_path = "pythonfiles.txt"
# char_count = 0
# with open(file_path) as file:
#        for word in file:
#            char_count = len(word.replace(' ','').strip('\n'))
# print(char_count)

# **************************************
# problem 91 :- copy from file and write in new file
# **************************************
# file_path = "pythonfiles.txt"
# copy_path = "pythonfiles1.txt"
# with open(file_path) as file, open(copy_path, "w") as copy:
#        for word in file:
#            copy.write(word)

# **************************************
# problem 92 :- python file checking in path
# **************************************
# import os.path
# file_path = "pythonfiles.txt"
# if os.path.isfile(file_path):
#     print(f'The file {file_path} exists')
# else:
#     print(f'The file {file_path} notexists')

# **************************************
# problem 93 :- current date and time
# **************************************
# import datetime
# print('Current Date and Time')
# print(datetime.datetime.now())

# **************************************
# problem 94 :- converting seconds to minutes and hours
# **************************************

# seconds = 5400
# minutes = seconds // 60
# hours = minutes/60
#
# print(seconds, ' is equivalent to')
# print(minutes, ' minutes')
# print(hours, 'seconds')
# **************************************
# problem 95 :- area of a circle
# **************************************
# import math
# diameter = int(input('enter your diameter:--'))
# radius = diameter/2
# pi = math.pi
# area = pi * radius ** 2
# print(' The area of a circle with diameter ', diameter, ' is :-', area)

# **************************************
# problem 96 :- area of a triangle
# **************************************

# print('please enter valid values for base and height :-')
# base = int(input('enter your base:--'))
# height = int(input('enter your height:--'))
# area_of_circle = (base * height ) / 2
# print(' The area of a triangle with base ', base, ' and height  ',height, ' is:--', area_of_circle)

# **************************************
# problem 97 :- celsius to fahrenheit
# **************************************

# print('please enter valid celsius value  :-')
# celsius = int(input('enter your celsius value:--'))
# fahrenheit = (celsius * 9/5) + 32
# print(celsius, 'celsius = ',fahrenheit, ' fahrenheit' )

# **************************************
# problem 98 :- fahrenheit to celsius
# **************************************

# print('please enter valid fahrenheit value  :-')
# fahrenheit = int(input('enter your celsius value:--'))
# celsius = (fahrenheit - 32) * 5/9
# print(fahrenheit, 'celsius = ',celsius, ' fahrenheit' )

# **************************************
# problem 99 :- body  mass index
# **************************************
# print('please enter valid height and weight values  :-')
# height = int(input('enter your height value in cm:--'))
# weight = int(input('enter your weight value in kgs:--'))
# metres = height / 100
# bmi = weight / metres ** 2
# print('The body  mass index of a person with the height in cms : ', height, 'and weight in kgs : ',weight, 'is :-', bmi)
# if bmi < 18.5:
#     print(' The person is Underweight')
# elif 18.5 < bmi < 25:
#     print(' The person is normal')
# elif 25 < bmi < 30:
#     print(' The person is Overweight')
# elif bmi > 30:
#     print(' The person is obesity')
# else:
#     print(' please give valid details')
# **************************************
# problem 100 :- print calender
# **************************************
# import calendar
# print('welcome to the python calender')
# year = int(input('enter the year as YYYY format'))
# month = int(input('now enter the month(1-12: '))
# print(calendar.month(year,month))
# **************************************
# problem 101 :- difference between two days
# **************************************
# import datetime
# date1 = datetime.datetime(2023,2,2)
# date2 = datetime.datetime(2023,3,2)
# print('first date is ', date1)
# print('second date is ', date2)
# print(' difference is ', date2 - date1)

# **************************************
# problem 102 :- match string
# **************************************
# import re
# search = "^My[\w\s]+blue$"
# str = input('enter a string to check if a match is found:')
# if re.search(search,str):
#     print('match')
# else:
#     print('No match')
# **************************************
# problem 103 :- check balanced brackets
# **************************************
# def bal_brac(string):
#     count = 0
#     for bracket in string:
#         if bracket == '[':
#             count +=1
#         elif bracket == ']':
#             count -=1
#         if count < 0:
#             break
#     return count == 0
#
# print(bal_brac(('[]')))
# print(bal_brac(('[[]')))
# print(bal_brac(('[]]')))
# print(bal_brac((']')))
# print(bal_brac(('[[][]]')))
# print(bal_brac(('[[]]')))
# print(bal_brac(('[][[]')))
#
