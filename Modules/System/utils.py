import maya.cmds as cmds
# Import the Python json module
import json 
import os

# Here are a couple of simple functions to read and write json data.
def writeJson(fileName, data):
    with open(fileName, 'w') as outfile:
        json.dump(data, outfile)
 
    file.close(outfile)
 
def readJson(fileName):
    with open(fileName, 'r') as infile:
        data = (open(infile.name, 'r').read())
    return data



def createLytJoints(jointInfo, prefix, side, symmetry):
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
  
        # Deselect so we don't make a joint hierarchy.
        cmds.select(d=True)

        if symmetry == True:
            """ The next part is a bit of a cheat, but I think you will find
            yourself coming up with several cheats when built in Maya functionality
            does less than optimal things.  We know the 'side' we are using and we
            also know that the mirror joints will have the same name as the original 
            joints except __1 will be replaced with __2.  If you don't have
            the symmetry option, you could skip this"""
            symjntname = renameSymmetryJnt(jnt, prefix)
        
            """ Now we add the new joint and symmetry joint to the list we made up top. """
            # To do this we use a list method called .append
            jointlist.append([jnt, symjntname])
        
        else:
            jointlist.append([jnt, None])

        
    # Now we can parent our joints.
    for j in range(len(jointlist)):
        print jointlist[j]
        if j != 0:
            cmds.parent(jointlist[j][0], jointlist[j-1][0])
        if symmetry == True and j != 0:
            cmds.parent(jointlist[j][1], jointlist[j-1][1])
    cmds.select(d=True)
    return (jointlist)

   

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

def renameSymmetryJnt(jnt, prefix):
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
        conlist = cmds.listConnections(con, s=False, destination=True, type='joint')
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
    return (symjntname)
    
def orientJoints(jnt):
    #cycles through the joint list to orient the joints
    for each in jnt:
        cmds.joint(each, e=True, oj='xyz', secondaryAxisOrient='yup', ch=True, zso=True)

def getLayoutAsset():
    layoutasset = []

    # The ls command can be used to find all nodes of a certain type.
    #assetnodes = cmds.ls(type='container')
    # The ls command can also be specific to our selection by using the sl flag
    #assetnodes = cmds.ls(sl=True, type='container')
    """ In our case we may be selecting a joint and not the asset when
    we hit the rig arm button.  We can find the arm asset using the container command.
    """

    # Start by getting the selection
    sel = cmds.ls(sl=True)[0]
    
    # Clear the selection to be safe
    cmds.select(d=True)
    if cmds.nodeType(sel) == 'container':
        # If the asset is selected, we can check it is an arm
        if cmds.getAttr('%s.type' % sel) == 'Arm_':
            layoutasset.append(sel)
    # If we don't have the asset selected, we need to find it.
    # Use the nodeList flag to see if our selection is in an asset
    selast = cmds.container(q=True, fc=sel)
    # Verify selast isn't None.
    if selast != None:
        layoutasset.append(selast)


    return(layoutasset)


def getAstContents(ast):
    astcontents_dict = {}
    astjnts = []
    """ We could probably do this with one line, but we will
    use a function so we can be more thorough. """
    astcontents = cmds.container(ast, q=True, nl=True)
    for a in astcontents:
        if cmds.nodeType(a) == 'joint':
            astjnts.append(a)

    astcontents_dict['joints'] = astjnts

    return (astcontents_dict)

def createJointChain(jointInfo, prefix):
    jointlist = []
        
    #length of the list
    lstlen = len(jointInfo)
    
    for each in jointInfo:
        #create joint name from variables
        jntname = prefix + each[0]       
  
        #create joints
        jnt = cmds.joint(p=each[1], n=jntname)

        jointlist.append(jnt)
  
        # Deselect so we don't make a joint hierarchy.
        cmds.select(d=True)

    # Now we can parent our joints.
    for j in range(len(jointlist)):
        if j != 0:
            cmds.parent(jointlist[j], jointlist[j-1])

    cmds.select(d=True)
    return (jointlist)


def collectLytInfo(lytjnts, mirror):
    rig_info = {}
    # Get the position of our joints.
    # We could get more info from the joints like orientation, rotate order, and more.
    poslist = []
    for j in lytjnts:
        # xform is a great command that can be used to set and query the position of an object
        poslist.append(cmds.xform(j, q=True, ws=True, t=True))

    rig_info['layoutjointpositions'] = poslist
    rig_info['layoutjoints'] = lytjnts

    """ What if we are building a mirrored rig.  We need to find the mirrored
    positions of the joints and we need a mirrored name.  We could get very 
    in-depth with this if we needed to, but we will keep it simple for now.
    We are probably working in standard Maya space with Y up and Z foreward. 
    So we realy just need the inverted x axis. """
    if mirror == True:
        mlytjnts = []
        mposlist = []
        # Generate a new name for the joint.
        # We could do a lot more to make this flexible.  Avoid hard coding names when possible.
        for j in lytjnts:
            mlytjnts.append(j.replace('_l_', '_r_'))

        for p in poslist:
            # Here I just replace the x axis with the inverted value.
            mposlist.append([-p[0], p[1], p[2]])

        rig_info['layoutjointpositions'] = mposlist
        rig_info['layoutjoints'] = mlytjnts

    return (rig_info)

""" If we are mirroring joints we wont be able to get the joint rotations 
until the joints have been created, so this function will do that """
def collectLayoutRotations(lytjnts):
    # Get the rotation of our joints.
    # We could get more info from the joints like orientation, rotate order, and more.
    rotlist = []
    for j in lytjnts:
        # xform is a great command that can be used to set and query the position of an object
        rotlist.append(cmds.xform(j, q=True, ws=True, ro=True))

    return rotlist

def connectJointChains(jntinfo):
    print jntinfo
    constraints = []
    for i in range(len(jntinfo[0])):
        parentcon = cmds.parentConstraint(jntinfo[0][i], jntinfo[1][i], jntinfo[2][i], mo=True)
        constraints.append(parentcon)
    return constraints

def setupControlObject(ctrl, ctrlName, ctrlAttrs, ctrlPos, ctrlRot, lockAttrs, *args):
    ctrlpath = os.environ["RDOJO"] +'Modules/Controls/'

    # Import a control object
    cmds.file(ctrlpath + ctrl, i=True)
    # rename the control
    ctrlGrp = 'grp_%s' % (ctrlName)
    cmds.rename('control', ctrlName)
    if cmds.objExists('grp_control'):
        cmds.rename('grp_control', ctrlGrp)
        # Move the control to the  position
        cmds.xform('grp_%s' % (ctrlName), t=ctrlPos, ws=True)
        cmds.xform('grp_%s' % (ctrlName), ro=ctrlRot, ws=True)
    # Add the control attributes
    if len(ctrlAttrs)!= 0:
        cmds.select(ctrlName)
        for attr in ctrlAttrs:
            cmds.addAttr(shortName=attr, longName=attr, defaultValue=0, k=True)

    # Lock Attrs
    for attr in lockAttrs:
        cmds.setAttr(ctrlName+attr, channelBox=False, lock=True)

    return ([ctrlGrp, ctrlName])

    # NOTE: Allow for types such as (Vector, Integer, String, Float, Boolean, Enum)

def calculatePVPosition(jnts):
    from maya import cmds , OpenMaya
    start = cmds.xform(jnts[0] ,q=True ,ws=True, t=True)
    mid = cmds.xform(jnts[1] ,q=True ,ws=True, t=True)
    end = cmds.xform(jnts[2] ,q=True ,ws=True, t=True)
    startV = OpenMaya.MVector(start[0] ,start[1],start[2])
    midV = OpenMaya.MVector(mid[0] ,mid[1],mid[2])
    endV = OpenMaya.MVector(end[0] ,end[1],end[2])
    startEnd = endV - startV
    startMid = midV - startV
    dotP = startMid * startEnd
    proj = float(dotP) / float(startEnd.length())
    startEndN = startEnd.normal()
    projV = startEndN * proj
    arrowV = startMid - projV
    arrowV*= 0.5
    finalV = arrowV + midV
    return ([finalV.x , finalV.y ,finalV.z])
