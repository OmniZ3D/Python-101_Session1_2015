import maya.cmds as mc

class Rig_Arm:
    def __init__(self, *args):
        print "In Rig Arm"

        """ In the first part of the course we worked out how to build
        our layout joints.  Now we can move on to generate an arm rig from
        the layout joints. We will start by outlining the steps for
        rigging an arm.
        """
        """
        We need a way to identify that a given node in Maya is part
        of our layout joints.  We could do this by marking any
        layout joints with an attribute, or we could put the 
        layout joints in an asset that is marked with a custom attribute.
        Take a look at the install.py excerpt below to see how we add an 
        attribute to the layout asset.
        """

        """
        Now we need to build our arm rig joints, or we could even use the
        joints from the layout.  We already have a createJoints function
        to work with if needed. Most arm rigs have 3 joint chains. (FK, IK, and Rig).
        The rig joints blend between the ik and fk.
        """
        """
        Create controls for fk joints.
        """