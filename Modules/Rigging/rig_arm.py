import maya.cmds as cmds

#create a list containing 4 joints for the arms
armJnt = (['jnt_scapula', [0.25, 10, 0]], ['jnt_shoulder', [2, 10, 0]], ['jnt_elbow', [4, 8, -0.5]], ['jnt_wrist', [6, 6, 0.5]])

#create the joints
for i in armJnt:
    #to check if joint exists, we will use a maya command called objExists.
    #we will also need to use a condition
    #first, tryout cmds.objExists and print out the return
    print cmds.objExists(i[0])
    #Now try using this in a condition.
    if cmds.objExists(i[0]) == True:
        #pass can be used to skip part of the script if a condition is not met.
        pass
    #if previous conditions are not met, then use 'else' to do something else.
    else:
        cmds.joint(n = i[0], p = i[1])