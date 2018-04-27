# To install module, please enter command in terminal:
# pip install pyyaml
import yaml

import csv

# The next function reads data from a yaml file
# and displays it into the console
FILE_NAME = "random.yaml"

def builDictionary(stream):
    for key, value in stream.items():
        # populate dictionary here >>
        print(key, value)

def readYaml(file_name):
    with open(file_name, "r") as stream:
        try:
            data = yaml.load(stream)['army']
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



readYaml(FILE_NAME)