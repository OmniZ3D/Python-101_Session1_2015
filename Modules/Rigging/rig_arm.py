import maya.cmds as cmds
import Modules.System.utils as utils

fileName = "C:/Users/A/Documents/GitHub/Python-101_Session1_2015/Modules/Layout/arm.json"

data = utils.readJson(fileName)
info = utils.json.loads(data)

prefix = "L_"

def createJoints(prefix):
    cmds.select(cl=True)
    for i in info["arm"]:
        jointName = prefix + i[0]
        if cmds.objExists(jointName) == True:
            print "Joint exists!!"
            break
        else:
            cmds.joint(n=jointName, p=i[1])
            print "%s done!" % jointName
    cmds.select(cl=True)
            
createJoints(prefix)