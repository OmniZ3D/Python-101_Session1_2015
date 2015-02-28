import maya.cmds as cmds
jointinfo = (['joint_shoulder', [1.0, 5.0,0.0]],['joint_upperarm', [2.0, 5.0, 0.0]],['joint_lowerarm', [4.0, 4.0, -1.0]],['joint_hand', [6.0, 3.0, 0.0]],['temp', [8.0, 2.0, 1.0]])
print jointinfo

cmds.select(d=True)
i = 0
for item in jointinfo:
        print item
        j = cmds.joint(n=item[0], p=item[1], rad=0.1)
        if i > 0:
            cmds.joint( jointinfo[i-1][0], e=True, zso=True, oj='xyz', sao='zup' )
        i+=1
cmds.delete ('temp')
