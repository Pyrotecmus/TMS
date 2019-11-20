import matplotlib.pyplot as plt


def donuts():
    product = input("Please enter a product\n")
    quantity = input("Please enter the maximum quantity\n")
    quantity = int(quantity)
    data = []
    quantities = []
    i = 0
    while i != quantity:
        i += 1
        quantities.append(i)
        data.append(int(input("For " + i.__str__() + " " + product + " what added happiness do you get\n")))
    plt.plot(quantities, data, label="happiness")
    plt.xlabel("Quantity of " + product)
    plt.ylabel("Utility")
    plt.show()
    return


if __name__ == '__main__':
    donuts()