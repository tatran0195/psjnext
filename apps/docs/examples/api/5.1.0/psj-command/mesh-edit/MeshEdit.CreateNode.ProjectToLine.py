# Title:   MeshEdit.CreateNode.ProjectToLine()
# Desc:    Create a node by projecting the third selected node/floating node to the shortest distance of the two previously selected nodes/floating nodes
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/mesh-edit/MeshEdit.CreateNode.ProjectToLine
# ---
# Prepare model
Geometry.Part.Cube()

# Create line projected node
newNode = MeshEdit.CreateNode.ProjectToLine(crlNodes=[Node(7, 8, 76)])  # [hl]
JPT.Debugger(newNode) # for checking the return value
