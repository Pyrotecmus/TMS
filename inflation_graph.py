import sys
import requests
import json
import matplotlib.pyplot as plt


#sort and store the data to display
def store_data_to_display(sort):
    value = []
    month_year = []
    i = -1
    data = [[]]
    for useless in sort:
        i += 1
    while i != 0:
        value.append(float(sort[i]["value"]))
        month_year.append(sort[i]["periodName"] + " " + sort[i]["year"])
        i -= 1
    value.append(float(sort[0]["value"]))
    month_year.append(sort[0]["periodName"] + " " + sort[0]["year"])
    data[0].append(value)
    data[0].append(month_year)
    return data


#find the data and display it into a grpah
def inflation_graph(product_id, start_year, end_year):
    ranges = {'startyear': start_year, 'endyear': end_year}
    try:
        request = requests.get('http://api.bls.gov/publicAPI/v2/timeseries/data/' + product_id + '.json', params=ranges)
        data = json.loads(request.text)
    except ValueError:
        print("Json error")
        return
    if data is not None:
        data = store_data_to_display(data['Results']['series'][0]['data'])
        plt.plot(data[0][1], data[0][0])
        plt.show()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        inflation_graph(sys.argv[1], 2009, 2019)
    if len(sys.argv) == 4:
        inflation_graph(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
    else:
        print("Wrong number of arguments")