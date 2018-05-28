class FinancialInstitution(object):
    # This are the fields that would be printed in the cvs file
    def __init__(self, bank_name, account_name, account_range, rate):
        self.bank_name = bank_name
        self.account_name = account_name
        self.account_range = account_range
        self.rate = rate

        