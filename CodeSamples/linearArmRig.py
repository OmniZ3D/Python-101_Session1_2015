# This script builds an arm rig


""" The first section is all about creating joints """
# First we define the positions and names of our joints.
jntinfo = ["arm", [5, 0, 0]], ["elbow", [10, 0, -1]], ["wrist", [15, 0, 0]], ["wristEnd", [18, 0, 0]]

# Loop through jntinfo and build rig joints.
rigjnts = []
for j in jntinfo:
    jnt = cmds.joint(name='rigj_'+ j[0], p=j[1])
    rigjnts.append(jnt)
    
# Deselect everything.
cmds.select(d=True)

# Loop through jntinfo and build fk joints.
fkjnts = []
for j in jntinfo:
    jnt = cmds.joint(name='fkj_'+ j[0], p=j[1])
    fkjnts.append(jnt)
    
# Deselect everything.
cmds.select(d=True)

# Loop through jntinfo and build ik joints.
ikjnts = []
for j in jntinfo:
    jnt = cmds.joint(name='ikj_'+ j[0], p=j[1])
    ikjnts.append(jnt)
    
# Deselect everything.
cmds.select(d=True)

""" Coneect the joints with a parent constraint """
constraints = []
for i in range(len(rigjnts)):
    parentcon = cmds.parentConstraint(fkjnts[i], ikjnts[i], rigjnts[i], mo=True)
    constraints .append(parentcon)
    
""" Create fk controls.  We can do this many ways.  For instance we could dynamically
draw a nurbs curve shape, or we could import a control object.  For now we will use a nurbs circle. """

# Make an empty list to store controls and groups.
# We will use this later to make the control hierarchy.
ctrllst=[]

for j in range(len(fkjnts)):
    # We dont want a control for the end joint.
    if j != 3: 
        # Get the position and rotation of each fk joint
        pos = cmds.xform(fkjnts[j], q=True, ws=True, t=True)
        rot = cmds.xform(fkjnts[j], q=True, ws=True, ro=True)
        ctrlname = fkjnts[j].replace('fkj_', 'ctrl_')
        ctrl = cmds.circle(name=ctrlname, nr=(1, 0, 0))
        # Make an empty group and parent the control under it.
        grp = cmds.group(empty=True, name='grp_' + ctrlname)
        cmds.parent(ctrl[0], grp)
        # Move the group to the joint.
        cmds.xform(grp, ws=True, t=pos)
        cmds.xform(grp, ws=True, ro=rot)
        ctrllst.append([ctrl, grp])
        # Constrain the fk joint to the control.
        cmds.parentConstraint(ctrl[0], fkjnts[j], mo=True)
        
# Now setup the control hierarchy.
for c in range(len(ctrllst)):
    if c != 0:
        cmds.parent(ctrllst[c][1], ctrllst[c-1][0]) 
        
""" Setup the ik arm with controls and an ik handle """
ikh = cmds.ikHandle( n='arm_ikh', sj=ikjnts[0], ee=ikjnts[2], sol='ikRPsolver')   
pos = cmds.xform(ikjnts[2], q=True, ws=True, t=True)
rot = cmds.xform(ikjnts[2], q=True, ws=True, ro=True)
ikctrlname = ikjnts[2].replace('ikj_', 'ctrl_ik_')
ikctrl = cmds.circle(name=ikctrlname, nr=(1, 0, 0))
ikcgrp = cmds.group(empty=True, name='grp_' + ctrlname)
cmds.parent(ikctrl[0], ikcgrp)
cmds.xform(ikcgrp, ws=True, t=pos)
cmds.xform(ikcgrp, ws=True, ro=rot)
# Constrain the ik handle to the ik control.
cmds.pointConstraint(ikctrl[0], ikh[0])

""" Now we need to find the position for the pole vector.  This is a little tricky.
When we manually rig an arm we just snap the pv to the elbow and translate it back. """
from maya import cmds , OpenMaya

start = cmds.xform(ikjnts[0] ,q=True ,ws=True, t=True)
mid = cmds.xform(ikjnts[1] ,q=True ,ws=True, t=True)
end = cmds.xform(ikjnts[2] ,q=True ,ws=True, t=True)
startV = OpenMaya.MVector(start[0] ,start[1],start[2])
midV = OpenMaya.MVector(mid[0] ,mid[1],mid[2])
endV = OpenMaya.MVector(end[0] ,end[1],end[2])
startEnd = endV - startV
startMid = midV - startV
dotP = startMid * startEnd
proj = float(dotP) / float(startEnd.length())
startEndN = startEnd.normal()
projV = startEndN * proj
arrowV = startMid - projV
arrowV*= 0.5
finalV = arrowV + midV
pvloc = cmds.spaceLocator(n='arm_pv')[0]
cmds.xform(pvloc , ws=True , t= (finalV.x , finalV.y ,finalV.z))

# Create a polvector constraint between the pv and the ik handle.
cmds.poleVectorConstraint(pvloc, ikh[0] )

# To finish the ik setup, we constrain the ik wrist joint to the ik control.
cmds.orientConstraint(ikctrl[0], ikjnts[2])

# Setup the ik/fk switch.
""" Its up to you where the switch attribute lives.  For now we 
will create an extra control object for arm settings. """
settingsctrl = cmds.circle(name="ctrl_settings", nr=(1, 0, 0))
# Use addAttr to create an ik fk attribute.
cmds.addAttr(settingsctrl, ln="ik_fk", at = "enum", en ="ik:fk:", k=True )

""" To do the switch we will toggle the parent constraint between the 
ik and fk joints.  Enum attributes have a value of 0(off) and 1(on).
So when we want to switch to ik we can just make a direct connection, but we will
need to reverse those values to switch to fk.  For this we will use a reverse node."""
for c in range(len(constraints)): 
    cmds.connectAttr(settingsctrl[0] + '.ik_fk', constraints[c][0] + '.' + fkjnts[c] + 'W0')
    revnode = cmds.shadingNode("reverse", asUtility=True, n='revnode_ikfk')
    cmds.connectAttr(settingsctrl[0] + '.ik_fk', revnode + '.inputX')
    cmds.connectAttr(revnode + '.outputX', constraints[c][0] + '.' + ikjnts[c] + 'W1')