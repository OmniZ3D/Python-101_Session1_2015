import maya.cmds as cmds
import json

def readJson(fileName):
    with open(fileName, 'r') as infile:
        data = (open(infile.name, 'r').read())
    return data
    
def createArmSkeleton():
    
    #open json file
    fileName = 'F:/Documents/Python-101_Session1_2015/Modules/Layout/arm.json'
    
    # Read the json file
    data = readJson(fileName)
    
    #.loads, loads the json data to memory.
    info = json.loads( data )
    
    for key, value in info.iteritems():
        for i in range(4):
            jnt =cmds.joint( p=(value[i][1]), n=( 'l_'+value[i][0]+'_lyt_JNT'))
            cmds.joint(jnt, e=True,oj='xyz',secondaryAxisOrient='yup',ch=True,zso=True)
            #print value[i][0]
    
createArmSkeleton()    
    