import maya.cmds as cmds
# os is a Python module that allows access to the operating system.
import os
 
cmds.upAxis( ax='y', rv=True )
cmds.currentUnit( linear='cm' )
cmds.currentUnit( time='ntsc' )

# Create a new environment variable that will provide easy access to the project root.
os.environ["RDOJO"] = "C:/Users/Griffy/Documents/GitHub/Python101-101_Session1_2015/"

# Import the UI
from Modules.UI import rdojo_ui
reload(rdojo_ui)
rdojo_ui.RDojo_UI()