"""
1.Coffee Brew Ratio

function main()
    dose = get_valid_number("dose (g)", 0, 100)
    yield_stmt = get_valid_number("yield (g)", 0, 300)
    ratio = calculate_ratio(yield_stmt, dose)
    category = determine_coffee_category(ratio)
    display ratio,category

function get_valid_number(prompt, low, high)
    display prompt
    get value
    while value < low or value > high
        display Invalid number,try again
        get value
    return value

function calculate_ratio(yield_stmt, dose)
    ratio = yield_stmt / dose
    return ratio

function determine_coffee_category(ratio)
    if ratio < 2:
        return "ristretto"
    if ratio < 3:
        return "normale"
    return "lungo"

main()
"""
def main():
    dose = get_valid_number("dose (g)", 0, 100)
    yield_stmt = get_valid_number("yield (g)", 0, 300)
    ratio = calculate_ratio(yield_stmt, dose)
    category = determine_coffee_category(ratio)
    print(f"1:{ratio:.1f} is considered {category}")

def get_valid_number(prompt, low, high):
    print(prompt)
    value = float(input("Enter your value: "))
    while value < low or value > high:
        print("Invalid number, try again")
        value = float(input("Enter your value: "))
    return value

def calculate_ratio(yield_stmt, dose):
    ratio = yield_stmt / dose
    return ratio

def determine_coffee_category(ratio):
    if ratio < 2:
        return "ristretto"
    if ratio < 3:
        return "normale"
    return "lungo"

main()

