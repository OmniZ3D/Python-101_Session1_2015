import maya.cmds as cmds
import utils as utils
reload(utils)
import json

def installLayout(layoutfile, side, prefix, symmetry, mirror):
    data = utils.readJson(layoutfile)
    # Load the data as a dictionary
    info = json.loads(data)
    jointInfo = info['Arm']

    # Now we have all the data we need to build the joints
    jntinfo = utils.createLytJoints(jointInfo, prefix, side, symmetry)

    assetname = 'Layout_' + side + prefix 
    lytast = cmds.container(n=assetname)
    cmds.addAttr(lytast, shortName="type", longName="type", dt='string', keyable=False)
    cmds.setAttr(lytast + '.type', prefix, type='string')

    if symmetry == True:
        mirassetname = 'LayoutMirror_' + side + prefix 
        mirrorlytast = cmds.container(n=mirassetname)
        cmds.addAttr(mirrorlytast, shortName="type", longName="type", dt='string', keyable=False)
        cmds.setAttr(mirrorlytast + '.type', prefix, type='string')
        # Add mirror attribute
        cmds.addAttr(lytast, shortName="mirror", longName="mirror", dt='string', keyable=False)
        cmds.setAttr(lytast + '.mirror', mirassetname, type='string')
        """
        If you don't have the symmetry joint option,
        you could add a "mirror attribute here".  
        In rig arm a mirrored arm rig could be created 
        if a layout asset has the mirror attribute.
        """
    if mirror == True:
        mirassetname = 'LayoutMirror_' + side + prefix 
        cmds.addAttr(lytast, shortName="mirror", longName="mirror", dt='string', keyable=False)
        cmds.setAttr(lytast + '.mirror', mirassetname, type='string')
        
    for j in jntinfo:
        cmds.container(lytast, edit=True, an=j[0])
        # Check for symmetry
        if symmetry == True:
            cmds.container(mirrorlytast, edit=True, an=j[1])

        

