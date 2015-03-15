import maya.cmds as cmds

name = ['upperArm', 'lowerArm', 'hand', 'handEnd']
for i in range(4):    
    cmds.joint( p=(i, 0, 0), n=( 'l_'+name[i]+'_JNT'))