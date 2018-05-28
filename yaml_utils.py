# To install module, please enter command in terminal:
# pip install pyyaml
import yaml
import os

# This class contains all methods to handle YAML files
class YAMLUtils(object):
    # File Name
    FILE_NAME = 'financial-institution-config.yaml'

    # Method reads YAML File
    @staticmethod
    def readYAML(file_name):
        if (os.path.isfile(file_name)):
            with open(file_name, "r") as stream:
                try:
                    data = yaml.load(stream)['root']
                    return data
                except yaml.YAMLError as exc:
                    print("YAML Error: " + exc)
        else:
            print("File <" + file_name + "> does not exist!")
            return None
            