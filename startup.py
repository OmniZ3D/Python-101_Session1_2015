import maya.cmds as cmds
 
cmds.upAxis( ax='y', rv=True )
cmds.currentUnit( linear='cm' )
cmds.currentUnit( time='ntsc' )
 
def createMenu(*args):
    mi = cmds.window('MayaWindow', ma=True, q=True)
    for m in mi:
        if m == 'RDojo_Menu':
            cmds.deleteUI('RDojo_Menu', m=True)
 
    cmds.menu('RDojo_Menu', label='RDMenu', to=True, p='MayaWindow')
 
createMenu()

# os is a Python module that allows access to the operating system.
import os
 
os.environ["RDOJO"] = "C:/Users/Seb/Documents/GitHub/Python-101_Session1_2015/"