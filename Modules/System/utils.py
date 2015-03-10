import json
import os

#Mydictionnary = {}
fileName = 'C:/Users/Seb/Documents/GitHub/Python-101_Session1_2015/Modules/Layout/temp.json'
dir = os.path.dirname(fileName)
data = ''
#writeJson(fileName, data)

#Write Json

def writeJson(fileName, data):
    if not os.path.exists(dir):
            os.makedirs(dir)
    with open(fileName,'w') as outfile:
        json.dump(data, outfile)
        
    file.close(outfile)

#read Json

def readJson(fileName):
    with open (fileName, 'r') as infile:
        date = (open(infile.name, 'r').read())
    return data