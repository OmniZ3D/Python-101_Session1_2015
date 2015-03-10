import maya.cmds as cmds

# Create a variable to store name and position
limbProxy = (['clavicle', [0.5, 5.0, 0.0]], ['shoulder', [1, 5.0, 0.0]], ['elbow', [2.5, 5.0, -.25]], ['wrist', [4.0, 5.0, 0.0]])

# Suffix and Mirror
suffix = 'PXY'
mirror = 'True'

# Not sure I'm keeping this function - just experimenting for now
def getPrefix(limbProxy):
	# This function looks at the x position of the first joint and assigns l or r. Maybe there's a better/smarter way to do this?
	prefix = ''
	if limbProxy[0][1][0] > 0:
		prefix = 'l'
	else:
		prefix = 'r'
	return prefix

# Prefix
prefix = getPrefix(limbProxy)

# Function to create limb proxy joints
def createProxyJoints(limbProxy, prefix, suffix, mirror):
	for i in limbProxy:
		# create the proxy joints
		proxy = cmds.joint(position = i[1], name = prefix + '_' + i[0] + '_' + suffix, radius = .25)
	cmds.select(deselect = True)

createProxyJoints(limbProxy, prefix, suffix, mirror)