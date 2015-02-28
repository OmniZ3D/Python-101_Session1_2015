import maya.cmds as mc
 
jointInfo=['arm__1',[5,0,0]],['elbow__1',[10,0,-1]],['wrist__1',[15,0,0]],['wristEnd__1',[18,0,0]]
# Creating a variable called "prefix" is a good way to make this code re-usable.
prefix='setup_'
# Add a variable for the side
side='_l'
""" Daniel is using a funtion here.  We haven't talked about functions yet, but this is a way to wrap up 
a block of code.  We will get into this soon """
def createJoints(jointInfo, prefix, side):
    for each in jointInfo:
        # Lets get our joint name put together before we build the joints so we can check if the joint exists.
        jntname = prefix + side + each[0]
        print ' The joint name is %s' % each[0]
        # Do a check to see if the joint exists.
        if mc.objExists(jntname) == True:
            # If the joint exists, we need to create a new name.
            # Partition will split a string at the defined character.
            print each[0].partition('__')
            instance = each[0].partition('__')[2]
            # instance will be the number at the end of jntname.
            """ lets replace that number with something else.  We could do this with a function
            to make things more robust, but for now we will keep it simple """
            # Do do math we need an integer + an integer.
            # I need the new instance as a string so I can add it to a string later. 
            # So cast instance as an int and the product of instance + 1 as a string.
            newinstance = str(int(instance) + 1)
            print ' Our new instance is %s' % newinstance
            # Lets use replace to change our instance number.
            # We are overriding the jntname variable.
            jntname = jntname.replace('__' + instance, '__' + newinstance)
            print ' Our new joint name is %s' % jntname
        """ Joints will add to a hierarchy if a joint is selected.
        It is best to deselect before making a joint.  This is a problem
        if we are using the for loop to build the joints in a hierarchy.
        We can get around this by doing a check. """
        
        # len will tell us the length of a list.
        lstlen = len(jointInfo)
        print ' jointInfo contains this many items. %s' % lstlen
         
        jnt = mc.joint(p=each[1], n=jntname, sym=True)
        mc.joint(jnt, e=True, oj='xyz', secondaryAxisOrient='yup', ch=True, zso=True)
        
        # Now do a condition to see if we made all the joints in jointInfo
        if each == jointInfo[lstlen-1]:
            mc.select(d=True)
            print "We made all of the joints."
        else:
            print "Still making joints here."
         
         
createJoints(jointInfo, prefix, side)