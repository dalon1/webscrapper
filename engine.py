from yaml_utils import YAMLUtils
from csv_utils import CSVUtils
from http_utils import HttpUtils
from parser_utils import ParserUtils
from financial_institution import FinancialInstitution

def main():
    banks = YAMLUtils.readYAML(YAMLUtils.FILE_NAME)
    
    for bank in banks:
        # Just demo for Simplii
        if bank['name'] != 'Simplii':
            break
        
        source = HttpUtils.getSourceCode(bank['url'])
        for account in bank['accounts']:
            account_name = ParserUtils.parseAccountName(source, account['account_name_xpath'])
            #fi = FinancialInstitution(bank['name'], account_name, "", "")
            ParserUtils.parseRatesTable(source, account['account_rates_start'], account['account_rates_end'])


main()