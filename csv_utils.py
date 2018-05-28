import csv

class CSVUtils(object):

    @staticmethod
    def createCSVFile(file_name, records):
        # removing that extra blank line created by default between records.
        with open(file_name, 'w', newline='') as csvfile:
            # Creating file writer (python) or stream writer (c#)
            file_writer = csv.writer(csvfile, delimiter = ',', 
            dialect = 'excel', quoting = csv.QUOTE_MINIMAL, quotechar='|')
            for record in records:
                file_writer.writerow([record.bank_name, record.account_name, record.account_range, record.rate])
    
    @staticmethod
    def createCSVRecord(stream):
        # Example: <bank_name>, <bank_account_name>, <range_rate>, <interest rate>
        records = []
        for i in range(0, len(stream)):
            for j in range(0, len(stream[i]['accounts'])):
                print([stream[i]['name'], stream[i]['url'], 
                stream[i]['accounts'][j]['account_name'], stream[i]['accounts'][j]['account_xpath'] ])
                records.append([stream[i]['name'], stream[i]['url'], 
                stream[i]['accounts'][j]['account_name'], stream[i]['accounts'][j]['account_xpath']])
        return records
