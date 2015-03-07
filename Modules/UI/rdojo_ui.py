import maya.cmds as cmds
  
cmds.upAxis( ax='y', rv=True )
cmds.currentUnit( linear='cm' )
cmds.currentUnit( time='ntsc' )
 
def runCommand(*args):
    print args
    print "Run Command"
    from Modules.Rigging import rig_arm
  
def createMenu(*args):
    mi = cmds.window('MayaWindow', ma=True, q=True)
    for m in mi:
        if m == 'RDojo_Menu':
            cmds.deleteUI('RDojo_Menu', m=True)
  
    mymenu = cmds.menu('RDojo_Menu', label='RDMenu', to=True, p='MayaWindow')
    cmds.menuItem(label='Rig Arm', parent=mymenu, command=runCommand)
createMenu()