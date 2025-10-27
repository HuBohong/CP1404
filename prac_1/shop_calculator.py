# # """
# # A shop requires a small program that would allow them to quickly work out the total price for a number of items, each with different prices.
# #
# # The program allows the user to enter the number of items and the price of each different item.
# # Then the program computes and displays the total price of those items.
# # If the total price is over $100, then a 10% discount is applied to that total before the amount is displayed on the screen.
# #
# # Sample output:
# # The output should look like the sample below (where bold text represents user input).
# # This uses f-string formatting to set the currency to 2 decimal places.
# #
# # """
# #
# total_price = 0
# item_number = int(input("Number of items: "))
#
# while item_number < 0:
#     print("Invalid number of items!")
#     item_number = int(input("Number of items: "))
#
# for item in range(item_number):
#     item_price = float(input("Price of item:"))
#     total_price += item_price
#
# if total_price > 100:
#     total_price *= 0.9
# print(f"Total price for {item_number} items is ${total_price: .2f} ")
#
# """
# 1. Discount Price
#
# get original_price
# discount = original_price * 0.2
# new_price = original_price – discount
# print new_price
# """
# DISCOUNT_RATE = 0.2
# original_price = float(input("Original price: "))
# discount = original_price * DISCOUNT_RATE
# new_price = original_price - discount
# print(new_price)
#
# """
# 2. Kilometres to Miles
#
# CHANGE_RATE =  0.621371
# get kilometres
# miles = kilometres *  CHANGE_RATE
# print miles
# """
#
"""
3. Holiday Cost

HOTEL_COST = 75
get daily_food_cost
get daily_activities_cost
get number_of_days
total_holiday_cost = (HOTEL_COST + daily_food_cost + daily_activities_cost) * number_of_days
print total_holiday_cost
"""
# HOTEL_COST = 75
# daily_food_cost = float(input("Daily food cost: "))
# #
# # persentage = 0.15 * 100
# # print(persentage, "%")
# deep_sleep_min = 1
# deep_sleep_sec = 20
# print("Deep sleep  = ", deep_sleep_min, "m", deep_sleep_sec, "s")
#
# # """
# 4. Deep Sleep
# """
# DISCOUNT_RATE = 0.2
# original_price = float(input("how much for original price"))
# discount = original_price * DISCOUNT_RATE
# new_price = original_price - discount
# print("the discounted price is, new_price")

# things = {1, 10, 20, 1, 10}
# things.add(20)
# print(len(things))

d ={'a': 123, 'b': 234}
d.get('a') += 1