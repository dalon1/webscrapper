from lxml import etree
import io

class ParserUtils(object):

    @staticmethod
    def parseAccountName(source_code, xpath):
        # Creating a file-like object with the respective source coode
        try:
            f = io.BytesIO(source_code)
            tree = etree.parse(f, etree.HTMLParser())
            result = tree.xpath(xpath)
            return result
        except Exception as e:
            print("Parsing Error: " +  e)
    
    @staticmethod
    def parseSingleValue(source_code, xpath):
        # Creating a file-like object with the respective source coode
        try:
            f = io.BytesIO(source_code)
            tree = etree.parse(f, etree.HTMLParser())
            result = tree.xpath(xpath)
            return result
        except Exception as e:
            print("Parsing Error: " +  e)

    @staticmethod
    def parseAccountRateTableBeta(source, xpath):
        records = []
        for x in range(2, 4):
            for i in range(1, 3):
                print(x, i)
                if (i % 2 != 0):
                    records.append(ParserUtils.parseSingleValue(source, "//*[@id='blq-content']/div[6]/div/div/div/div[2]/div/div/div/div/table/tbody/tr[" 
                    + str(x) + "]/td[" + str(i) + "]/text()"))
                else:
                    records.append(ParserUtils.parseSingleValue(source, "//*[@id='blq-content']/div[6]/div/div/div/div[2]/div/div/div/div/table/tbody/tr[" 
                    + str(x) + "]/td[" + str(i) + "]/span/text()"))
        return records
    
    @staticmethod
    def parseRatesTable(source, start_xpath, end_xpath):
        records = []
        # Comparing xpaths - char by char to check for differences to determine the size of the table tr[x] & td[y]
        i = [i for i in range(len(start_xpath)) if start_xpath[i] != end_xpath[i]]
        
        # I'll explain this code soon. But this allows me to iterate through all the interest rates table,
        # once I have determined with the previous lambda expressions the delimiter of the table
        for tr in range(int(start_xpath[i[0]]), int(end_xpath[i[0]]) + 1):
            for td in range(int(start_xpath[i[1]]), int(end_xpath[i[1]]) + 1):
                print("tr: " + str(tr) + ", td: " + str(td))


        return records
