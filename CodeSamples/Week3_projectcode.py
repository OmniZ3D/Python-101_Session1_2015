""" In Week 3 We created some functions that handled the job
of creating layout joints. The goal was to incorporate 
lists, variables, functions, and other basic Python concepts."""

import maya.cmds as mc
 
""" Create a list of items that defines the base name and starting
position of our joints. """
jointInfo=['arm__1',[5,0,0]],['elbow__1',[10,0,-1]],['wrist__1',[15,0,0]],['wristEnd__1',[18,0,0]]
 
""" Define variables that will store a value for the prefix, name, and side of our joints. """
prefix = 'setup_'
side = 'l_'
symmetry = True
 
""" Function to create joints """
def createJoints(jointInfo, prefix, side, symmetry):
    """ Here is another cool thing you can do.  Create an empty
    list.  Later in the script we will fill the list with items.
    """
    jointlist = []
         
    #length of the list
    lstlen = len(jointInfo)
    print ' joinInfo contains this many items %s' % lstlen
     
    for each in jointInfo:
        #create joint name from variables
        jntname = prefix + side + each[0]       
         
        # Check to see if the jntname exixsts
        """ jntname will be equal to the new joint name returned from generateNewJointName
        if that name already exists """
        #condition that states if joints exist. If true creates a new name
        if mc.objExists(jntname) == True:
            jntname = generateNewJointName(jntname)
         
        print 'The joint name is %s ' % each[0]
         
        #create joints
        jnt = mc.joint(p=each[1], n=jntname, sym=symmetry)
        print jnt
   
        # Deselect so we don't make a joint hierarchy.
        cmds.select(d=True)
 
        if symmetry == True:
            """ The next part is a bit of a cheat, but I think you will find
            yourself coming up with several cheats when built in Maya functionality
            does less than optimal things.  We know the 'side' we are using and we
            also know that the mirror joints will have the same name as the original 
            joints except __1 will be replaced with __2."""
            symjnt = renameSymmetryJnt(jnt)
         
            """ Now we add the new joint and symmetry joint to the list we made up top. """
            # To do this we use a list method called .append
            jointlist.append([jnt, symjnt])
         
        else:
            jointlist.append(jnt)
 
         
    # Now we can parent our joints.
    for j in range(len(jointlist)):
        print jointlist[j]
        if j != 0:
            cmds.parent(jointlist[j][0], jointlist[j-1][0])
            if symmetry == True:
                print (jointlist[j][1], jointlist[j-1][1])
                cmds.parent(jointlist[j][1], jointlist[j-1][1])
 
    
 
""" Function that generates a new joint name if that joint already exists. """ 
def generateNewJointName(jntname):
    print "in Gen"
    print jntname
     
    #split string at defined character
    print jntname.partition('__')
    instance = jntname.partition('__')[2]
 
    #cast instance as a string to add it to another string later
    newinstance = str(int(instance)+1)
    print ' Our new instance is %s' % newinstance
 
    #replace jntname with our instance number
    jntname = jntname.replace('__'+instance,'__'+newinstance)
    print ' Our new joint name is %s' % jntname
     
    # Remember "return" returns the indicated data as the result of the function call.
    return jntname

""" A function that provides a meaningfull name for the symmetry joints. """ 
def renameSymmetryJnt(jnt):
    symConstr = mc.listConnections(jnt, connections=True, t='symmetryConstraint', et=True)
    print "constraint"
    print symConstr
      
    # So we will refine more.
    # First a condition to make sure the list has items.
    if symConstr != []:
        for item in symConstr:
            print item
            # .startswith is a string operation
            if item.startswith('symmetryConstraint'):
                con = item
                  
    # Now get the joint connected to the constraint.
    if con != None:
        conlist = mc.listConnections(con, s=False, type='joint')
        print 'conlist'
        print conlist
          
        if conlist[0].startswith(prefix):
            symjnt = conlist[0]
            print symjnt
              
            try:
                tmpvar = conlist[0].replace('_l_', '_r_')
                symjntname = tmpvar.replace('__2', '__1')
                mc.rename(conlist[0], symjntname)
            except: pass
             
        return (symjntname)

""" A function that orients the joints. """     
def orientJoints(jnt):
    #cycles through the joint list to orient the joints
    for each in jnt:
        mc.joint(each, e=True, oj='xyz', secondaryAxisOrient='yup', ch=True, zso=True)
 

# This line calls the createJoints function.
createJoints(jointInfo, prefix, side, symmetry)