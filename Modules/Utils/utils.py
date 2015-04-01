# Import the Python json module
import json
import maya.cmds as cmds

# Here are a couple of simple functions to read and write json data.
def writeJson(fileName, data):
    with open(fileName, 'w') as outfile:
        json.dump(data, outfile)

    file.close(outfile)

def readJson(fileName):
    with open(fileName, 'r') as infile:
        data = (open(infile.name, 'r').read())
    return data

def createJoints(jointInfo,prefix,side,symmetry):
    #empty list that will store joint data
    jointlist=[]

    #length of the list
    lstlen = len(jointInfo)
    print ' joinInfo contains this many items %s' % lstlen

    for each in jointInfo:
        #create joint name from variables
        jntname = prefix + side + each[0]


        #condition that states if joints exist. If true creates a new name
        if cmds.objExists(jntname) == True:
            jntname = generateNewJointName(jntname)

        print 'The joint name is %s ' % each[0]

        #create joints
        jnt = cmds.joint(p=each[1], n=jntname, sym=symmetry)

        # Deselect so we don't make a joint hierarchy.
        cmds.select(d=True)

        if symmetry == True:
            symjntname = renameSymmetryJnt(jnt, prefix)

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

def createFK(jntlist,side):
    #from a given joint list create a series of locators and controllers with Parent Constraint for FK

    for each in jntlist:
        loc = cmds.spaceLocator(position = [0, 0, 0], name = 'loc_ctrl_' + side + each)

        #parent the locator to the selected object
        cmds.parent(loc, each)

        #zero all transform attributes
        cmds.setAttr ("loc_ctrl_" + side + each + ".translateX", 0)
        cmds.setAttr ("loc_ctrl_" + side + each + ".translateY", 0)
        cmds.setAttr ("loc_ctrl_" + side + each + ".translateZ", 0)

        cmds.setAttr ("loc_ctrl_" + side + each + ".rotateX", 0)
        cmds.setAttr ("loc_ctrl_" + side + each + ".rotateY", 0)
        cmds.setAttr ("loc_ctrl_" + side + each + ".rotateZ", 0)

        #set locator transforms to world space
        cmds.parent(loc, world = True)

        #create curve and parent constrain the locator
        animcurve = cmds.circle(center=[0,0,0],name= 'anim_' + side + each)
        cmds.delete(animcurve, icn=True)

        cmds.parent(animcurve,loc)

        cmds.setAttr ("anim_" + side + each + ".translateX", 0)
        cmds.setAttr ("anim_" + side + each + ".translateY", 0)
        cmds.setAttr ("anim_" + side + each + ".translateZ", 0)

        cmds.setAttr ("anim_" + side + each + ".rotateX", 0)
        cmds.setAttr ("anim_" + side + each + ".rotateY", 90)
        cmds.setAttr ("anim_" + side + each + ".rotateZ", 0)

        cmds.parent(animcurve, world=True)
        cmds.makeIdentity(animcurve,a=True,t=True, r=True,s=True,pn=True)

        cmds.parentConstraint(loc,each)
        cmds.parent(loc,animcurve)

def createIK(jntlist,side,prefix):
    # receive a joint list and side string

    # create IK Handles
    ankleIK = cmds.ikHandle(sj=jntlist[0],ee=jntlist[1],sol="ikRPsolver",n=(prefix+side+"ankleIK"))
    ballIK = cmds.ikHandle(sj=jntlist[1],ee=jntlist[2],sol="ikRPsolver",n=(prefix+side+"ballIK"))
    toeIK = cmds.ikHandle(sj=jntlist[2],ee=jntlist[3],sol="ikRPsolver",n=(prefix+side+"toeIK"))

    #create rig nodes
    ballNode = cmds.group(n=prefix+side+"ballRig")
    matchPosition(ballIK[0],ballNode)

    toeNode = cmds.group(n=prefix+side+"toeRig")
    matchPosition(ballIK[0], toeNode)

    heelNode = cmds.group(n=prefix+side+"heelRig")
    matchPosition(ankleIK[0], heelNode)

    toeTipNode = cmds.group(n=prefix+side+"toeTipRIG")
    matchPosition(toeIK[0], toeTipNode)

    footNode = cmds.group(n=prefix+side+"footCtrl")
    matchPosition(ankleIK[0], footNode)

    #parent ik handles
    cmds.parent(ankleIK[0], ballIK[0], ballNode)
    cmds.parent(toeIK[0],toeNode)

    #parent rig nodes
    cmds.parent(ballNode, toeNode, heelNode)
    cmds.parent(heelNode, toeTipNode)
    cmds.parent(toeTipNode, footNode)

    #add control attributes
    cmds.addAttr(footNode,ln='roll', at='float', min=-10, max=10, dv=False)
    cmds.setAttr((footNode+".roll"), e=True, keyable=True)

    cmds.addAttr(footNode,ln='toe', at='float', min=-10, max=10, dv=False)
    cmds.setAttr((footNode+".toe"), e=True, keyable=True)

    #add knee control
    kneeCtrl = cmds.circle(n=prefix+'kneeCtrl')
    kneeCtrlGrp = cmds.group(n=(prefix+"kneeCtrlGRP"))
    cmds.parent(kneeCtrl[0], kneeCtrlGrp)
    matchPosition(jntlist[0], kneeCtrlGrp)
    cmds.xform(kneeCtrl[0],r=True,t=[0,0,5])
    cmds.makeIdentity(kneeCtrlGrp,a=True)
    cmds.makeIdentity(kneeCtrl[0],a=True)
    cmds.pointConstraint(jntlist[0],kneeCtrlGrp)
    cmds.poleVectorConstraint(kneeCtrl[0],ankleIK[0])

    #connect knee control to foot
    kneeRotateNode = cmds.createNode(multiplyDivide,n=(prefix+"kneeRotateMulti"))
    cmds.connectAttr((footNode+".rotateY"), (kneeRotateNode+".input1X"),f=True)
    cmds.setAttr(kneeRotateNode+".input2X", 1)
    cmds.connectAttr((kneeRotateNode+".outputX"), (kneeCtrlGrp+".rotateY"), f=True)

def matchPosition(posStart,objEnd):
    # query position of the start object
    movePos = cmds.xform(posStart, q=True, ws=True, t=True)
    # move to the final position of the object
    cmds.move(movePos[0],movePos[1],movePos[2], objEnd, a=True)
    # freeze transformations
    cmds.makeIdentity(objEnd,a=True)
