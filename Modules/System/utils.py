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
        if cmds.objExists(jntname) == True:
            jntname = generateNewJointName(jntname)
        
        print 'The joint name is %s ' % each[0]
        
        #create joints
        jnt = cmds.joint(p=each[1], n=jntname, sym=symmetry)
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
            jointlist.append(jnt, symjntname)
        
        else:
            jointlist.append(jnt)

        
    # Now we can parent our joints.
    for j in range(len(jointlist)):
        if j != 0:
            cmds.parent(jointlist[j][0], jointlist[j-1][0])
        if symmetry == True:
            cmds.parent(jointlist[j][1], jointlist[j-1][1])

   

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

def renameSymmetryJnt(jnt):
    symConstr = cmds.listConnections(jnt, connections=True, t='symmetryConstraint', et=True)
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
        conlist = cmds.listConnections(con, source=True, type='joint')
        print 'conlist'
        print conlist
         
        if conlist[0].startswith(prefix):
            symjnt = conlist[0]
            print symjnt
             
            try:
                tmpvar = conlist[0].replace('_l_', '_r_')
                symjntname = tmpvar.replace('__2', '__1')
                cmds.rename(conlist[0], symjntname)
            except: pass
    
def orientJoints(jnt):
    #cycles through the joint list to orient the joints
    for each in jnt:
        cmds.joint(each, e=True, oj='xyz', secondaryAxisOrient='yup', ch=True, zso=True)