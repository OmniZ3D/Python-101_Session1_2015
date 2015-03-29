import maya.cmds as cmds
import Modules.System.utils as utils
reload(utils)

class Rig_Arm:
    def __init__(self, mirror, *args):
        print "In Rig Arm"

        # Make an empty dictionary to store info about our arm rig
        self.rig_info = {}

        layoutasset = utils.getLayoutAsset()[0]

        # getAstContents will return a dictionary with all of the layout joints
        layoutcontents = utils.getAstContents(layoutasset)

        self.rig_info = utils.collectLytInfo(layoutcontents['joints'], False)

        # call the install function
        self.install()

        # We can insert a global variable for the mirror value.
        # If mirror == True, we can auto generate a right side rig.
        self.mirror = mirror
        if mirror == True:
            """ We can check to see if mirror is True.  If it is
            we can override self.rig_info so it contains mirrored
            joint names and positions. We will move the code that
            populates self.rig_info into its own function in utils"""
            # Overide self.rig_info
            self.rig_info = utils.collectLytInfo(layoutcontents['joints'], True)
            self.install()

    # Make a function called install that will handle all the rigging stuff
    def install(self, *args):
        # See what rig_info looks like
        print self.rig_info
        """ self.rig_info has all the information we need to place our
        fk, ik, and rig joints. 
        Now we need to build our arm rig joints, or we could even use the
        joints from the layout.  We already have a createJoints function
        to work with if needed. Most arm rigs have 3 joint chains. (FK, IK, and Rig).
        The rig joints blend between the ik and fk.
        Because we setup create joints to accept a list formated like [joint, position],
        we need to arrange the data from self.rig_info so it works.
        """
        # Get the root name of the layout joint so we can strip it from the joint names.
        rootname = self.rig_info['layoutjoints'][0].partition('_')[0]
        jointInfo = []
        for i in range(len(self.rig_info['layoutjoints'])):
            jointInfo.append([self.rig_info['layoutjoints'][i].replace(rootname, ""), self.rig_info['layoutjointpositions'][i]])

        utils.createJointChain(jointInfo, 'rigjnt')
        utils.createJointChain(jointInfo, 'fkjnt')
        utils.createJointChain(jointInfo, 'ikjnt')

  
        """
        Create controls for fk joints.
        """