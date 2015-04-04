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

        """ This dictionary will store data from the lyout.json files """
        self.layout_info = {}

        """ Call the internal method loadLayoutDefinitions()
            The loadLayoutDefinitions method will read all the json files
            in the layout folder.  Then it will store the data
            in self.part_info.  Remember that we use self when
            calling a method of the class we are in."""

        self.loadLayoutDefinitions()

        # This dictionary will store all of the available rigging modules.
        self.rigmodlst = os.listdir(os.environ["RDOJO"] + 'Modules/Rigging/')

    # The function for building the UI
    def ui(self, *args):
        """ Check to see if the UI exists """
        windowName = "Window"
        if cmds.window(windowName, exists=True):
            cmds.deleteUI(windowName)
        """ Define width and height for buttons and windows"""    
        windowWidth = 480
        windowHeight = 80
        buttonWidth = 100
        buttonHeight = 30

        self.UIElements["window"] = cmds.window(windowName, width=windowWidth, height=windowHeight, title="RDojo_UI", sizeable=True)

        self.UIElements["mainColLayout"] = cmds.columnLayout( adjustableColumn=True )
        self.UIElements["guiFrameLayout1"] = cmds.frameLayout( label='Layout', borderStyle='in', p=self.UIElements["mainColLayout"] )
        self.UIElements["guiFlowLayout1"] = cmds.flowLayout(v=False, width=windowWidth, height=windowHeight/2, wr=True, bgc=[0.2, 0.2, 0.2], p=self.UIElements["guiFrameLayout1"])
        
        # Menu listing all the layout files.
        cmds.separator(w=10, hr=True, st='none', p=self.UIElements["guiFlowLayout1"])
        self.UIElements["keyMenu"] = cmds.optionMenu('layouts', label='Layouts',  p=self.UIElements["guiFlowLayout1"])

        # Create a menu item for each json file in the Layout directory.
        for key in self.layout_info['Keys']:  
            cmds.menuItem(label=key + '_', p=self.UIElements["keyMenu"])

        # Check Box to indicate symmetry
        cmds.separator(w=10, hr=True, st='none', p=self.UIElements["guiFlowLayout1"])
        self.UIElements["symmetry_checkbox"] = cmds.checkBox( label='Symmetry', p=self.UIElements["guiFlowLayout1"])

        # Check Box to indicate mirror
        cmds.separator(w=10, hr=True, st='none', p=self.UIElements["guiFlowLayout1"])
        self.UIElements["mirror_checkbox"] = cmds.checkBox( label='Mirror', p=self.UIElements["guiFlowLayout1"])

        # Option menu for side
        # Make a list of possible sides
        sides = ['l_', 'r_', 'c_']
        cmds.separator(w=10, hr=True, st='none', p=self.UIElements["guiFlowLayout1"])
        self.UIElements["side_optionmenu"] = cmds.optionMenu( label='Side', p=self.UIElements["guiFlowLayout1"])
        for s in sides:
            cmds.menuItem(label=s, p=self.UIElements["side_optionmenu"])

        # Load Layout button
        cmds.separator(w=10, hr=True, st='none', p=self.UIElements["guiFlowLayout1"])
        self.UIElements["loadLayout_button"] = cmds.button(label='load layout', width=buttonWidth, height=buttonHeight, bgc=[0.2, 0.4, 0.2], p=self.UIElements["guiFlowLayout1"], c=self.loadLayout) 



        self.UIElements["guiFrameLayout2"] = cmds.frameLayout( label='Rigging', borderStyle='in', p=self.UIElements["mainColLayout"])
        self.UIElements["guiFlowLayout2"] = cmds.flowLayout(v=False, width=windowWidth, height=windowHeight/2, wr=True, bgc=[0.2, 0.2, 0.2], p=self.UIElements["guiFrameLayout2"])
                
        # Rig arm button
        cmds.separator(w=10, hr=True, st='none', p=self.UIElements["guiFlowLayout2"])
        self.UIElements["rig_button"] = cmds.button(label='rig layout', width=buttonWidth, height=buttonHeight, bgc=[0.2, 0.4, 0.2], p=self.UIElements["guiFlowLayout2"], c=self.runRigCommand) 


        """ Show the window"""
        cmds.showWindow(windowName)
    
    def runRigCommand(self, *args):
        mirror = cmds.checkBox(self.UIElements['mirror_checkbox'], q=True, value=True)

        """ We need to figure out what part of the rig we are making. 
            We can get this information from our selected layout """
        layoutasset = utils.getLayoutAsset()[0]
        modfile = 'rig_' + cmds.getAttr('%s.type' % layoutasset)

        """__import__ basically opens a module and reads some info from it 
            without actually loading the module in memory."""
        mod = __import__("Modules.Rigging."+modfile, {}, {}, [modfile])
        reload(mod)
        # getattr will get an attribute from a class
        moduleClass = getattr(mod, mod.classname)
        moduleInstance = moduleClass(mirror, layoutasset)


    def loadLayout(self, *args):
    	# Pull all the options from the UI
    	""" We will use the same commands we used to build the UI Elements,
    	but this time we will run the flags in query mode """
    	side = cmds.optionMenu(self.UIElements['side_optionmenu'], q=True, v=True) 
    	prefix = cmds.optionMenu(self.UIElements["keyMenu"], q=True, v=True) 
    	""" For those of you running Maya 2013, consider how you could use 
    	symmetry to mirror joints later """
    	symmetry = cmds.checkBox(self.UIElements['symmetry_checkbox'], q=True, value=True)
        mirror = cmds.checkBox(self.UIElements['mirror_checkbox'], q=True, value=True)
        jsonfile = prefix.replace('_', '')
        layoutfile = os.environ["RDOJO"] + "Modules/Layout/" + jsonfile +".json"
        install.installLayout(layoutfile, side, prefix, symmetry, mirror)

    def loadLayoutDefinitions(self, *args):
        import json

        # Empty list to temporarily store dictionary keys. 
        keys = []

        """ Use the os.environ["RDOJO"] and navigate to the layout file.
            Make a optionMenu and add a menu item for each layout.json
            in the layout folder """
        
        lytfilelst = os.listdir(os.environ["RDOJO"] + 'Modules/Layout/')
        # Read the JSON file and store data to dict
        for item in lytfilelst:
            data = utils.readJson(os.environ["RDOJO"] + 'Modules/Layout/' + item)
            info = json.loads( data )
        for key, value in info.iteritems():
            keys.append(key)
            self.layout_info[key] = value

        # Add all the json to the self.layout_info dictionary.
        self.layout_info['Keys'] = keys 