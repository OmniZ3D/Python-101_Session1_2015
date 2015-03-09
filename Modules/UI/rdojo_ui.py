import maya.cmds as cmds

class RDojo_UI:

	def runCmd(*args):
		from Modules.Rigging import rig_arm
		reload(rig_arm)

	def __init__(self, *args):
		mi = cmds.window("MayaWindow", ma=True, q=True)
		for m in mi:
			if m ==  "RDojoMenu":
				cmds.showWindow("RDojoMenu")

		myMenu = cmds.menu("RDojoMenu", label="RDMenu", to=True, p="MayaWindow")
		cmds.menuItem(l="Rig Tools", parent=myMenu, c=self.ui)
		self.UIElements= {}

	def ui(self, *args):
		if cmds.window("rigTool", ex=True):
			cmds.deleteUI("rigTool")
		cmds.window("rigTool", t="Rig Tool", w=110, h=310, s=False)
		cmds.rowLayout(nc=3)
		cmds.button(l="Save layout", w=100, h=30)
		cmds.button(l="Load layout", w=100, h=30)
		cmds.button(l="Rig arm", w=100, h=30, c=self.runCmd)
		cmds.showWindow()