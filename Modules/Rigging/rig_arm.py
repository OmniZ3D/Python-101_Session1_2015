import maya.cmds as mc
"""
#jointInfo contains the names of the joints to be created
jointInfo=['arm__1',[5,0,0]],['elbow__1',[10,0,-1]],['wrist__1',[15,0,0]],['wristEnd__1',[18,0,0]]

#prefix and side of the joint chain
prefix = 'setup_'
side = 'l_'
symmetry = True
"""
class Rig_Arm:
    def __init__(self, *args):
        print "In Rig Arm"