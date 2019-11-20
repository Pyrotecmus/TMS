import csv
import matplotlib.pyplot as plt


def parsing():
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        price = []
        demand = []
        supply = []
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                price.append(int(row[0]))
                demand.append(int(row[1]))
                supply.append(int(row[2]))
                line_count += 1
        plt.plot(supply, price, label="supply")
        plt.plot(demand, price, label="demand")
        plt.xlabel("quantity")
        plt.ylabel("price")
        plt.legend()
        plt.show()


if __name__ == '__main__':
    parsing()