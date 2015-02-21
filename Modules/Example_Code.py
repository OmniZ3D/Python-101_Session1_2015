######################################
# Nested Lists
#####################################
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




######################################
# Functions, Variables, Lists.
#####################################
def myFunction(myvar):
    result = "My Function takes " + myvar
    return result
    
myfuncreturn = myFunction('hat')


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





#########################################
# More Json
#########################################
import json
mydictionary = {}
mydictionary['fruit'] = [["apple", [1.0, 1.0, 1.0]], ["orange", [2.0, 2.0, 2.0]]]
mydictionary['veg'] = [["kale", [1.0, 1.0, 1.0]], ["carrots", [2.0, 2.0, 2.0]]]

fileName = 'C:/Users/Griffy/Documents/GitHub/Python101_S2_2014/Data/testdata.json'
data = mydictionary 
writeJson(fileName, data)

data = readJson(fileName)

info = json.loads( data )
print info

print type(json.loads( data ))

for key, value in info.iteritems():
    print key, value
    
print info['veg'][0][1]


def writeJson(fileName, data):
	with open(fileName, 'w') as outfile:
		json.dump(data, outfile)

	file.close(outfile)

def readJson(fileName):
    with open(fileName, 'r') as infile:
        data = (open(infile.name, 'r').read())
    return data
    
    
    
try:
    print "Hello"
except:
    return



########################################
# Write Json
#######################################
import maya.cmds as cmds
import json
import tempfile

# An empty dictionary that will be used to store locator_info
locator_info_dictionary = {}

# Define a list containing locator info
locator_info = (['lctr1', [0.0,0.0,0.0]], ['lctr2', [1.0,0.0,-1.0]], ['lctr3', [2.0,0.0,0.0]])

# Assign locator_info to dictionary keys
# For this example we will look at using list comprehensions
# Read documentation here... http://docs.python.org/2/tutorial/datastructures.html#list-comprehensions        
        
locator_info_dictionary['names']= [locator_info[x][0] for x in range(len(locator_info))]
locator_info_dictionary['positions']= [locator_info[x][1] for x in range(len(locator_info))]

print locator_info_dictionary
data = locator_info_dictionary


# These functions can be used to read and write json
# Define a path to the json file.  Change this to a path on your computer.
fileName = 'C:/Users/Griffy/Documents/GitHub/Python101/data/locator_info.json'

def writeJson(fileName, data):
	with open(fileName, 'w') as outfile:
		json.dump(data, outfile)

	file.close(outfile)

def readJson(fileName):
    with open(fileName, 'r') as infile:
        data = (open(infile.name, 'r').read())
    return data
    
# Now we will save to a json file
writeJson(fileName, data)

# Read the Json file
data = readJson(fileName)
info = json.loads( data )
info2 = json.dumps( data )

# Now take a look at the different data types returned by loads and dumps
print type(json.dumps( data ))
print type(json.loads( data ))

for key, value in info.iteritems():
    print key, value

########################################
# Read json and store data in a Dictionary
###########################################

"""  
Previously we used json to write some locator information to a json file
"""


import maya.cmds as cmds
import json
import tempfile
 
# An empty dictionary that will be used to store locator_info
locator_info_dictionary = {}
 
# Define a list containing locator info
# Note:  The last locator will be used as an aim for orienting the wrist.
locator_info = (['lctr1', [0.0,0.0,0.0]], ['lctr2', [1.0,0.0,-1.0]], ['lctr3', [2.0,0.0,0.0]], ['lctr4', [2.5,0.0,0.0]])
 
# Assign locator_info to dictionary keys
# For this example we will look at using list comprehensions
# Read documentation here... <a href="http://docs.python.org/2/tutorial/datastructures.html#list-comprehensions" style="text-decoration:underline;">http:/<wbr>/<wbr>docs.python.org/<wbr>2/<wbr>tutorial/<wbr>datastructures.html#list-comprehensions</a>        
         
locator_info_dictionary['names']= [locator_info[x][0] for x in range(len(locator_info))]
locator_info_dictionary['positions']= [locator_info[x][1] for x in range(len(locator_info))]
 
print locator_info_dictionary
data = locator_info_dictionary
 
 
# These functions can be used to read and write json
# Define a path to the json file.  Change this to a path on your computer.
fileName = 'C:/Users/Griffy/Documents/GitHub/Python101/data/locator_info.json'
 
def writeJson(fileName, data):
    with open(fileName, 'w') as outfile:
        json.dump(data, outfile)
 
    file.close(outfile)
 
def readJson(fileName):
    with open(fileName, 'r') as infile:
        data = (open(infile.name, 'r').read())
    return data
     
# Now we will save to a json file
writeJson(fileName, data)
 
# Read the Json file
data = readJson(fileName)
info = json.loads( data )
info2 = json.dumps( data )
 
# Now take a look at the different data types returned by loads and dumps
print type(json.dumps( data ))
print type(json.loads( data ))
 
for key, value in info.iteritems():
    print key, value
    
    
"""
Now we can create some locators from json data
The json data is now stored in info which
is effectively a dictionary.
"""

print info['names']
print info['positions']
# Lets use a loop to build locators
for i in range(len(info['names'])):
    lctr = cmds.spaceLocator(name=info['names'][i])
    # The position flag won't yield the desired
    # results, so we position the locators after we 
    # make them.
    cmds.xform(lctr, ws=True, t=info['positions'][i])
    
"""
At this point we want to let the user
position the locators.  When they are 
done positioning the locators, we can save
the new positions to a json file.
"""
# Make a new dictionary to store the updated locator information.
newLctrInfo = {}
# Find the locators in the scene.
# * works as a wildcard in a string
cmds.select('lctr*')
# Store the selected locators to a variable
lctrSel = cmds.ls(sl=True, type='transform')
# Clear the selection
cmds.select(d=True)
# Now get the position of each locator.
# Make a new list to hold the positions.
lctrPositions = []
for each in lctrSel:
    pos = cmds.xform(each, q=True, ws=True, t=True)
    lctrPositions.append(pos)
# Now pop our lists into the dictionary.
newLctrInfo['names']=lctrSel
newLctrInfo['positions']=lctrPositions
# Define a path to save the json file.
newFileName = 'C:/Users/Griffy/Documents/GitHub/Python101/data/character_info.json'
writeJson(newFileName, newLctrInfo)

"""
At this point we have read our generic
locator_info.json.  We built locators from
that info, positioned the locators, and 
saved out to a new json file.
Now we need to build joints.  As you can imagine
this will be similar to the locator creation.
"""

# Read the Json file
data = readJson(newFileName)
info = json.loads( data )
# Clear the selection
cmds.select(d=True)
# Build the joints
jntList = []
for i in range(len(info['names'])):
    # Make a name for the joint.
    jntName = info['names'][i].replace('lctr', 'jnt')
    jnt = cmds.joint(name=jntName, position=info['positions'][i], a=True)
    jntList.append(jnt)
    
# Make sure the new joint chain is oriented.
cmds.joint(jntList[0], edit=True, oj='xyz', sao='yup', ch=True, zso=True)
# We don't need that last joint so delete it.
# Find the last item in jntList
jlLen = len(jntList)
print jlLen
cmds.delete(jntList[jlLen-1])


basicFilter = "*.json"
file = cmds.fileDialog2(fileFilter=basicFilter, dialogStyle=2, fm=1, okc='Load')
print file

    




###########################################
# FUNCTIONS
###########################################
import maya.cmds as cmds

""" Example 1 """

# A basic function
def printSomeThings():
    print "I love Python"
    
# Will show the functions space in memory    
printSomeThings
# Call the printSomeThigs function
printSomeThings()



""" Example 2 """

# A function accepting an argument
def printSomeThings(things):
    print "I love %s"%things

# Call the function and pass an argument    
printSomeThings('flowers')



""" Example 3 """

# What if we want to get some data out of our function?
def printSomeThings(things):
    # Create a variable called thingsILove
    thingsILove =  "I love %s"%things
    
    # return will 'return' return data froma function
    return thingsILove
    
# Print the result of the function call
print printSomeThings('flowers')

# We can now use the return data outside of the function
someThings = printSomeThings('flowers')
print someThings + ' and candy'
""" Python has several 'methods' that can be used on 
different types.  Maybe we want to replace flowers
with something else. """
print someThings.replace('flowers', 'puppies') + ' and candy'
# We can also split our string
print someThings.split()
# Or partition it
stPar = someThings.partition('love')
print stPar[0]
print stPar[1]
print stPar[2]

# Lets find out if someThings ends with flowers
if someThings.endswith('flowers') == True:
    print someThings + ' and death rays'

# Before we move on, let's look at a couple more things
# we can do with data.
# If we want to know how many characters are in the string
# someThings, we can use len.
print len(someThings)
# Len will also work for counting indexed items in a list.
numbers = (1, 2, 3)
print len(numbers)
# We can also examine a list for it's range.
for i in range(len(numbers)):
    print i
    # This will print the item that occupies the current
    # index of numbers.
    print numbers[i]
    
################################################
# classes
#################################################

""" Functions are handy for wraping blocks of code, 
but what if we want to wrap several functions into a 
big library or 'module'?  We have already imported
several modules during this course.  maya.cmds and 
sys are some examples.
Now we get to create our own.  To do that, we are going to need a class.
Here is an example, but we will need to do something a little more involved
to get a handle on classes."""

class printThings:
    
    def printThingsILike(likes, *args):
        print likes
        print args
        
    def printThingsIDontLike(dislikes, *args):
        print dislikes


#################################################
#  Load ui
##################################################
import system.dojo_ui as dojoui
reload(dojoui)
dojoui = dojoui.RDojo_UI()
dojoui.ui()

print sys.path

import rigging.rigging
import rigging.ui.vv_mayarigger_ui as rigging_ui
reload(rigging_ui)
rigging_ui.Rig_UI()


import __builtin__
print __builtin__.lyt_filename

import rigging.rigging as rigging
print rigging
reload(rigging)
rigging.VV_RigTool()

from rigging.rig_arm import Rig_Arm as Rig_Arm
print Rig_Arm
Rig_Arm.rigArm()

import rigging.rig_arm as Rig_Arm
Rig_Arm = Rig_Arm.Rig_Arm()
Rig_Arm.rigArm()

import __builtin__

__builtin__.control_path = 'C:/Users/Griffy/Documents/GitHub/Python101/rigging/controls/'

print __builtin__.control_path

cmds.shadingNode("pointOnCurveInfo", asUtility=True)


rigging.VV_RigTool()