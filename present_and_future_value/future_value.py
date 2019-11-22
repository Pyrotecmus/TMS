def ask_number_years():
    years = int(input("Enter the number of years\n"))
    if not isinstance(years, int):
        return ask_number_years()
    return years


def ask_interest_rate():
    interest = float(input("Enter the rate\n"))
    if not isinstance(interest, float):
        return ask_interest_rate()
    return interest


def ask_present_value():
    future = int(input("Enter the present value\n"))
    if not isinstance(future, int):
        return ask_present_value()
    return future


def calculate_future_value(years, interest, present):
    future = present * (1 + interest) ** years
    return future


def future_value():
    present = ask_present_value()
    interest = ask_interest_rate()
    years = ask_number_years()
    print(calculate_future_value(years, interest, present))


if __name__ == '__main__':
    future_value()