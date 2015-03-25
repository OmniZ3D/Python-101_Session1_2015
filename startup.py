import maya.cmds as cmds
import os

cmds.upAxis( ax='y', rv=True )
cmds.currentUnit( linear='cm' )
cmds.currentUnit( time='ntsc' )

#access to the project root
os.environ["RDOJO"] = "D:/Libraries/Documents/GITHUB/Python101"

#import UI
from Modules.UI import rdojo_ui
reload(rdojo_ui)
rdojo_ui.RDojo_UI()

