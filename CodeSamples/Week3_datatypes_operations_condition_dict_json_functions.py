""" Week 3 Code Examples """
############################

""" Data Types.  Copy the following code into a script editor and run it. """
 
my_string = "I Love Python "
print type(my_string)
 
my_integer = 101
print type(my_intiger)
 
my_float = 2.5
print type(my_float)
 
my_boolean = True
print type(my_boolean)
 
""" Python is able to identify the data type contained in each variable without
any special prompting.  This is one of the reasons I love Python.
But what if we want to combine different types of data? The following
code will generate an error. You can comment out this line once you see the error."""
print my_string + my_integer
# This produces the following error.   TypeError: cannot concatenate 'str' and 'int' objects #
""" This error is telling us we can't combine to different data types.
To make this work, we need to cast my_intiger to a string. """
 
print my_string + str(my_integer)
# That gives us "I Love Python 101"




""" Operations   Copy the following code into a script editor and run it. """
 
print 1 +  2
 
print "hello" + " world"




""" Conditions   Copy the following code into a script editor and run it. """
fruit = ['apple', 'banana']
if fruit[0] == 'apple':
    print 'I think I want apple pie'
elif fruit[0] == 'banana':
    print 'I think I want a banana split'
else:
    print 'No dessert for me, thanks.'
     
# Let's try this in a loop
fruits = ['apple', 'banana']
for fruit in fruits:
    if fruits[0] == 'apple':
        print 'I think I want apple pie'
    elif fruits[0] == 'banana':
        print 'I think I want a banana split'
    else:
        print 'No dessert for me, thanks.'
         
# Other types of coditions.
"""
== is equal to
!= is not equal to
> is greater than
< is less than
>= is greater than or equal to
<= is less than or equal to
"""
 
my_var = 5
if my var is > 4:
    print "True"
if my_var > 1 and < 6:
    print "True"



""" Dictionaries """
# Declare an empty dictionary    
mydictionary = {}
# Add items to the dictionary under the key fruit.
mydictionary['fruit'] = [["apple", [1.0, 1.0, 1.0]], ["orange", [2.0, 2.0, 2.0]]]
# Add items to the dictionary under the key veg.
mydictionary['veg'] = [["kale", [1.0, 1.0, 1.0]], ["carrots", [2.0, 2.0, 2.0]]]
 
for key, value in mydictionary.iteritems():
    print (key, value)
     
# As a bonus, here is another way to do a loop if you want to taget a specific index from 2 lists.
for i in range(len(mydictionary)):
    print mydictionary['fruit'][i]
    print mydictionary['veg'][i]


""" JSON """
# Import the Python json module
import json 
# Here are a couple of simple functions to read and write json data.
def writeJson(fileName, data):
    with open(fileName, 'w') as outfile:
        json.dump(data, outfile)
 
    file.close(outfile)
 
def readJson(fileName):
    with open(fileName, 'r') as infile:
        data = (open(infile.name, 'r').read())
    return data
    
     
mydictionary = {}
mydictionary['arm'] = [["shoulder", [1.0, 1.0, 1.0]], ["elbow", [2.0, 2.0, 1.0]], ["wrist", [3.0, 1.0, 1.0]], ["wristEnd", [4.0, 1.0, 1.0]]]
mydictionary['leg'] = [["hip", [1.0, 1.0, 1.0]], ["knee", [2.0, 2.0, 1.0]], ["ankle", [3.0, 1.0, 1.0]], ["ankleEnd", [4.0, 1.0, 1.0]]]
 
# Change this directory
fileName = 'C:/Users/Griffy/Documents/GitHub/Python-101_Session1_2015/Modules/Layout/testdata.json'
data = mydictionary 
 
# Write the json file
writeJson(fileName, data)
 
# Read the json file
data = readJson(fileName)
 
#.loads, loads the json data to memory.
info = json.loads( data )
print info
 
print type(json.loads( data ))
 
for key, value in info.iteritems():
    print key, value
     
print info['arm'][0][1]




""" Functions """
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



""" Classes """
""" Functions are handy for wrapping blocks of code, 
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