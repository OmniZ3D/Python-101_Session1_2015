import maya.cmds as mc

jointInfo=['arm',[5,0,0]],['elbow',[10,0,-1]],['wrist',[15,0,0]],['wristEnd',[18,0,0]]
prefix='setup_'

def createJoints(jointInfo, prefix):
    for each in jointInfo:
        mc.joint(p=each[1],n=(prefix+each[0]),sym=True)
        #mc.joint(e=True,oj='xyz',secondaryAxisOrient='yup',ch=True,zso=True)
        
        
createJoints(jointInfo, prefix)