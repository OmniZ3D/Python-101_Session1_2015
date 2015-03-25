import maya.cmds as cmds
import json
import Modules.System.utils as utils 
# Read the json file

class makeJoints:

    def __init__(self, jntInfo, part, symmetry, prefix):
        #set joint attributes
        side='_L'
        self.joints(jntInfo, part, symmetry, side, prefix)

        #function to create joints from json library with symmetry and a prefix
    def joints(self, jntInfo, part, symmetry, side, prefix):
        cmds.select(d=True)
        jntNum = 0
        while jntNum < len(jntInfo[part]):
            jntName = prefix + jntInfo[part][jntNum][0] + side
                #check for existing joint jntName and make new name if exists
            if cmds.objExists(jntName) ==True:  
                self.generateNewJointName(jntInfo, part, jntNum)
                jntName = prefix + jntInfo[part][jntNum][0] + side
                #create joint jntName and rename if symmetry == True
            cmds.joint(position=jntInfo[part][jntNum][1], name=jntName, symmetry=symmetry)
            if symmetry==True:
                cmds.rename(jntName + '1', prefix + jntInfo[part][jntNum][0] + '_R')
                cmds.select(d=True)
            jntNum +=1
            #parent joints into chain
        posChild=len(jntInfo[part])-1
        posParent=posChild - 1
        while(posChild>=1):
            cmds.parent(prefix + jntInfo[part][posChild][0] + side, prefix + jntInfo[part][posParent][0] + side)
            if symmetry==True:
                cmds.parent(prefix + jntInfo[part][posChild][0] + '_R', prefix + jntInfo[part][posParent][0] + '_R')
            posChild-=1
            posParent-=1
        cmds.select(d=True)
        cmds.joint (prefix + jntInfo[part][0][0] + side, e=True, oj='xyz', secondaryAxisOrient='yup', ch=True,zso=True)

        #create a new name for joints if alreayd exists
    def generateNewJointName(self, jntInfo, part, jntNum):
        jntNameLength = len(jntInfo[part][jntNum][0])
        jntInstant = int(jntInfo[part][jntNum][0][jntNameLength-2:jntNameLength])
        jntInstant += 1
        if jntInstant >=10:
            jntInfo[part][jntNum][0] = jntInfo[part][jntNum][0][0:jntNameLength-2] + str(jntInstant)
        else:
            jntInfo[part][jntNum][0] = jntInfo[part][jntNum][0][0:jntNameLength-2] + '0' + str(jntInstant)
        return jntInfo