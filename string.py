## Задачи для закрепления на занятии

#1 Вводится строка. Удалить из нее все пробелы, после этого определить, 
# является ли она палиндромом, т.е. одинаково пишется как с начала так и с конца. 

# string = input('Enter a string: ')
# string_ = string.replace(' ','')

# if string_[:] == string_[::-1]:
#     print('Yes')
# else:
#     print('no no no')


# ------------------------------------------------------------------------------------------------
#2 Найти самое длинное слово в введенном предложении

# string = input('Enter a string: ').split()
# long_word =  string[0]
#
# for i in string:
#      if len(long_word) < len(i):
#         long_word = i
#
# print(long_word)

#4 Заменить все пробелы в строке на точки не используя replace.

# string = input('Enter a string: ').split()
# string_ = ','.join(string)
#
# print(string_)

# ------------------------------------------------------------------------------------------------
#5

# string = 'qwertyuiop'

# print(string[2])
# print(string[-1])
# print(string[0:5])
# print(string[2])
# print(string[1::2])
# print(string[0::2])
# print(string[::-1])
# print(string[::-2])
# print(len(string))

# ------------------------------------------------------------------------------------------------
# Вводится дата в формате `dd.mm.yyyy`
# Вывести дату в формате `mm\dd\yyyy`
# while True:
#     data_ = input('Enter a data (dd.mm.yyyy): ')
#     if len(data_) == 10 and data_[2] == '.' and data_[5] == '.':
#         data = data_.split('.')
#         print(f'{data[1]}/{data[0]}/{data[2]}')
#         break
#
#     else:
#         print('Incorrect enter! Enter format - dd.mm.yyyy')

# ------------------------------------------------------------------------------------------------
# Найти самое длинное слово в введенном предложении. Учтите что в предложении есть знаки препинания.
# string = input('Enter a string: ')
#
# string_ = string.replace('.','')
# string_ = string_.replace(',','')
# string = string_.split()
# long_word = string[0]
# for i in string:
#      if len(long_word) < len(i):
#         long_word = i
#
# print(f'Longest word: {long_word}')

# ------------------------------------------------------------------------------------------------
#Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
# Например, если было введено "abc cde def", то должно быть выведено "abcdef".
# string = input('Enter a string: ')
# string = string.replace(' ','')
# i = 0
# i_new = 0
# new_word = string[0]
#
# while i < len(string):
#     i_new = 0
#     while i_new < len(new_word):
#         if new_word.find(string[i]) == -1:
#             new_word += string[i]
#             i_new += 1
#         else:
#             i_new += 1
#     i += 1
#
# print(new_word)

# ------------------------------------------------------------------------------------------------
# Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
# Учитывать только английские буквы.
string = input('Enter a string: ')
i, big, small = 0, 0, 0
while i < len(string):
    if 64 < ord(string[i]) < 91 or 66 < ord(string[i]) < 123:
        if string[i].isupper() == True:
            big += 1
        else:
            small += 1
    i += 1

print(f'Smal letter: {small}, Big letter: {big}')