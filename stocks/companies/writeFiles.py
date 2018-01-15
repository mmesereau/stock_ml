import requests
import csv
import datetime

def writeFile(company):
    apikey = 'WTYNLHRE6K26BJNC'
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={0}&outputsize=full&apikey={1}&datatype=csv'.format(company, apikey)
    response = requests.get(url)
    file = open("companies/companies/" + company + ".csv", "w")
    full = ""
    for item in response:
        full += str(item).replace("'b'", ",").replace("b'", "").replace("'", "")
    full = full.split('\r\n')[0].split('\\r\\n')
    for item in full:
        file.write(str(item) + '\n')
    return True

def update_csv(company):
    apikey = 'WTYNLHRE6K26BJNC'
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={0}&outputsize=compact&apikey={1}&datatype=csv'.format(company, apikey)
    full = ""
    days_to_add = []
    response = requests.get(url)
    existing_file = open("companies/companies/" + company + ".csv", "r")
    existing_data = existing_file.readlines()
    existing_file.close()
    # existing_data = existing.split('\n')
    file_to_update = open("companies/companies/" + company + ".csv", "w")
    for item in response:
        full += str(item).replace("'b'", ",").replace("b'", "").replace("'", "")
    full = full.split('\r\n')[0].split('\\r\\n')
    for day in full:
        date = day.split(',')[0]
        # print(date, datetime.date.today())
        # if str(date) == str(datetime.date.today()):
        #     print(date, (date in existing_data))
        if not any(str(date) in days for days in existing_data):
            print("new day added!")
            days_to_add.append(day + "\n")
    days_to_add.reverse()
    for day in days_to_add:
        existing_data.insert(1, day)
    for item in existing_data:
        file_to_update.write(str(item))
    return True

def clean(company):
    try:
        existing_file = open("companies/companies/" + company + ".csv", "r")
        existing_data = existing_file.readlines()
        existing_file.close()
        while "timestamp" not in existing_data[0]:
            existing_data = existing_data[1:]
        new_file = open("companies/companies/" + company + ".csv", "w")
        for item in existing_data:
            new_file.write(str(item))
        new_file.close()
        return True
    except:
        writeFile(company)
        return True


    # for item in response:
    #     print(item)
    # file = open("companies/companies/" + company + ".csv", "w")
    # data = str(response[0]).replace("'b'", ",").replace("b'", "").replace("'", "")
