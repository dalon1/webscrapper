# To install module, please enter command in terminal:
# pip install pyyaml
import yaml

import urllib.request as request
from lxml import etree
import csv

# The next function reads data from a yaml file
# and displays it into the console
FILE_NAME = "bank-data.yaml"

def builDictionary(stream):
    for key, value in stream.items():
        # populate dictionary here >>
        print(key, value)

def readYaml(file_name):
    with open(file_name, "r") as stream:
        try:
            data = yaml.load(stream)['root']
            builDictionary(data)
            createCSV('csvtest1.csv', data)
            #print(yaml.load(stream)['army'])
        except yaml.YAMLError as exc:
            print("Error: " + exc)

def createCSV(file_name, stream):
    # removing that extra blank line created by default between records.
    with open(file_name, 'w', newline='') as csvfile:
        # Creating file writer (python) or stream writer (c#)
        file_writer = csv.writer(csvfile, delimiter = ',', 
        dialect = 'excel', quoting = csv.QUOTE_MINIMAL, quotechar='|')
        for key, value in stream.items():
            file_writer.writerow([key, value])

def accessURL(url):
    #Proxy should be handled here >>
    req = request.Request(url = url, headers= {'Content-Type': 'text/html'})
    response = request.urlopen(req)
    print(response.read())
    #tree = etree.parse(response, etree.HTMLParser())
    #print(test)
    #nodes = etree.xpath('//*[@id="account-summaries"]/li/div[1]/table')
    #print(nodes)


readYaml(FILE_NAME)
#accessURL("http://www.scotiabank.com/ca/en/0,,1115,00.html")