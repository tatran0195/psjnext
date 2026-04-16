# Title:   MeshEdit.CreateNode.Absolute()
# Desc:    Create a node by inputting the direct coordinate value
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/mesh-edit/MeshEdit.CreateNode.Absolute
# ---
# Create an absolute node
newNode = MeshEdit.CreateNode.Absolute(dlCoordinate=[0.01, 0.0, 0.0], iNewNodeID=489)  # [hl]
JPT.Debugger(newNode) # for checking the return value
