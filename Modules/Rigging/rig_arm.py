import maya.cmds as cmds
prefix_name = "L_arm"

jntList = [['Limb01_JNT', [2,0,0]], ['Limb02_JNT', [7,0,-2]], ['Limb03_JNT', [12,0,0]],  ['LimbEnd_JNT', [14,0,0]]]
def createLimb(jntList, prefix_name):
    jnt = []
    for c in jntList:
        jnt.append(cmds.joint(p=c[1], n= prefix_name + c[0]))

    for d in jnt:
        cmds.joint(d, edit = True, orientJoint = "xyz", secondaryAxisOrient = "yup", zso = True)
     
		
		
createLimb(jntList, prefix_name)
