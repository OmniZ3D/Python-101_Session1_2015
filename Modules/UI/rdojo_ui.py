import maya.cmds as cmds
import json
import tempfile
 
# Import our json_utils module
import Modules.System.utils as utils
reload(utils)
import Modules.Rigging.rig_arm as rig_arm
 
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
        windowWidth = 110
        windowHeight = 310
        buttonWidth = 100
        buttonHeight = 30
 
        self.UIElements["window"] = cmds.window(windowName, width=windowWidth, height=windowHeight, title="RDojo_UI", sizeable=True)
         
        self.UIElements["guiFlowLayout1"] = cmds.flowLayout(v=False, width=windowWidth, height=windowHeight, bgc=[0.2, 0.2, 0.2])
 
        # Load Layout button
        cmds.separator(p=self.UIElements["guiFlowLayout1"])
        #self.filename = 'joints'
        self.UIElements["loadLayout_button"] = cmds.button(label='load layout', width=buttonWidth, height=buttonHeight, p=self.UIElements["guiFlowLayout1"], c=self.loadLayoutCommand) 
 
        # Save Layout button
        cmds.separator(p=self.UIElements["guiFlowLayout1"])
        self.UIElements["saveLayout_button"] = cmds.button(label='save layout', width=buttonWidth, height=buttonHeight, p=self.UIElements["guiFlowLayout1"], c=self.saveLayoutButton) 
 
        # Rig arm button
        cmds.separator(p=self.UIElements["guiFlowLayout1"])
        self.UIElements["rigarm_button"] = cmds.button(label='rig part', width=buttonWidth, height=buttonHeight, p=self.UIElements["guiFlowLayout1"], c=self.runRigCommand) 

                # Text field for the prefix name
        cmds.separator(w=5, p=self.UIElements["guiFlowLayout1"])
        self.UIElements["prefix_textfield"] = cmds.textField(width=buttonWidth, p=self.UIElements["guiFlowLayout1"])
 
        # Check Box to indicate symmetry
        cmds.separator(w=5, p=self.UIElements["guiFlowLayout1"])
        self.UIElements["symmetry_checkbox"] = cmds.checkBox( label='Symmetry', p=self.UIElements["guiFlowLayout1"])
 
        # Option menu for side
        # Make a list of possible sides
        sides = ['_L', '_R', '_C']
        cmds.separator(w=5, p=self.UIElements["guiFlowLayout1"])
        self.UIElements["side_optionmenu"] = cmds.optionMenu( label='Side', p=self.UIElements["guiFlowLayout1"])
        for s in sides:
            cmds.menuItem(label=s, p=self.UIElements["side_optionmenu"])
 
        #option menu for part of rig to build
        parts = ['arm', 'leg']
        cmds.separator(w=5, p=self.UIElements["guiFlowLayout1"])
        self.UIElements["partMenu"] = cmds.optionMenu( label='Part', p=self.UIElements["guiFlowLayout1"])
        for s in parts:
            cmds.menuItem(label=s, p=self.UIElements["partMenu"])

        """ Show the window"""
        cmds.showWindow(windowName)
     
    def runRigCommand(self, *args):
        prefix = cmds.textField(self.UIElements['prefix_textfield'], q=True, text=True) + '_'
        part = cmds.optionMenu (self.UIElements['partMenu'], value=True, query=True)
        symmetry = cmds.checkBox(self.UIElements["symmetry_checkbox"], value=True, query=True)
        side = cmds.optionMenu (self.UIElements['side_optionmenu'], value=True, query=True)
        rig_arm.makeJoints(self.jntInfo, part, symmetry, prefix, side)

    def loadLayoutCommand(self, *args):
        path = cmds.fileDialog(directoryMask='G:/Users/rogerm/Documents/GitHub/Python-101_Session1_2015/Modules/Layout/*.json')
        self.jntInfo = utils.readJson(path)
        return self.jntInfo           

    def saveLayoutButton(self, *args):
        path = cmds.fileDialog(directoryMask='G:/Users/rogerm/Documents/GitHub/Python-101_Session1_2015/Modules/Layout/*.json', mode =1)
        utils.writeJson(path, self.jntInfo)