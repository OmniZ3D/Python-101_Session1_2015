import maya.cmds as cmds
# The UI class
class RDojo_UI:

	# The __init__ function
	# Please look at this documentation
	# http://docs.python.org/2/tutorial/classes.html
	def __init__(self):
		print 'In RDojo_UI'

	# The function for building the UI
	def ui(self, *args):
		""" Create a dictionary to store UI elements.
		This will allow us to access these elements later. """
        self.UIElements = {}

        """ Check to see if the UI exists """
        windowName = "Window"
        if cmds.window(self.windowName, exists=True):
            cmds.deleteUI(self.windowName)
        """ Define width and height for buttons and windows"""    
        windowWidth = 40
        windowHeight = 110
        buttonWidth = 100
        buttonHeight = 30

        self.UIElements["window"] = cmds.window(self.windowName, 
        	width=self.windowWidth, 
        	height=self.windowHeight, 
        	title="Window", sizeable=True)
        
        self.UIElements["guiFlowLayout1"] = cmds.flowLayout(v=False, 
        	width=220, height=self.windowHeight, 
        	bgc=[0.2, 0.2, 0.2])