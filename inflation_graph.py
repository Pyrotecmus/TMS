import sys
import requests


def inflation_graph(product_id):
    request = requests.get('http://api.bls.gov/publicAPI/v2/timeseries/data/' + product_id + '.json')
    print(request)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        inflation_graph(sys.argv[1])
    else:
        print("Wrong number of arguments")