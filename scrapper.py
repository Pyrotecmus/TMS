import selenium
from selenium import webdriver
import sys
import pycountry
import random


def save(driver, av):
    if av[1] == "all":
        randomCountries(driver)
    else:
        topFour(av[1], driver)
    return


def fill(str):
    split = str.splitlines(0)
    country = pycountry.countries.get(name=split[0])
    num = split[1].replace(',', '')
    num = num.replace('.', '')
    oui = int(num)
    oui = oui / 100000000
    ret = country.alpha_3 + " " + int(oui).__str__() + "B\n"
    return ret


def randomCountries(driver):
    driver.get("https://wits.worldbank.org/CountryProfile/en/Country/USA/Year/2017/TradeFlow/Export/Partner/by-country/Product/Total")
    data = []
    data.append(driver.find_element_by_xpath('//*[@id="row0jqx-ProductGrid"]').text)
    data.append(driver.find_element_by_xpath('//*[@id="row1jqx-ProductGrid"]').text)
    data.append(driver.find_element_by_xpath('//*[@id="row2jqx-ProductGrid"]').text)
    data.append(driver.find_element_by_xpath('//*[@id="row3jqx-ProductGrid"]').text)
    data.append(driver.find_element_by_xpath('//*[@id="row4jqx-ProductGrid"]').text)
    ret = ""
    ret += fill(data[0])
    ret += fill(data[1])
    ret += fill(data[2])
    ret += fill(data[3])
    ret += fill(data[4])
    return


def topFour(country, driver):
    driver.get("https://wits.worldbank.org/CountryProfile/en/Country/" + country + "/Year/2017/TradeFlow/Export/Partner/by-country/Product/Total")
    data = []
    data.append(driver.find_element_by_xpath('//*[@id="row0jqx-ProductGrid"]').text)
    data.append(driver.find_element_by_xpath('//*[@id="row1jqx-ProductGrid"]').text)
    data.append(driver.find_element_by_xpath('//*[@id="row2jqx-ProductGrid"]').text)
    data.append(driver.find_element_by_xpath('//*[@id="row3jqx-ProductGrid"]').text)
    ret = ""
    ret += fill(data[0])
    ret += fill(data[1])
    ret += fill(data[2])
    ret += fill(data[3])
    return ret


def scrapper(av, driver):
    if av[1] == "all":
        print(randomCountries(driver))
    else:
        print(topFour(av[1], driver))
    return


if __name__ == '__main__':
    driver = webdriver.Chrome('./chromedriver')
    scrapper(sys.argv, driver)
    driver.close()
