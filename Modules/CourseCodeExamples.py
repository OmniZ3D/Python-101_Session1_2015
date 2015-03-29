""" Week 2 Code Examples """
import maya.cmds as cmds
# Create a space locator at a specific position.
cmds.spaceLocator(p=(1,1,1))
 
# Use setAttr to move the locator
cmds.setAttr('locator1.tx', 5)
 
# Get the translateX attribute from the locator.
print cmds.getAttr('locator1.tx')