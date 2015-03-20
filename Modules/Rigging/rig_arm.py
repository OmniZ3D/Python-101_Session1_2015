import maya.cmds as cmds
import json
import Modules.System.utils as utils 
# Read the json file

class makeJoints:

    def __init__(self, jntInfo, part, symmetry, prefix):

        #read joint info for the joints

        #set joint attributes
        side='_L'
        
        #make the joints
        self.joints(jntInfo[part], symmetry, side, prefix)
    def joints(self, jntInfo, symmetry, side, prefix):
        cmds.select(d=True)
        for item in jntInfo:
            cmds.joint(position=item[1], name=prefix + item[0] + side, symmetry=symmetry)
            if symmetry==True:
                cmds.rename(prefix + item[0] + side + '1' , prefix + item[0] + '_R')
            cmds.select(d=True)
        posChild=len(jntInfo)-1
        posParent=posChild - 1
        while(posChild>=1):
            cmds.parent(prefix + jntInfo[posChild][0] + side, prefix + jntInfo[posParent][0] + side)
            if symmetry==True:
                cmds.parent(prefix + jntInfo[posChild][0] + '_R', prefix + jntInfo[posParent][0] + '_R')
            posChild-=1
            posParent-=1
        cmds.select(d=True)
        cmds.joint (prefix + jntInfo[0][0] + side, e=True, oj='xyz', secondaryAxisOrient='yup', ch=True,zso=True)
