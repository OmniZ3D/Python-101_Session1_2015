import maya.cmds as cmds
  
cmds.upAxis( ax='y', rv=True )
cmds.currentUnit( linear='cm' )
cmds.currentUnit( time='ntsc' )
 
# Load The UI
# We havn't talked much about importing modules yet.
from Modules.UI import rdojo_ui as ui
reload(ui)

# os is a Python module that allows access to the operating system.
import os
os.environ["RDOJO"] = "C:/Users/Bacon/Documents/GitHub/Python-101_Session1_2015/"