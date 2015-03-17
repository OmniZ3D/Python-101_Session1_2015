import maya.cmds as mc

class rig_arm:
    
    print "class rig_arm is ON"

    jointlist = []
    jointName = "" 
    jointInfoDef = (['joint_shoulder', [1.0, 5.0,0.0]],['joint_upperarm', [2.0, 5.0, 0.0]],['joint_lowerarm', [4.0, 4.0, -1.0]],['joint_hand', [6.0, 3.0, 0.0]],['temp', [8.0, 2.0, 1.0]])
    prefixDef = 'setup'
    sideDef ='L_'
    symmetryDef = False
    #As i'm working with Maya2013, I don't have a Sym flag in the joint command
    def __init__(self): 
        mc.select(d=True)  
    
    def generateNewJointName(self,jntname = ""):
        print "in Gen"
        print jntname

        if jntname is None:
            jntname = self.jointName

        #split string at defined character
        print jntname.partition('_')
        instance = jntname.partition('_')[2]
 
        #cast instance as a string to add it to another string later
        newinstance = str(int(instance)+1)
        print ' Our new instance is %s' % newinstance
 
        #replace jntname with our instance number
        jntname = jntname.replace('__'+instance,'__'+newinstance)
        print ' Our new joint name is %s' % jntname
     
        # Remember "return" returns the indicated data as the result of the function call.
        return jntname

    def createJoints(self, jointInfo , prefix , side , symmetry ): 

        if jointInfo is None:
            jointInfo = self.jointInfoDef
        if prefix is None:
            prefix = self.prefixDef
        if side is None:
            side = self.sideDef
        if symmetry is None:
            symmetry = self.symmetryDef

        lstlen = len(jointInfo)
        print 'jointInfo contains this many items %s' % lstlen
        
        for each in jointInfo:
            jntname = prefix + '_' + side + each[0]
            if mc.objExists(jntname) == True:
                jntname = self.generateNewJointName(jntname)
                           
            print 'the joint name is %s' %each[0]
            
            jnt = mc.joint(n=jntname, p=each[1]) 
            self.jointlist.append(jnt)
            print jnt

            mc.select(d=True)
        
        print"########################"
        
        for j in range(len(self.jointlist)):
            print self.jointlist[j]
            if j != 0:
                mc.parent(self.jointlist[j], self.jointlist[j-1])
                mc.joint(self.jointlist[j-1], e=True, zso=True, oj="xyz", ch=True)
        
        self.jointName = jntname
        # return jntname
                

        
        
instanceRig_arm = rig_arm()
jointInfo2 = None
#jointInfo2 = (['joint_s', [2.0, 6.0,5.0]],['joint_u', [2.0, 5.0, 5.0]],['joint_l', [4.0, 4.0, 4.0]],['joint_h', [6.0, 3.0, 5.0]],['t', [8.0, 2.0, 6.0]],['i', [10.0, 4.0, 6.0]])

instanceRig_arm.createJoints(None, None, 'Left_', None)
instanceRig_arm.generateNewJointName()



