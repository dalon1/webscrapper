from yaml_utils import YAMLUtils
from csv_utils import CSVUtils
from http_utils import HttpUtils
from parser_utils import ParserUtils

#url = "http://www.rbcroyalbank.com/rates/persacct.html"
#xpath = "/html/body/table[1]/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[4]/td[2]/table[3]/tbody/tr/td[2]/h3/a/i"

#url = "http://dannelvision.com/"
#xpath = "//*[@id='wrapper']/div[3]/div/h2/small/text()"

#url = "https://www.cibc.com/en/interest-rates/personal-bank-account-rates.html"
#xpath = "//*[@id='blq-content']/div[6]/div/div/div/div[1]/div/div/p[1]/a/strong/text()"
#xpath = "//*[@id='blq-content']/div[6]/div/div/div/div[2]/div/div/div/div/table/tr/td/text()"
#xpath = '//*[@id="blq-content"]/div[6]/div/div/div/div[2]/div/div/div/div/table/tbody/tr[2]/td[1]/text()'
#xpath = '//*[@id="blq-content"]/div[6]/div/div/div/div[2]/div/div/div/div/table/tbody/tr[2]/td[2]/span/text()'

#url = "https://www.tdcanadatrust.com/products-services/banking/accounts/account-rates.jsp"
#xpath = '///*[@id="sa"]/table/tbody/tr[3]/th/text()'

#url =  "https://www.bmo.com/home/personal/banking/rates/gic-term-deposits"
#xpath = "//*[@id='main_content']/h3[1]/a/text()"
#xp1 = '//*[@id="header3"]/text()'
#xp2 = '//*[@id="main_content"]/table[3]/tbody/tr[2]/td[2]/text()'
url = 'https://www.simplii.com/en/rates.html'
xp1 = '//*[@id="accounts"]/div[1]/div/h4/span/text()'
xp2 = '//*[@id="accounts"]/div[2]/div/div/div/table/tbody/tr[2]/td[2]/p/text()'
xp3 = '//*[@id="accounts"]/div[2]/div/div/div/table/tbody/tr[2]/td[1]/p/text()'
source = HttpUtils.getSourceCode(url)
#print(source)
#account = ParserUtils.parseAccountRateTable(source, xpath)
#account = ParserUtils.parseSingleValue(source, xpath)
#print(account)
#a = ParserUtils.parseSingleValue(source, xp1)
#print(a)
#print(ParserUtils.parseSingleValue(source, xp2))
#print(ParserUtils.parseSingleValue(source, xp3))

start_xpath = '//*[@id="accounts"]/div[2]/div/div/div/table/tbody/tr[2]/td[1]/p/text()'
end_xpath = '//*[@id="accounts"]/div[2]/div/div/div/table/tbody/tr[6]/td[2]/p/text()'
# Comparing xpaths - char by char to check for differences to determine the size of the table tr[x] & td[y]
#i = [i for i in range(len(start_xpath)) if start_xpath[i] != end_xpath[i]]
        
        # I'll explain this code soon. But this allows me to iterate through all the interest rates table,
        # once I have determined with the previous lambda expressions the delimiter of the table
#for tr in range(int(start_xpath[i[0]]), int(end_xpath[i[0]]) + 1):
#    for td in range(int(start_xpath[i[1]]), int(end_xpath[i[1]]) + 1):
#        print("tr: " + str(tr) + ", td: " + str(td))

def parseRatesTable(source, start_xpath, end_xpath):
        records = []
        # Comparing xpaths - char by char to check for differences to determine the size of the table tr[x] & td[y]
        i = [i for i in range(len(start_xpath)) if start_xpath[i] != end_xpath[i]]
        
        # I'll explain this code soon. But this allows me to iterate through all the interest rates table,
        # once I have determined with the previous lambda expressions the delimiter of the table
        for tr in range(int(start_xpath[i[0]]), int(end_xpath[i[0]]) + 1):
            for td in range(int(start_xpath[i[1]]), int(end_xpath[i[1]]) + 1):
                print("tr: " + str(tr) + ", td: " + str(td))


        return None

parseRatesTable(None, start_xpath, end_xpath)