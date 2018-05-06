from yaml_utils import YAMLUtils
from csv_utils import CSVUtils
from http_utils import HttpUtils

url = "http://www.rbcroyalbank.com/rates/persacct.html"
print(HttpUtils.getSourceCode(url) )