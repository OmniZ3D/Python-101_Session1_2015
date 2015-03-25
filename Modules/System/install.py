import maya.cmds as cmds
import Modules.Utils.utils as utils
reload(utils)
import json

def installLayout(layoutfile, side, prefix, symmetry):
    data = utils.readJson(layoutfile)

    #load data as a dictionary
    info = json.loads(data)
    jointInfo = info['Arm']

    print "Here is the info loaded from the json file"
    print jointInfo
    print "Here are the options from the UI"
    print (side, prefix, symmetry)

    #data to build the joints
    jntinfo = utils.createJoints(jointInfo, prefix, side, symmetry)

    assetname = 'Layout_' + side + prefix
    lytast = cmds.container(n=assetname)

    if symmetry == True:
            mirassetname = 'LayoutMirror_' + side + prefix
            mirrorlytast = cmds.container(n=mirassetname)
    for j in jntinfo:
        cmds.container(lytast, edit=True, an=j[0])

        # Check for symmetry
        if symmetry == True:
            cmds.container(mirrorlytast, edit=True, an=j[1])