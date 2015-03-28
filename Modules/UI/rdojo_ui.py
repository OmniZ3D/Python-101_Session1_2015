import maya.cmds as cmds
import json
import tempfile
import os

#Import json_utils module
import Modules.Utils.utils as utils
reload(utils)
import Modules.Rigging.rig_arm as rig_arm
reload(rig_arm)
import Modules.System.install as install
reload(install)

#UI Class
class RDojo_UI:

    #init function
    def __init__(self,*args):
        print 'In RDojo_UI'
        mi = cmds.window('MayaWindow', ma=True, q=True)
        for m in mi:
            if m == 'RDojo_Menu':
                cmds.deleteUI('RDojo_Menu', m=True)

        mymenu = cmds.menu('RDojo_Menu', label='RDMenu', to=True, p='MayaWindow')
        cmds.menuItem(label='Rig Tool', parent=mymenu, command=self.ui)

        #Create dictionary for UI elements
        self.UIElements = {}

    def ui(self,*args):
        windowName = "Window"
        if cmds.window(windowName,exists=True):
            cmds.deleteUI(windowName)
        windowWidth = 800
        windowHeight = 60
        buttonWidth = 100
        buttonHeight = 30

        self.UIElements["window"] = cmds.window(windowName, width=windowWidth, height=windowHeight, title="RDojo_UI", bgc=[0.2,0.2,0.2], sizeable=True)
        self.UIElements["guiFlowLayout1"] = cmds.flowLayout(v=False,width=windowWidth,height=windowHeight,wr=True,bgc=[0.2,0.2,0.2])

        #Layout Button
        cmds.separator(w=5,p=self.UIElements["guiFlowLayout1"])
        self.UIElements["loadLayout_button"] = cmds.button(label='load layout', width=buttonWidth,height=buttonHeight,p=self.UIElements["guiFlowLayout1"],c=self.loadLayout)

        #Save Layout Button
        cmds.separator(w=5,p=self.UIElements["guiFlowLayout1"])
        self.UIElements["saveLayout_button"] = cmds.button(label='save layout',width=buttonWidth,height=buttonHeight,p=self.UIElements["guiFlowLayout1"])

        #Rig Arm Button
        cmds.separator(w=5,p=self.UIElements["guiFlowLayout1"])
        self.UIElements["rigarm_button"] = cmds.button(label='rig arm',width=buttonWidth,height=buttonHeight,p=self.UIElements["guiFlowLayout1"],c=self.runRigCommand)

        #Text field for prefix name
        cmds.separator(w=5,p=self.UIElements["guiFlowLayout1"])
        self.UIElements["prefix_textfield"] = cmds.textField(width=buttonWidth, p=self.UIElements["guiFlowLayout1"])

        #Checkbox for symmetry on/off
        cmds.separator(w=5,p=self.UIElements["guiFlowLayout1"])
        self.UIElements["symmetry_checkbox"] = cmds.checkBox(label='Symmetry', p=self.UIElements["guiFlowLayout1"])

        #option menu for side
        sides = ['_l_','_r_', '_c_']
        cmds.separator(w=5,p=self.UIElements["guiFlowLayout1"])
        self.UIElements["side_optionmenu"] = cmds.optionMenu(label='Side', p=self.UIElements["guiFlowLayout1"])
        for s in sides:
            cmds.menuItem(label=s,p=self.UIElements["side_optionmenu"])

        #show window
        cmds.showWindow(windowName)

    def runRigCommand(self,*args):
        rig_arm.Rig_Arm()

    def loadLayout(self,*args):
        side=cmds.optionMenu(self.UIElements['side_optionmenu'],q=True,v=True)
        prefix=cmds.textField(self.UIElements['prefix_textfield'],q=True,text=True)
        symmetry=cmds.checkBox(self.UIElements['symmetry_checkbox'],q=True,value=True)

        #static path to json file
        layoutfile = os.environ["RDOJO"] + "/Modules/Layout/arm.json"
        install.installLayout(layoutfile,side,prefix,symmetry)


