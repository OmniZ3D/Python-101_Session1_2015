import maya.cmds as cmds
import json
import tempfile
import os

# Import our json_utils module
import Modules.System.utils as utils
reload(utils)
import Modules.Rigging.rig_arm as rig_arm
reload(rig_arm)
import Modules.System.install as install
reload(install)

# The UI class
class RDojo_UI:

    # The __init__ function
    def __init__(self, *args):
        print 'In RDojo_UI'
        mi = cmds.window('MayaWindow', ma=True, q=True)
        for m in mi:
            if m == 'RDojo_Menu':
                cmds.deleteUI('RDojo_Menu', m=True)
 
        mymenu = cmds.menu('RDojo_Menu', label='RDMenu', to=True, p='MayaWindow')
        cmds.menuItem(label='Rig Tool', parent=mymenu, command=self.ui)

        """ Create a dictionary to store UI elements.
        This will allow us to access these elements later. """
        self.UIElements = {}

    # The function for building the UI
    def ui(self, *args):
        """ Check to see if the UI exists """
        windowName = "Window"
        if cmds.window(windowName, exists=True):
            cmds.deleteUI(windowName)
        """ Define width and height for buttons and windows"""    
        windowWidth = 800
        windowHeight = 60
        buttonWidth = 100
        buttonHeight = 30

        self.UIElements["window"] = cmds.window(windowName, width=windowWidth, height=windowHeight, title="RDojo_UI", sizeable=True)
        
        self.UIElements["guiFlowLayout1"] = cmds.flowLayout(v=False, width=windowWidth, height=windowHeight, wr=True, bgc=[0.2, 0.2, 0.2])

        # Load Layout button
        cmds.separator(w=5, p=self.UIElements["guiFlowLayout1"])
        self.UIElements["loadLayout_button"] = cmds.button(label='load layout', width=buttonWidth, height=buttonHeight, p=self.UIElements["guiFlowLayout1"], c=self.loadLayout) 

        # Save Layout button
        cmds.separator(w=5, p=self.UIElements["guiFlowLayout1"])
        self.UIElements["saveLayout_button"] = cmds.button(label='save layout', width=buttonWidth, height=buttonHeight, p=self.UIElements["guiFlowLayout1"]) 

        # Rig arm button
        cmds.separator(w=5, p=self.UIElements["guiFlowLayout1"])
        self.UIElements["rigarm_button"] = cmds.button(label='rig arm', width=buttonWidth, height=buttonHeight, p=self.UIElements["guiFlowLayout1"], c=self.runRigCommand) 

        # Text field for the prefix name
        cmds.separator(w=5, p=self.UIElements["guiFlowLayout1"])
        self.UIElements["prefix_textfield"] = cmds.textField(width=buttonWidth, p=self.UIElements["guiFlowLayout1"])

        # Check Box to indicate symmetry
        cmds.separator(w=5, p=self.UIElements["guiFlowLayout1"])
        self.UIElements["symmetry_checkbox"] = cmds.checkBox( label='Symmetry', p=self.UIElements["guiFlowLayout1"])

        # Check Box to indicate mirror
        cmds.separator(w=5, p=self.UIElements["guiFlowLayout1"])
        self.UIElements["mirror_checkbox"] = cmds.checkBox( label='Mirror', p=self.UIElements["guiFlowLayout1"])

        # Option menu for side
        # Make a list of possible sides
        sides = ['l_', 'r_', 'c_']
        cmds.separator(w=5, p=self.UIElements["guiFlowLayout1"])
        self.UIElements["side_optionmenu"] = cmds.optionMenu( label='Side', p=self.UIElements["guiFlowLayout1"])
        for s in sides:
			cmds.menuItem(label=s, p=self.UIElements["side_optionmenu"])

        """ Show the window"""
        cmds.showWindow(windowName)
    
    def runRigCommand(self, *args):
        mirror = cmds.checkBox(self.UIElements['mirror_checkbox'], q=True, value=True)
        rig_arm.Rig_Arm(mirror)

    def loadLayout(self, *args):
    	# Pull all the options from the UI
    	""" We will use the same commands we used to build the UI Elements,
    	but this time we will run the flags in query mode """
    	side = cmds.optionMenu(self.UIElements['side_optionmenu'], q=True, v=True) 
    	prefix = cmds.textField(self.UIElements['prefix_textfield'], q=True, text=True)
    	""" For those of you running Maya 2013, consider how you could use 
    	symmetry to mirror joints later """
    	symmetry = cmds.checkBox(self.UIElements['symmetry_checkbox'], q=True, value=True)
        mirror = cmds.checkBox(self.UIElements['mirror_checkbox'], q=True, value=True)
        # Since we are only making an arm, we can make a static path to the arm.json file here.
        # What if we had a leg.json as well?
        layoutfile = os.environ["RDOJO"] + "Modules/Layout/arm.json"
        install.installLayout(layoutfile, side, prefix, symmetry, mirror)

        

