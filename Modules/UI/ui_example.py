""" ui.example.py is a python script. """

""" import the maya commands module.  A script is refered to as a module 
    when it is imported into into another script or module. """
import maya.cmds as cmds

import Modules.System.utils as utils

import os

"""Up here at the top is where you put
   information about your script.  We could read this information when we 
   import this module if we format it like __author__ """

__author__ = 'rgriffin'


# The UI class
""" Classes can be thought of us containers for functions. """
    
class Example_UI:

    """ The __init__ function.  Code in the __init__ function initialize
    when this module is imported. 
    When a function is part of an imported class, we refer to it
    as a method. """
    def __init__(self, *args):
        """ Create a dictionary to store UI elements.
        Dictionaries are like list but can hold "keys"
        This dictionary will allow us access to the ui elements
        in all the methods of this class. """
        self.UIElements = {}

        """ This dictionary will store data from the lyout.json files """
        self.layout_info = {}

        """ Call the internal method loadLayoutDefinitions()
            The loadLayoutDefinitions method will read all the json files
            in the layout folder.  Then it will store the data
            in self.part_info.  Remember that we use self when
            calling a method of the class we are in."""

        self.loadLayoutDefinitions()

    # The function for building the UI
    def ui(self, *args):
        """ Check to see if the UI exists """
        windowName = "Window"
        if cmds.window(windowName, exists=True):
            cmds.deleteUI(windowName)

        """ Define width and height variables for buttons and windows"""    
        windowWidth = 120
        windowHeight = 60
        buttonWidth = 100
        buttonHeight = 30

        # Define the main ui window and assign it a key in the UIElements dictinary.
        self.UIElements["window"] = cmds.window(windowName, width=windowWidth, height=windowHeight, title="Example_UI", sizeable=True)
        
        # This is a flow layout.
        self.UIElements["guiFlowLayout1"] = cmds.flowLayout(v=False, width=windowWidth, height=windowHeight, wr=True, bgc=[0.2, 0.2, 0.2])

        # Menu listing all the layout files.
        self.UIElements["keyMenu"] = cmds.optionMenu('layouts', label='Layouts',  p=self.UIElements["guiFlowLayout1"])
        
        # Create a menu item for each json file in the Layout directory.
        for key in self.layout_info['Keys']:  
            cmds.menuItem(label=key, p=self.UIElements["keyMenu"])
        
        """ Show the window"""
        cmds.showWindow(windowName)

    def loadLayoutDefinitions(self, *args):
        import json

        # Empty list to temporarily store dictionary keys. 
        keys = []

        """ Use the os.environ["RDOJO"] and navigate to the layout file.
            Make a optionMenu and add a menu item for each layout.json
            in the layout folder """
        
        lytfile_lst = os.listdir(os.environ["RDOJO"] + 'Modules/Layout/')
        # Read the JSON file and store data to dict
        for item in lytfile_lst:
            data = utils.readJson(os.environ["RDOJO"] + 'Modules/Layout/' + item)
            info = json.loads( data )
        for key, value in info.iteritems():
            keys.append(key)
            self.layout_info[key] = value

        # Add all the json to the self.layout_info dictionary.
        self.layout_info['Keys'] = keys 