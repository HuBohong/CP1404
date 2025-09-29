"""
A teacher is distributing gifts to students.
Each student should receive the same number of gifts.
The teacher wants to know how many gifts each student will get and how many gifts will be left.
"""
#
# gift_number = int(input("Number of gifts:"))
# stu_number = int(input("Number of students:"))
#
# gift_avg = gift_number // stu_number
# gift_left = gift_number % stu_number
#
# print(gift_avg)
# print(gift_left)
#
# item_price = float(input("please enter a price:"))
# GST = input("is there GST? (True/False):").upper()
# flag = []
# flag.append(GST)
#
# if "T" or "TRUE" in flag:
#     print(f"{item_price}+GST")
# else:
#     print(item_price)

# user_number = int(input("please enter a number:"))
# my_number = 1

# while user_number >= 0:
#     print(user_number)
#     user_number -= 1
#
# for i in range(1,user_number):
#     print(i)
#
# while my_number < user_number:
#     print(my_number)
#     my_number += 1

# constant_number = 8
# guessed_number = int(input("please gess the number"))
#
# while guessed_number != constant_number:
#     print("wrong")
#     guessed_number = int(input("please gess the number"))
#
# print(f"you got it,the correct number is {guessed_number}")

# user_name = input("please enter your name")
# user_salary = float(input("please enter your salary"))
#
# while user_salary < 0 or user_name == "":
#     print("invalid input")
#     user_name = input("please enter your name")
#     user_salary = int(input("please enter your salary"))
#
# print(f"your name is {user_name.upper()} and salary is ${user_salary:.2f}")

# total_age = 0
# people_number = int(input(" How many people are there? "))
# while people_number <= 0:
#     print("Invalid input")
#     people_number = int(input("How many people are there? "))
#
# for i in range(people_number):
#
#     age = int(input("Age: "))
#
#     while age <0:
#         print("Invalid input")
#         age = int(input("Age: "))
#
#     total_age += age
#
# # avg_age = total_age / people_number
# # print(f"the total number of people is {people_number} and the average age is {avg_age:.2f}")
# user_input = 0
# total_age = 0
# count = 0
#
# while user_input != -1:
#     user_input = int(input("please enter the age, enter -1 to stop"))
#     # while user_input <= 0:
#     #     print("error input")
#     #     user_input = int(input("please enter the age, enter -1 to stop"))
#
#     total_age += user_input
#     count += 1
#
# if total_age <= 0:
#     print("no data")
# else:
#     avg_age = total_age / count
#     print(f"the average age is:{avg_age:.2f} and the total number of people is {count}")

# i-j+i

# 1-2+1
# 1-5+1
# 1-8+1
# 2-2+2
# 2-5+2
# 2-8+2
# 3-2+3
# 3-5+3
# 3-8+3

# import random
#
# length = int(input("input a value"))
# width = random.randint(1,length+1)
#
# area = length * width
# print(f"The area is: {area}")

# from random import randint
#
#
# def main():
#     high, low = get_valid_number()
#     random_number = randint(low, high + 1)
#     print_face(random_number)
#
#
# def get_valid_number():
#     high = int(input("Please enter the height number"))
#     low = int(input("Please enter the low number"))
#
#     while high <= low:
#         print("Invalid input")
#         high = int(input("Please enter the height number"))
#         low = int(input("Please enter the low number"))
#
#     return high, low
#
#
# def print_face(random_number: int):
#     print(":)" * random_number)
#
#
# main()

#
# """practice"""
# import random
#
#
# def main():
#     name = ""
#     print_menu()
#     user_choice = int(input("please select a method to try:"))
#
#     # while user_choice > 4 or user_choice < 1:
#     #     print("Invalid input")
#     #     user_choice = int(input("please select a method to try:"))
#
#     while user_choice != 4:
#         if user_choice == 1:
#             name = get_name()
#
#         elif user_choice == 2:
#             print_lines()
#
#         elif user_choice == 3:
#             print_ramdom_number()
#
#         else:
#             print("invalid input")
#         print_menu()
#         user_choice = input("please select a method to try:")
#
#     print(f"bye{name}")
#
#
# def print_menu():
#     print("User Menu:\n 1. get valid name \n 2. print a line \n 3. print ramdom number \n 4.quit")
#
#
# def get_name():
#     """get valid name from user"""
#     user_name = input("please enter your name:")
#     while user_name == "":
#         print("invalid input")
#         user_name = input("please enter your name:")
#
#     return user_name
#
#
# def print_lines():
#     print("*" * 10)
#
#
# def print_ramdom_number():
#     print(random.randint(1, 100))
#
#
# main()
#
# """
# assertion statement
# true do noting
# false raise assertion error
# """
#
#
# # max_length = m
#
# list = [1,2,3,4,5,6,7,8,9]
# # print(max(list))
# text = "This is a sentence"
# list_word = text.split()
# for word in list_word:
#     if len(word) > 3:
#         print(word)

# for char in text:
# #     print(char, end=" ")
# file = open("GuitarPractice" , "a")
# file.write("GuitarPractice")
# file.close()