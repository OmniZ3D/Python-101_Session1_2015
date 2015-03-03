import maya.cmds as cm

cm.joint(n='jnt_clavicle',p=(2.0,0.0,0.0))
cm.joint(n='jnt_shoulder',p=(6.0,0.0,0.0))
cm.joint(n='jnt_elbow',p=(12.0,0.0,-2.0))
cm.joint(n='jnt_wrist',p=(18.0,0.0,0.0))

cm.joint('jnt_clavicle',e=True,oj='xyz',sao='xup')
cm.joint('jnt_shoulder',e=True,oj='xyz',sao='xup')
cm.joint('jnt_elbow',e=True,oj='xyz',sao='xup')
cm.joint('jnt_wrist',e=True,o=(0,0,0))