"""
CP1401 2025 TR3 Assignment 1 Program 1 – Simple Interest Calculator
Name: 你的姓名
Date started: 开始日期（如：2025-10-14）
Pseudocode:
1. 打印程序标题 "Simple Interest Calculator"
2. 获取用户输入的初始本金（starting balance），转换为浮点数
3. 获取用户输入的时间周期（time period），转换为整数
4. 定义固定年利率常量：INTEREST_RATE = 6.4（百分比形式）
5. 计算总利息：total_interest = starting_balance * (INTEREST_RATE / 100) * time_period
6. 计算到期本息和：future_balance = starting_balance + total_interest
7. 打印计算依据："Based on {time_period} time periods at {INTEREST_RATE}% per period"
8. 打印总利息，格式为保留2位小数的货币形式（$ X.XX）
9. 打印到期本息和，格式为保留2位小数的货币形式（$ X.XX）
"""

# 定义固定年利率常量（6.4%）
INTEREST_RATE = 6.4

# 程序主逻辑
print("Simple Interest Calculator")
# 获取用户输入（无需处理类型错误，按文档要求）
starting_balance = float(input("Starting balance: "))
time_period = int(input("Time period: "))

# 计算单利和到期本息和
total_interest = starting_balance * (INTEREST_RATE / 100) * time_period
future_balance = starting_balance + total_interest

# 输出结果（严格匹配示例格式，保留2位小数）
print(f"Based on {time_period} time periods at {INTEREST_RATE}% per period")
print(f"Total interest = $ {total_interest:.2f}")
print(f"Future balance = $ {future_balance:.2f}")