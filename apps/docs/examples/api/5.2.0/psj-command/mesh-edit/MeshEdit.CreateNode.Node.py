# Title:   MeshEdit.CreateNode.Node()
# Desc:    Create a node by referring to the coordinate value of the existing node
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/mesh-edit/MeshEdit.CreateNode.Node
# ---
# Prepare model
Geometry.Part.Cube()

# Create node at node
newNode = MeshEdit.CreateNode.Node(iNewNodeId=489, crTarget=Node(480))  # [hl]
JPT.Debugger(newNode) # for checking the return value
