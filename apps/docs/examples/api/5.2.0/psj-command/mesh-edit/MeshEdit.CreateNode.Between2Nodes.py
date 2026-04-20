# Title:   MeshEdit.CreateNode.Between2Nodes()
# Desc:    Create node between two selected nodes
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/mesh-edit/MeshEdit.CreateNode.Between2Nodes
# ---
# Prepare model
Geometry.Part.Cube()

# Create a node between two nodes
newNodes = MeshEdit.CreateNode.Between2Nodes(iNewNodeID=490, iNumberofNodes=2, crlNodes=[Node(6, 7)])  # [hl]
JPT.Debugger(newNodes) # for checking the return value
