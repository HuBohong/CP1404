MILETOKM = 1.60934

def main():
    speed_in_miles = get_valid_number("Speed in miles")
    speed_limit_in_kilometres = get_valid_number("speed limit in kilometres")

    speed_in_kilometres = convert_miles_to_kilometres(speed_in_miles)

    amount_over_limit = speed_in_kilometres - speed_limit_in_kilometres
    fine = determine_fine(amount_over_limit)

    print_in_format(speed_in_miles,speed_in_kilometres,amount_over_limit, fine)



def get_valid_number(prompt):
    value = int(input(prompt))
    return value

def convert_miles_to_kilometres(value):
    return value * MILETOKM

def determine_fine(amount_over_limit):
    if amount_over_limit <= 0:
        return 0
    elif amount_over_limit < 11 and amount_over_limit > 0:
        return 322
    elif amount_over_limit < 20 and amount_over_limit >= 11:
        return 483
def print_in_format(speed_in_miles,speed_in_kilometres,amount_over_limit, fine):
    if fine == 0:
       pass
    else:
        print(f"Your speed in miles: {speed_in_miles}")
        print(f"Your speed in kilometres: {speed_in_kilometres:.2f}")
        print(f"Your speed of {speed_in_kilometres} was over limit by {amount_over_limit:.2f}")
        print(f"Your fine will be ${fine}")
        bank_balance = get_bank_balance()

        print(f"Your bank balance after your fine will be ${bank_balance - fine}")



def get_bank_balance():
    return 0
main()
