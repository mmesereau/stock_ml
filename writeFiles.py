import requests
import csv

def writeFile(company):
    apikey = 'WTYNLHRE6K26BJNC'
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={0}&outputsize=full&apikey={1}&datatype=csv'.format(company, apikey)
    response = requests.get(url)
    file = open("companies/" + company + ".csv", "w")
    full = ""
    for item in response:
        full += str(item).replace("'b'", ",").replace("b'", "").replace("'", "")
    full = full.split('\r\n')[0].split('\\r\\n')
    for item in full:
        file.write(str(item) + '\n')
