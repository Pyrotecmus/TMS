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


def ask_future_value():
    future = int(input("Enter the future value\n"))
    if not isinstance(future, int):
        return ask_future_value()
    return future


def calculate_present_value(years, interest, future):
    denominator = (1 + interest) ** years
    present = future / denominator
    return present


def present_value():
    future = ask_future_value()
    interest = ask_interest_rate()
    years = ask_number_years()
    print(calculate_present_value(years, interest, future))


if __name__ == '__main__':
    present_value()