"""
CP1404/CP5632 Assignment 1 - Books to Read
Student Name: [你的姓名]
Student ID: [你的学号]
GitHub Repository Link: [你的GitHub仓库链接]
This program manages a list of books (to read and completed) via CSV file,
supporting display, add, and mark-as-completed functions with error handling.
"""

import csv

# 命名常量（遵循文档要求，仅使用全局常量）
COMPLETED = 'c'
UNREAD = 'u'
MENU_OPTIONS = """Menu:
D - Display books
A - Add a new book
C - Complete a book
Q - Quit
>>> """


def main():
    """主函数：程序入口，控制整体流程"""
    # 程序启动时加载书籍（仅一次）
    filename = "books.csv"
    books = load_books(filename)
    print(f"Books to Read 1.0 by [你的姓名]")
    print(f"{len(books)} books loaded.\n")

    # 显示菜单直到用户选择退出
    while True:
        choice = input(MENU_OPTIONS).strip().upper()
        if choice == 'D':
            display_books(books)
        elif choice == 'A':
            add_book(books)
        elif choice == 'C':
            complete_book(books)
        elif choice == 'Q':
            # 用户退出时保存书籍（仅一次）
            save_books(filename, books)
            print(f"\n{len(books)} books saved to {filename}")
            print("\"So many books, so little time. Frank Zappa\"")
            break
        else:
            print("Invalid menu choice\n")

def load_books(filename):
    """从CSV文件加载书籍数据到列表（列表嵌套列表），仅在程序启动时调用一次"""
    books = []
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 4:  # 确保每行包含完整的书籍数据（标题、作者、页数、状态）
                    title, author, pages_str, status = row
                    try:
                        pages = int(pages_str)
                        if pages > 0 and status in (COMPLETED, UNREAD):
                            books.append([title, author, pages, status])
                    except ValueError:
                        # 忽略页数非数字的无效行
                        pass
    except FileNotFoundError:
        # 若文件不存在，返回空列表（程序首次运行时可能出现）
        pass
    return books


def save_books(filename, books):
    """将书籍数据保存到CSV文件，仅在用户退出时调用一次"""
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(books)


def get_valid_input(prompt, validation_func, error_msg):
    """通用输入校验函数（遵循单一职责原则，复用性强）
    prompt: 输入提示文本
    validation_func: 校验函数（返回True表示输入有效）
    error_msg: 无效输入时的提示信息
    返回：有效输入值
    """
    while True:
        user_input = input(prompt).strip()
        if validation_func(user_input):
            return user_input
        print(error_msg)


def get_valid_number(prompt, min_value=1):
    """获取有效数字输入（用于页数和书籍编号）"""
    while True:
        user_input = input(prompt).strip()
        try:
            number = int(user_input)
            if number >= min_value:
                return number
            print(f"Number must be > {min_value - 1}")
        except ValueError:
            print("Invalid input - please enter a valid number")


def display_books(books):
    """按作者→书名排序显示书籍，未读书籍标注*，并统计未读页数和数量"""
    if not books:
        print("No books in the list.")
        return

    # 按作者（忽略大小写）排序，作者相同时按书名（忽略大小写）排序
    sorted_books = sorted(books, key=lambda x: (x[1].lower(), x[0].lower()))
    unread_count = 0
    unread_pages = 0

    # 计算标题和作者的最大长度（确保输出对齐）
    max_title_len = max(len(book[0]) for book in sorted_books)
    max_author_len = max(len(book[1]) for book in sorted_books)

    print("\nBook List:")
    for i, book in enumerate(sorted_books, 1):
        title, author, pages, status = book
        # 未读书籍前加*
        prefix = "*" if status == UNREAD else " "
        # 格式化输出（左对齐，按最大长度补空格）
        print(f"{prefix}{i}. {title:<{max_title_len}} by {author:<{max_author_len}} | {pages} pages")
        if status == UNREAD:
            unread_count += 1
            unread_pages += pages

    # 输出未读统计信息
    if unread_count == 0:
        print("No books left to read. Why not add a new book?")
    else:
        print(f"You still need to read {unread_pages} pages in {unread_count} books.\n")


def add_book(books):
    """添加新书籍（初始状态为未读），包含完整输入校验"""
    # 校验标题（非空）
    title = get_valid_input(
        "Title: ",
        lambda x: len(x) > 0,
        "Input can not be blank"
    )

    # 校验作者（非空）
    author = get_valid_input(
        "Author: ",
        lambda x: len(x) > 0,
        "Input can not be blank"
    )

    # 校验页数（正整数）
    pages = get_valid_number("Number of Pages: ", min_value=1)

    # 添加到内存列表（暂不保存到文件）
    books.append([title, author, pages, UNREAD])
    print(f"\n{title} by {author} ({pages} pages) added.\n")


def complete_book(books):
    """将未读书籍标记为已读，包含书籍编号校验"""
    # 筛选未读书籍
    unread_books = [book for book in books if book[3] == UNREAD]
    if not unread_books:
        print("No unread books - well done!\n")
        return

    # 显示未读书籍列表（供用户选择编号）
    print("\nUnread Books:")
    for i, book in enumerate(unread_books, 1):
        print(f"*{i}. {book[0]} by {book[1]} | {book[2]} pages")

    # 获取有效书籍编号
    book_index = get_valid_number(
        "Enter the number of a book to mark as completed: ",
        min_value=1
    ) - 1  # 转换为列表索引（从0开始）

    # 校验编号是否在未读书籍范围内
    if book_index >= len(unread_books):
        print("Invalid book number\n")
        return

    # 找到原列表中的书籍并更新状态（不可从已读改回未读）
    completed_book = unread_books[book_index]
    for book in books:
        if book == completed_book:
            book[3] = COMPLETED
            print(f"\n{book[0]} by {book[1]} completed!\n")
            break



if __name__ == "__main__":
    main()
# """
# CP1404 Assignment 1 - Books to Read
# Name:Hu Bohong
# Date Started:10/14/2025
# GitHub URL:https://github.com/cp1404-students/a1-books-HuBohong
# """
