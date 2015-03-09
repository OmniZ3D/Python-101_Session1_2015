import maya.cmds as cmds
import os
 
cmds.upAxis( ax='y', rv=True )
cmds.currentUnit( linear='cm' )
cmds.currentUnit( time='ntsc' )

os.environ["RDOJO"] = "C:/Users/A/Documents/GitHub/Python-101_Session1_2015"

from Modules.UI import rdojo_ui as ui
reload(ui)
ui.RDojo_UI()