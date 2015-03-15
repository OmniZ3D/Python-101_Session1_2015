import maya.cmds as cmds
  
cmds.upAxis( ax='y', rv=True )
cmds.currentUnit( linear='cm' )
cmds.currentUnit( time='ntsc' )
 
# Load The UI
# We havn't talked much about importing modules yet.
from ui import rdojo_ui as ui
reload(ui)