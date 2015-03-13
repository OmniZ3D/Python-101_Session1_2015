# Import the Python json module
import json 
# Here are a couple of simple functions to read and write json data.
def writeJson(fileName, data):
    with open(fileName, 'w') as outfile:
        json.dump(data, outfile)
  
    file.close(outfile)
  
def readJson(fileName):
    with open(fileName, 'r') as infile:
        data = (open(infile.name, 'r').read())
    return data