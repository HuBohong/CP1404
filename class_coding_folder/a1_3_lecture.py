"""
CP1401 2025 TR3 Assignment 1 Program 3 – Lecture Tracker
Name: 你的姓名
Date started: 开始日期（如：2025-10-14）
"""
# 定义周数最大值常量（按文档要求为10）
MAX_WEEKS = 10

# 程序主逻辑
print("Lecture Tracker - How are you going with watching lecture videos?")

# 步骤1：获取并验证周数
number_of_weeks = int(input("Number of weeks so far: "))
# 周数错误检查（<0或>10则设为10）
if number_of_weeks < 0 or number_of_weeks > MAX_WEEKS:
    print(f"Invalid number of weeks. Using the maximum of {MAX_WEEKS}.")
    number_of_weeks = MAX_WEEKS

# 步骤2：循环获取每周观看百分比（带错误检查）
total_percentage = 0  # 存储总观看百分比
for week in range(1, number_of_weeks + 1):
    is_valid_input = False
        # 持续获取输入，直到得到有效百分比
    percentage_input = float(input(f"Week {week} percentage of lecture videos watched: "))
    while percentage_input< 0 or percentage_input> 100:
        # 百分比有效性判断（0<=x<=100）

        percentage_input = float(input(f"Week {week} percentage of lecture videos watched: "))

        # else:
        #     # 有效则累加到总数，跳出当前周循环
        #     total_percentage += percentage_input
        #     is_valid_input = True

# 步骤3：计算并输出结果
average_percentage = total_percentage / number_of_weeks
remaining_percentage = 100 - average_percentage

# 打印平均百分比 注意格式要求
print(f"Your average percentage lecture watching was {average_percentage:.1f}%")

# 输出评价信息
if average_percentage == 100.0:
    print("Great job! You are doing the recommended minimum amount of lecture watching.")
else:
    print(f"You still have {remaining_percentage:.1f}% of the lectures to catch up on. You can do it!")