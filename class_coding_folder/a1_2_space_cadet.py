"""
CP1401 2025 TR3 Assignment 1 Program 2 – Space Cadet Results
Name: 你的姓名
Date started: 开始日期（如：2025-10-14）

"""

# 程序主逻辑
print("Welcome Trainee Space Cadet. How did you do?")
# 获取用户输入
practical_score = int(input("Practical score (0-50): "))
exam_score = int(input("Exam score (0-50): "))

# 计算总成绩
total_score = practical_score + exam_score
print(f"Your total score is {total_score} out of 100.")

# 成绩评定逻辑（嵌套决策+顺序判断，符合问题优先级）
if total_score < 50:
    # 条件1：不及格
    print("You failed. Please try again next year.")
else:
    # 条件2：及格，先判断岗位
    if practical_score >= exam_score:
        future_role = "field agent"
    else:
        future_role = "desk officer"
    # 再判断是否进入荣誉榜
    if total_score >= 85:
        print(f"You will become a {future_role}. Congratulations on making the honour roll!")
    else:
        print(f"You will become a {future_role}.")

