""" Week 2 Code Examples """
############################
import maya.cmds as cmds
# Create a space locator at a specific position.
cmds.spaceLocator(p=(1,1,1))
 
# Use setAttr to move the locator
cmds.setAttr('locator1.tx', 5)
 
# Get the translateX attribute from the locator.
print cmds.getAttr('locator1.tx')



""" Variables, Lists, and Loops """
import maya.cmds as cmds
# Using maya.cmds we can create a joint, name it, and position it.
cmds.joint(n='joint_arm1', p=[0.0, 1.0, 0.0])
  
# If we want to do something with the joint we need to save it in a variable.
shldrjnt = cmds.joint(n='joint_shoulder', p=[0.0, 4.0, 0.0])
print shldrjnt
# Now we have our shoulder joint saved to the shldrjnt variable as a unicode object.
print type(shldrjnt)
# We can get all sorts of information about the joint
print cmds.xform(shldrjnt, q=True, ws=True, t=True)
print cmds.getAttr('%s.jointOrient' % shldrjnt)
# We can even delete the joint.
cmds.delete(shldrjnt)
  
# With this in mind we can create all of the joints we need for an arm.
shldrjnt = cmds.joint(n='joint_shoulder', p=[0.0, 4.0, 0.0])
elbowjnt = cmds.joint(n='joint_elbow', p=[1.0, 4.0, 2.0])
wristjnt = cmds.joint(n='joint_wrist', p=[0.0, 4.0, 4.0])
  
# That is pretty cool but kind of inefficient.
# To make this a little nicer we will use a list.
"""
A List is well.. a list of items like you would take shopping.
To save us some typing we can make a list with all of our joint names in it.
In fact, we can make a list of lists so we can have a list for each
joint name and position.  We use square brackets to encapsulate each item in the list.
That list of lists can even be saved to a variable.
"""
  
jointinfo = (['joint_upperarm', [0.0, 5.0, 0.0]], ['joint_lowerarm', [1.0, 5.0, 2.0]], ['joint_hand', [0.0, 5.0, 4.0]])
print jointinfo
  
# So we have our list, but how do we work with it?
# For this we will call upon the power of the loop.
"""
A loop is a way to iterate over multiple objects in a list.
You can read about list and much more in the Python101 dicument.
"""
cmds.select(d=True)
for item in jointinfo:
    print item
    # To get an item from the item list we need to call it's index number.
    print item[0]
    print item[1]
    # We can use the data to make our joints.
    cmds.joint(n=item[0], p=item[1])

""" A deeper look at loops """
"""
Grab the following code and run all of it in the Maya script editor
"""

import maya.cmds as cmds
 
# Difine a list of strings and assign it to the mylist variable.
mylist = ('a', 'b')
 
# Enter a for loop and print each item in my list
for item in mylist:
    # Hit tab to indicate the next line is part of the loop
     
    # Create an empty list in the "scope" of the loop
    newvar = []
     
    # Append item to newvar
    newvar.append(item)
 
print newvar
 
""" 
Python cares about white space. To exit the for loop
we just remove the tab and start at the begining of a new line
"""
print "Now we are out of the loop """

""" More on Lists """
"""
Let's look a little more at nested lists.
Grab all of this code and run it in the script editor.
"""
  
import maya.cmds as cmds
  
# This is a pretty standard list
# The brackets indicate the items are part of a list
mylist = ('a', 'b', 'c')
print mylist
  
myotherlist = ('1', '2', '3')
print myotherlist
  
  
""" If we want to have multiple lists in a list
we need a way to indicate the list items are lists 
themselves.  For this we use square brackets """
  
mynestedlists = (['a', 'b', 'c'], ['1', '2', '3'])
print mynestedlists
  
# This is an empty list.
myemptylist = []
print myemptylist
  
""" Lets add mylist and myotherlist to myemptylist.
We do this with pythons append function.
"""
myemptylist.append([mylist, myotherlist])
print myemptylist
  
# We use the term index when refering to items in a list
# Python starts with item 0
# If we want to print the first item in myemptylist..
print myemptylist[0] # [0] is the index
# To get the first item in the first item of the list...
print myemptylist[0][0]
# The first item of the first item of the first item...
print myemptylist[0][0][0]