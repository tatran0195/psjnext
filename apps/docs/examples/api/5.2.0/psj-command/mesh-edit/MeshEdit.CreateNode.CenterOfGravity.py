# Title:   MeshEdit.CreateNode.CenterOfGravity()
# Desc:    create node Center Of Gravity
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/mesh-edit/MeshEdit.CreateNode.CenterOfGravity
# ---
# Prepare model
Geometry.Part.Cube()

# Create center node of gravity
newNode = MeshEdit.CreateNode.CenterOfGravity(iNodeID=489, crlTargets=[Part(1)])  # [hl]
JPT.Debugger(newNode) # for checking the return value
