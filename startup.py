import maya.cmds as cmds
 
cmds.upAxis( ax='y', rv=True )
cmds.currentUnit( linear='cm' )
cmds.currentUnit( time='ntsc' )

from Modules.UI import rdojo_ui as ui
reload(ui)