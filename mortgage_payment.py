def ask_months():
    months = input("After this amount of months :\n")
    months = int(months)
    if not isinstance(months, int):
        print("Not valid")
        months = ask_months()
    return months


def ask_interest():
    interest = input("Monthly interest rate :\n")
    interest = float(interest)
    if not isinstance(interest, float):
        print("Not valid")
        interest = ask_interest()
    return interest / 100


def ask_total():
    total = input("Total length of loan in months :\n")
    total = int(total)
    if not isinstance(total, int):
        print("Not valid")
        total = ask_total()
    return total


def ask_principal():
    principal = input("Principal :\n")
    principal = int(principal)
    if not isinstance(principal, int):
        print("Not valid")
        principal = ask_principal()
    return principal


#Calculate the Outstanding Loan Balance
def loan_balance(principal, interest, total, months):
    first = (1 + interest) ** total
    second = (1 + interest) ** months
    third = (1 + interest) ** total
    third -= 1
    result = principal * ((first - second) / third)
    return result


#Calculate the fixed monthly payment
def monthly_payment(principal, interest, total):
    first = principal * interest
    second = (1 + interest) ** total
    third = (1 + interest) ** total
    third -= 1
    result = first * (second / third)
    return result


def payment():
    principal = ask_principal()
    interest = ask_interest()
    total = ask_total()
    months = ask_months()
    print("Fixed Monthly Payment = ", monthly_payment(principal, interest, total))
    print("Outstanding Loan Balance = ", loan_balance(principal, interest, total, months))


if __name__ == '__main__':
    payment();