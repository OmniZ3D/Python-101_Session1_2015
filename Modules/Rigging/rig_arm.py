import maya.cmds as cmds
import json
import Modules.System.utils as utils 
# Read the json file

class makeJoints:

    def __init__(self, jntInfo, part, symmetry, prefix, side):
        #set joint attributes
        self.joints(jntInfo, part, symmetry, side, prefix)

        #function to create joints from json library with symmetry and a prefix
    def joints(self, jntInfo, part, symmetry, side, prefix):
        jointlist = []
        #jointCount=len(jointlist)
        #jointCount +=1
        if side == '_L':
            symSide='_R'
        if side =='_R':
            symSide='_L'
        cmds.select(d=True)
        
        for each in jntInfo[part]:
            if side == '_R':
                each[1][0] *= -1
            jntName = prefix + self.generateNewJointName(prefix, each[0], side, symSide)
            symName= jntName + symSide
            jntName += side


            cmds.joint(position=each[1], name=jntName, symmetry=symmetry)
            cmds.select(d=True)
            
            if symmetry==True:
                jntNameLength = len(jntName)
                cmds.rename(jntName[0:jntNameLength-2] + side + str('1'), jntName[0:jntNameLength-2] + symSide)
                symName=jntName[0:jntNameLength-2] + symSide
                jntName=jntName[0:jntNameLength-2] + side
                jointlist.append([jntName, symName])
            else:
                jointlist.append([jntName, None])
            cmds.select(d=True)        
            if side == '_R':
                each[1][0] *= -1
        for each in range(len(jointlist)):
            if each != 0:
                cmds.parent(jointlist[each][0], jointlist[each-1][0])
                if symmetry == True and each != 0:
                    cmds.parent(jointlist[each][1], jointlist[each-1][1])
        print jointlist






#        cmds.joint (prefix + jntInfo[part][0][0] + side, e=True, oj='xyz', secondaryAxisOrient='yup', ch=True,zso=True)

        #create a new name for joints if alreayd exists
    def generateNewJointName(self, prefix, part, side, symSide):
        jntNameLength = len(part)
        jntInstant = int(part[jntNameLength-2:jntNameLength])
        while (cmds.objExists(prefix + part[0:jntNameLength-1] + str(jntInstant) + side)==True or cmds.objExists(prefix + part[0:jntNameLength-1] + str(jntInstant) + symSide)==True) and jntInstant < 10:
            jntInstant +=1
        if jntInstant >=10:
            while (cmds.objExists(prefix + part[0:jntNameLength-2] + str(jntInstant) + side)==True or cmds.objExists(prefix + part[0:jntNameLength-2] + str(jntInstant) + symSide)==True):
                jntInstant +=1
            jntName = part[0:jntNameLength-2] + str(jntInstant)
        else:
            jntName = part[0:jntNameLength-2] + '0' + str(jntInstant)
        return jntName



