import maya.cmds as mc

#jointInfo contains the names of the joints to be created
jointInfo=['arm__1',[5,0,0]],['elbow__1',[10,0,-1]],['wrist__1',[15,0,0]],['wristEnd__1',[18,0,0]]

#prefix and side of the joint chain
prefix = 'setup_'
side = 'l_'

#function to create joints
def createJoints(jointInfo, prefix, side):
    for each in jointInfo:

        #create joint name from variables
        jntname = prefix + side + each[0]
        print 'The joint name is %s ' % each[0]

        #condition that states if joints exist. If true creates a new name
        if mc.objExists(jntname) == True:

            #split string at defined character
            print each[0].partition('__')
            instance = each[0].partition('__')[2]

            #cast instance as a string to add it to another string later
            newinstance = str(int(instance)+1)
            print ' Our new instance is %s' % newinstance

            #replace jntname with our instance number
            jntname = jntname.replace('__'+instance,'__'+newinstance)
            print ' Our new joint name is %s' % jntname

        #lenght of the list
        lstlen = len(jointInfo)
        print ' joinInfo contains this many items %s' % lstlen

        #create joints
        jnt = mc.joint(p=each[1],n=jntname,sym=True)
        mc.joint(jnt,e=True,oj='xyz',secondaryAxisOrient='yup',ch=True,zso=True)



        #condition that sees if all joints have been created
        if each == jointInfo[lstlen-1]:
            mc.select(d=True)

            #sends orient joint list, since we have created all the joints
            allJoints = mc.ls(type='joint')
            orientJoints(allJoints)

            #function that renames all joints on the right side
            renameJoints(allJoints)

            print "We made all joints + oriented them"
        else:
            print "Still making joints here"

def renameJoints(jnt):

    for each in jnt:

        oldSide = each.partition('_l_')[1]
        jntIndex = each.partition('__')[2]

        #check if it's on the left or right side of the setup
        if jntIndex == '2':
            print 'the part of the name that will be replaced is %s'% oldSide

            newSide = '_r_'
            newName = each.replace(oldSide,newSide)

            mc.rename(each,newName)
            print 'the new joint name is %s' % each

        '''
        FIRST ATTEMPT WITH THE listConnections command

        #save connections in a new variable
        #symConstr = mc.listConnections(connections=True, t='constraint')

        #replace the string value to run rename command
        oldJntName = symConstr
        newJntName = symConstr.replace("_l_","_r_")

        mc.rename(oldJntName,newJntName)
        '''


def orientJoints(jnt):
    #cycles through the joint list to orient the joints
    for each in jnt:
        mc.joint(each, e=True, oj='xyz', secondaryAxisOrient='yup', ch=True, zso=True)

createJoints(jointInfo, prefix, side)