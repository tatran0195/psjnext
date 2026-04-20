# Title:   MeshEdit.CreateNode.Between3Nodes()
# Desc:    Create a center node of 3 selected nodes
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/mesh-edit/MeshEdit.CreateNode.Between3Nodes
# ---
# Prepare model
Geometry.Part.Cube()

# Create a node at the center of three nodes
newNode = MeshEdit.CreateNode.Between3Nodes(iNewNodeID=490, crlNodes=[Node(8, 7, 5)])  # [hl]
JPT.Debugger(newNode) # for checking the return value
