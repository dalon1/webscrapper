from yaml_utils import YAMLUtils
from csv_utils import CSVUtils

def callStatic():
    data = YAMLUtils.readYAML("financial-institution-config.yaml")
    records = CSVUtils.createCSVRecord(data)
    CSVUtils.createCSVFile("csv_financial.csv", records)
    
callStatic()