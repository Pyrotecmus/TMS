import sys
import pycountry
from forex_python.converter import CurrencyRates
import matplotlib.pyplot as plt


#compare each currency and fill a data to return
def currency_change(country, countries):
    currency = CurrencyRates()
    data = []
    for change in countries:
        if pycountry.currencies.get(alpha_3=change) is not None:
            data.append(currency.convert(country, change, 1))
    return data


#print the data
def print_matrix(data):
    for line in data:
        print(line)


#Call a function to fill the data to display for each currency
def currency_matrix(countries):
    data = []
    disp_countries = []
    for country in countries:
        if pycountry.currencies.get(alpha_3=country) is not None:
            disp_countries.append(country)
            data.append(currency_change(country, countries))
    print_matrix(data)
    return


if __name__ == '__main__':
    currency_matrix(sys.argv)