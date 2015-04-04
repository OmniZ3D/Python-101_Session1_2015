import maya.cmds as cmds
import Modules.System.utils as utils
reload(utils)

# We can use variables above the class level that can be read on class import
# This is also known as an attribute of a class
classname = 'Rig_Arm'
lytfile = 'arm.json'

class Rig_Arm:
    def __init__(self, mirror, layoutasset, *args):
        print "In Rig Arm"

        # Make an empty dictionary to store info about our arm rig
        self.rig_info = {}

        # getAstContents will return a dictionary with all of the layout joints
        layoutcontents = utils.getAstContents(layoutasset)

        self.rig_info = utils.collectLytInfo(layoutcontents['joints'], False)
        self.rig_info['layoutjointrotations'] = utils.collectLayoutRotations(layoutcontents['joints'])

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
            self.rig_info['layoutjointrotations'] = utils.collectLayoutRotations(layoutcontents['joints'])
            # Now we run the same install with new joint names and positions.
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

        self.rig_info['rigjnts'] = utils.createJointChain(jointInfo, 'rigjnt')
        self.rig_info['fkjnts'] = utils.createJointChain(jointInfo, 'fkjnt')
        self.rig_info['ikjnts'] = utils.createJointChain(jointInfo, 'ikjnt')

        # Connect the joint chains
        self.rig_info['jointcons'] = utils.connectJointChains([self.rig_info['ikjnts'], self.rig_info['fkjnts'], self.rig_info['rigjnts'] ])

        """Create controls for fk joints."""
        ctrllst = []
        for c in range(len(self.rig_info['fkjnts'])):
            if c != 3:
                ctrl = 'ctrl_circle.ma'
                ctrlName = self.rig_info['fkjnts'][c].replace('fkjnt_', 'ctrl_')
                ctrlAttrs = []
                ctrlPos = self.rig_info['layoutjointpositions'][c]
                ctrlRot = self.rig_info['layoutjointrotations'][c]
                lockAttrs = ['.tx', '.ty', '.tz']
                control = utils.setupControlObject(ctrl, ctrlName, ctrlAttrs, ctrlPos, ctrlRot, lockAttrs)
                ctrllst.append(control)

                # Constrain the fk joint to the control.
                cmds.parentConstraint(control[1], self.rig_info['fkjnts'][c], mo=True)
        
        # Store the controls in the rig_info dictionary.
        self.rig_info['fkctrls'] = ctrllst

        # Setup the fk control hierarchy.
        for c in range(len(self.rig_info['fkctrls'])):
            if c != 0:
                print self.rig_info['fkctrls'][c]
                cmds.parent(self.rig_info['fkctrls'][c][0], self.rig_info['fkctrls'][c-1][1])

