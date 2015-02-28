import maya.cmds as cmds

#create a list containing 4 joints for the arms
armJnt = (['jnt_scapula', [0.25, 10, 0]], ['jnt_shoulder', [2, 10, 0]], ['jnt_elbow', [4, 8, -0.5]], ['jnt_wrist', [6, 6, 0.5]])

#create the joints
for i in armJnt:
    cmds.joint(n = i[0], p = i[1])