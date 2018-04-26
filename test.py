import yaml

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
            builDictionary(yaml.load(stream)['army'])
            #print(yaml.load(stream)['army'])
        except yaml.YAMLError as exc:
            print("Error: " + exc)

 

readYaml(FILE_NAME)