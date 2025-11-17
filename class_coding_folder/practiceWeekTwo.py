# with open("GuitarPractice" , "r") as file:
#     for line in file:
#         word = line.strip().split(",")
#         # print(word)
#         try:
#             print(f"Guitar {word[0]} founded in {word[1]} price is ${word[2]}")
#         except IndexError:
#             # print("Invalid line in file")
#             word.append("Unknown")
#             word.append("0")
#             print(f"Guitar {word[0]} founded in {word[1]} price is ${word[2]}")

# with open("GuitarPractice", "a") as file:
#     # print()
#     file.write("abc,2020,1000 \n")

# with open("GuitarPractice" , "r") as file:
#     # line = file.readline()
#     # print(line)
#     line = file.readlines()
#     print(line)

# with open("GuitarPractice" , "r") as file:
#     # line = file.readline()
#     # print(line)
#     line = file.read(128)
#     print(line)
#
# with open("GuitarPractice" , "rb") as file:
#     # line = file.readline()
#     # print(line)
#     line = file.read()
# #     print(line)
# user_file = input("Enter file name: ")
# in_file = open(user_file , "r")
# for line in in_file:
#     if line.startswith("#"):
#         print(line)

# s = "\tPython, Monty  \n"
# # print(s[1], ".", sep="")
# # print(s.replace(" ","*"))
# print(s.strip(), sep="")
# print(s.rstrip().split(","))

### !!! with open 注意缩进 indentation!!!!!

# name = input("Enter file name: ")
# with open(name, "w") as out_file:
#     print(name, file=out_file)
# print("done")

# names = ["abc", "def", "ghi"]
# for name in names:
#     file_name = name + ".txt"
#     with open(file_name, "w") as out_file:
#         print(names.index(name) + 1,name, file = out_file)

#
# with open("studentName","r") as in_file:
#     list = in_file.readlines()
#
#     for i in range(0,len(list),2):
#         name = list[i].strip()
#         country = list[i+1].strip()
#         print(name,country)

# test = "this is a test"
#
# #
# # dic(str)
# text = "Enjoy the test"
# result = text.strip().split()
# print(result)

# x = "str(1.0)"
# x[-1] = "5"

# x = str(int('1'))
# # x[-1] = '2'

# try:
#     x = int("0")
#     print(10 / x)
# except ZeroDivisionError:
#     print("div")
# except NameError:
#     print("name")
# except ValueError:
#     print("value")
# except:
#     print("other")


# import random
# print(random.uniform(1,2))

# s = "Python"
# print(s[1:4])
# print(s[0:-4])
# print(s[-4:0])

# something = "i an the king of the world"
# words = something.split()
# i = 0
# for word in words:
#     words[i] = word.title()
#     i += 1
# text = ",".join(words)
# print(text)
# x = 1.32323232323
# print(f"{x:,.2f}")

# names= ["Ada","Alan","Bill","John"]
# print(",".join(name))
# name_to_remove = input("Who do you want to remove: ")
# while name_to_remove != "":
#     try:
#         name.remove(name_to_remove)
#     except ValueError:
#         print("Not found")
#
#     print(",".join(name))
#     name_to_remove = input("Enter name to remove: ")

# for name in names:
#     print(name)

# del(names[2])
# print(names)
# x = [5]
# print(x is 5)

# s = "1 ,2 ,3, 4, 5"
#
# print([x for x in s])
# #
# s = ["1","2","3","4","5"]
# print([c for c in s])
#
# def main():
#     numbers = get_numbers()
#     square_numbers(numbers)
#     display_numbers(numbers)
#
#
# def get_numbers():
#     user_input = input("Enter numbers separated by commas: ")
#     numbers = user_input.split(",")
#     return [number.strip() for number in numbers]
#
#
# def square_numbers(numbers):
#     for i in range(len(numbers)):
#         numbers[i] = float(numbers[i]) ** 2
#
#
# def display_numbers(numbers):
#     print("..".join([str(number) for number in numbers]))
#
#
# main()
# from operator import itemgetter
#
# data = [["Derek",7],["x",80],["b",612],["C",9]]
# name_width = max([len(pair[0]) for pair in data])
# number_width = max([len(str(pair[1])) for pair in data])
#
# data.sort(key=itemgetter(1),reverse=True)
# for row in data:
#     print(f"{row[0]:<{name_width}} = {row[1]:>{number_width}}")
#
# print(range(0,4))
# before = [1, 4, 0, -1]
# after = before.sort()
# print(after[0])

# words = "aye bee sea"
# print("/".join(words))

# print("*".join([len(word) for word in "one*two*three".split('*')]))

# things = list("one two three")
# print("{}-{}".format(*things))
#
# things = [True, 1.2, "Good", [1, 10]]
# print("%".join([things[2][1:-1]]))
# print([t for t in things if type(t) in (float, int)])
# contro

# SENTINEL = -1
# total_age = 0
# ppl_count = 0
# value = int(input("please enter yur age (-1 for exit)"))
# while value != SENTINEL:
#     ppl_count = ppl_count + 1
#     total_age = total_age + value
#     value = int(input("please enter yur age (-1 for exit)"))
# print(ppl_count,total_age)

# data = [["Derek",7],["Xavier",80],["bob",612],["Chantanelle",9]]
#
# name_length = max(len(parts[0]) for parts in data)
# number_length = max(len(str(parts[1])) for parts in data)
#
# for parts in data:
#     print(f"{parts[0]:{name_length}} - {parts[1]:{number_length}}")

# data = {"Derek":7,"Xavier":80,"bob":612,"Chantanelle":9}
# name_length = max(len(name) for name in data.keys())
# for name, age in data.items():
#     print(f"{name: {name_length}} =  {age}")

# data = ["Derek", "Xavier", "bob", "Chantanelle"]
# name_and_length = {}
# for name in data:
#     name_and_length[name] = len(name)
# print(name_and_length)
#
# name_and_length_com = {name: len(name) for name in data}
# print(name_and_length_com)

# monsters = [["mike", 340], ["James", 14], ["Randall", 24]]
# scary_monsters = [monster for monster in monsters if monster[1] > 16]
#
# print(scary_monsters)


"""
为什么要用函数？
高代码复用性
提高代码可读性
模块化编程

def 函数名(参数列表):
    ### 函数体
    return 返回值

函数名()
def get_valid_number(x):
    y = x+3
    return y

y = get_valid_number(5)
##函数名命名方法?

形参 vs 实参
参数传递机制


"""
from operator import length_hint

from Demos.security.sspi.validate_password import validate

# def get_valid_number(x):
#     y = x+3
#     return y
#
# jie_shou = get_valid_number(5)
# print(jie_shou)

# def main():
#     height = get_valid_number()
#
#     dose = input("Dose: ")
#     yie = input("Yield: ")
#     ratio = calculate_coffee_ratio(dose, yie)
#
#     calculate_bmi(2,3)
#
# def get_valid_number():
#     return 1
#
# def calculate_bmi(height, weight):
#     return weight / (height ** 2)
# def calculate_coffee_ratio(dose, yie):
#     return yie / dose
#
#
# class Thing:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def change(self, b):
#         self.a += b
#
# it = Thing(5, 6)
# it.change(2)
# # print(it.a, it.b)
#
# FILENAME = "practiceWeekTwo.py"
#
# def factorial1():
#     x = 1
#     print(x+g)
#
# def factorial2():
#     a = 2
#     print(FILENAME)
#
# def main():
#     g = 1
#     factorial1()
#     factorial2()
#
# main()
#
# numbers = [10, 20, 40, 20 ,81]
# #
# # # numbers.append(1)
# # numbers.reverse()
#
#
# for number in numbers:
#     print(number)


# places = ["guizhou", "beijing", "shanghai", "hangzhou", "gangguojin", "shizonglinjia"]
# # place = input("Place: ")
# # while place != "":
#         places.append(place)
# #     place = input("Place: ")
# # print(len("gangguojin"))
# # print(len(places))
# longest_place = ""
# length = 0
# print("On my holiday, I went to: ")
# for place in places:
#     if len(place) > length:
#         longest_place = place
#         length = len(place)
#
# print(longest_place)



# """
# 1 用户输入要生成多少个随机数
# 2 让用户设置随机数最大数字
# 3 最大值
# 4 最小值
# 5 随机从列表中选择一个数字
# 6 顺序排列
# 7 反序排列
# # """
# from random import randint
#
# number_of_randoms = 5
# max_of_ramdoms = 100
#
#
# numbers = []
#
# for i in range(number_of_randoms):
#     random_number = randint(0, max_of_ramdoms)
#     #将随机数加入列表
#     numbers.append(random_number)
# #最大值
# max(numbers)
# #最小值
# min(numbers)
# #生成随机索引
# random = randint(0,len(numbers)-1)
# print(numbers)
# #打印随机索引对应的数字
# print(numbers[random])
#
# #反序排列
# numbers.reverse()
# print(numbers)
# #顺序排列
# numbers.sort()
# print(numbers)


#
# red_team = ["Miles", "Ella", "Chet"]
# blue_team = ["Louis", "Wes", "Jimmy"]
#
# for player in red_team:
#     for opponent in blue_team:
#         print(f"{player} vs. {opponent}")
#     print("---------------------")
# print()

# position argument的顺序