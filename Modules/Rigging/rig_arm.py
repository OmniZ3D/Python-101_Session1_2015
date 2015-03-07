import maya.cmds as cmds

#a list with arm joints
jointInfo=['arm__1', [5, 0, 0]], ['elbow__1', [10, 0, -1]], ['wrist__1', [15, 0, 0]], ['wristEnd__1', [18, 0, 0]]

#set the prefix and joint side separately
#each with its own variables
#this is so we can reuse jointInfo anytime we needed
prefix = 'setup_'
side = '_l__'

#function to create joints (???)
def createJoints(jointInfo, prefix, side):        
    for each in jointInfo:
        
        #create joint names before the joints
        #let us check if the joint exists or not
        #names are arranged as below
        #what is %$'% ???????
        jntname = prefix + side + each[0]
        
        
        #this part of the script is to check if there already existed
        #the same joints and what to do later about it
        if cmds.objExists(jntname) == True:
            
            #if joint exists, we need to create a new name
            #partition will split a string at the defined character
            print each[0].partition('__')
            instance = each[0].partition('__')[2]
            #instance will be the number at the end of the joint
            
            """lets replace that number with something else"""
            #we need an integer + an integer
            #the new instance needed to be a string so it can be added into another string later
            #cast instance as an integer and the product of instance + 1 as string
            newinstance = str(int(instance)+1)
            print 'Our new instance is %s'% newinstance
            
            #use replace to change instance number
            #now overriding the jntname variable
            jntname = jntname.replace('__'+instance, '__'+newinstance)
            print 'Our new joint name is %s'% jntname
            
        #length of the list (but what for?)
        lstlen = len(jointInfo)
        print 'jointInfo contains this many items %s'% lstlen
        
        #create joints
        jnt = cmds.joint(p = each[1], n = jntname)
        cmds.joint(jnt, e = True, oj = 'xyz', sao = 'yup', ch = True, zso = True)
        
        #Now do a condition to see if we made all the joints in jointInfo
        if each == jointInfo[lstlen-1]:
            cmds.select(d = True)
            print 'We made all of the joints.'
        else:
            print 'Still making joints here.'
            
createJoints(jointInfo, prefix, side)