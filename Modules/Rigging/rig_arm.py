# Create a variable to store joint name and position
armJoints = (['clavicle_JNT', [0.0, 5.0, 0.0]], ['shoulder_JNT', [1.0, 5.0, 0.0]], ['elbow_JNT', [2.5, 5.0, -.25]], ['wrist_JNT', [4.0, 5.0, 0.0]])

cmds.select(deselect = True)

# Create the arm placement joints
for i in armJoints:
	cmds.joint(name = i[0], position = i[1], radius = .25)

cmds.select(deselect = True)