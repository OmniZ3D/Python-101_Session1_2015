import maya.cmds as cmds

def runCmd(*args):
	print args
	from Modules.Rigging import rig_arm

def createMenu(*args):
	mi = cmds.window("MayaWindow", ma=True, q=True)
	for m in mi:
		if m ==  "RDojoMenu":
			cmds.deleteUI("RDojoMenu", m=True)

	myMenu = cmds.menu("RDojoMenu", label="RDMenu", to=True, p="MayaWindow")
	cmds.menuItem(l="Rig Arm", parent=myMenu, c=runCmd)

createMenu()