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


with open("studentName","r") as in_file:
    list = in_file.readlines()

    for i in range(0,len(list),2):
        name = list[i].strip()
        country = list[i+1].strip()
        print(name,country)
