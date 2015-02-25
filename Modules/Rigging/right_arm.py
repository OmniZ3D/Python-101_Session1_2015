import maya.cmds as cmds
 
joinlist = (["shoulder_j", [1,10,0]], ["arm_j", [2,10,0]], ["elbow_j", [6,10,0]], ["forearm_j", [10,10,0]])
for item in joinlist:
    cmds.joint (n=item[0], p=item[1])
