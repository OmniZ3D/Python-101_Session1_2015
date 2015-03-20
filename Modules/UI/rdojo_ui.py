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
        self.UIElements["saveLayout_button"] = cmds.button(label='save layout', width=buttonWidth, height=buttonHeight, p=self.UIElements["guiFlowLayout1"]) 
 
        # Rig arm button
        cmds.separator(p=self.UIElements["guiFlowLayout1"])
        self.part = 'arm'
        self.symmetry = True
        self.prefix = 'setup_'
        self.UIElements["rigarm_button"] = cmds.button(label='rig arm', width=buttonWidth, height=buttonHeight, p=self.UIElements["guiFlowLayout1"], c=self.runRigCommand) 
 
        """ Show the window"""
        cmds.showWindow(windowName)
     
    def runRigCommand(self, *args):
        rig_arm.makeJoints(self.jntInfo, self.part, self.symmetry, self.prefix)

    def loadLayoutCommand(self, *args):
        path = 'G:/Users/rogerm/Documents/GitHub/Python-101_Session1_2015/Modules/Layout/'
        self.jntInfo = utils.readJson(path + 'joints.json')
        return self.jntInfo           