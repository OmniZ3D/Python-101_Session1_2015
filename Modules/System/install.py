import maya.cmds as cmds
import utils as utils
reload(utils)
import json

def installLayout(layoutfile, side, prefix, symmetry):
	data = utils.readJson(layoutfile)
	# Load the data as a dictionary
	info = json.loads(data)
	jointInfo = info['Arm']
	print "Here is the info loaded from the json file"
	print jointInfo
	print "Here are the options from the UI"
	print (side, prefix, symmetry)

	# Now we have all the data we need to build the joints
	jntinfo = utils.createJoints(jointInfo, prefix, side, symmetry)

	""" Now I will introduce you to an asset.  An asset is like a 
	group with more options.  Assets can even hold non-dag nodes.
	We can put all of our joints and constraints into an asset.
	If you don't have the symmetry joint option, you can tag
	the asset as mirrored by adding Mirror to the asset name """

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

