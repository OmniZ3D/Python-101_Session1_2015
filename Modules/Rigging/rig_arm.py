import maya.cmds as mc

#jointInfo contains the names of the joints to be created
jointInfo=['shld__1',[5,0,0]],['elbow__1',[10,0,-1]],['wrist__1',[15,0,0]],['wristEnd__1',[18,0,0]]

#prefix and side of the joint chain
prefix = 'setup_'
side = 'l_'
symmetry = True

#function to create joints
def createJoints(jointInfo, prefix, side, symmetry):
    for each in jointInfo:

        jointlist = []

        #lenght of the list
        lstlen = len(jointInfo)
        print ' joinInfo contains this many items %s' % lstlen


        for each in jointInfo:
            #create joint name from variables
            jntname = prefix + side + each[0]

            #condition that states if joints exist. If true creates a new name
            if mc.objExists(jntname) == True:
                jntname = generateNewJointName(jntname)

            print 'The joint name is %s ' % each[0]

            #create joints
            jnt = mc.joint(p=each[1],n=jntname,sym=symmetry)
            print jnt

            #Deselect so we don't make a joint hierarchy
            mc.select(d=True)

            if symmetry == True:
                #Maya Cheat = we know that they have the same name as the original
                symjnt = renameSymmetryJnt(jnt)

                #add the new joint and symmetry joint to the list
                jointlist.append([jnt, symjnt])

            else:
                jointlist.append(jnt)

        #Cycle that will parent the joints
        for j in range(len(jointlist)):
            print jointlist[j]
            if j != 0:
                mc.parent(jointlist[j][0], jointlist[j-1][0])
                if symmetry == True:
                    print(jointlist[j][1], jointlist[j-1][1])
                    mc.parent(jointlist[j][1], jointlist[j-1][1])


def generateNewJointName(jntname):
    print "in Gen"
    print jntname

    #split string at defined character
    print jntname.partition('__')
    instance = jntname.partition('__')[2]

    #cast instance as a string to add it to another one later
    newinstance = str(int(instance)+1)
    print ' Our new instance is %s' % newinstance

    #replace jntname with instance number
    jntname = jntname.replace('__'+instance, '__'+newinstance)
    print ' Our new joint name is %s' % jntname

    #return result of function
    return jntname

def renameSymmetryJnt(jnt):
    symConstr = mc.listConnections(jnt, connections=True, t='symmetryConstraint', et=True)
    print 'constraint'
    print symConstr

    #condition that checks if the list has items
    if symConstr != []:
        for item in symConstr:
            print item
            if item.startswith('symmetryConstraint'):
                con = item

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

def orientJoints(jnt):
    #cycles through the joint list to orient the joints
    for each in jnt:
        mc.joint(each, e=True, oj='xyz', secondaryAxisOrient='yup', ch=True, zso=True)

createJoints(jointInfo, prefix, side, symmetry)