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
        info = json.loads(data)
    return info

def rigPart():
    # Store the selected itemto a variable.
	sel = cmds.ls(sl=True)[0]
	node = cmds.listRelatives(sel, ad=True, type='joint')
	nodeSize = len(node)-1
	ctrlPos = cmds.xform(sel, query=True, ws=True, rp=True)
	cmds.circle (name=sel + '_ctrl', nr=(90,0,0), center=ctrlPos, radius=10)
	cmds.xform (sel + '_ctrl', cp=True)
	cmds.orientConstraint(sel + '_ctrl', sel, mo=True, weight=1)
	cmds.ikHandle(n=node[nodeSize] + 'IK', startJoint=node[nodeSize], endEffector=node[nodeSize-2], solver='ikRPsolver')
	ctrlPos=cmds.xform(node[nodeSize-2], query=True, ws=True, rp=True)
	cmds.circle(name=node[nodeSize-2] + '_ctrl', nr=(90,0,0), center=ctrlPos, radius=10)
	cmds.xform(node[nodeSize-2] + '_ctrl', cp=True)
	cmds.parent (node[nodeSize] + 'IK', node[nodeSize-2] + '_ctrl')
	cmds.orientConstraint(node[nodeSize-2] + '_ctrl', node[nodeSize-2], mo=True, weight=1)
	cmds.polyCreateFacet(n="poleVectorPOS", p=[cmds.xform(node[nodeSize], query=True, ws=True, rp=True), cmds.xform(node[nodeSize-2], query=True, ws=True, rp=True), cmds.xform(node[nodeSize-1], query=True, ws=True, rp=True)], ch=False )
	cmds.polyMoveVertex('poleVectorPOS.vtx[2]', ch=False, localTranslateY=91.44)
	ctrlPos = cmds.xform('poleVectorPOS.vtx[2]', query=True, ws=True, translation=True)
	cmds.circle (n=node[nodeSize-1] + "PoleVector", center=ctrlPos, radius=10)
	cmds.xform (node[nodeSize-1] + "PoleVector", cp=True)
	cmds.delete("poleVectorPOS")
	cmds.poleVectorConstraint(node[nodeSize-1] + "PoleVector", node[nodeSize] + "IK")