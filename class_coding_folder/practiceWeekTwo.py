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

monsters = [["mike", 340], ["James", 14], ["Randall", 24]]
scary_monsters = [monster for monster in monsters if monster[1] > 16]

print(scary_monsters)
