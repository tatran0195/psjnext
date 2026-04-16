# Title:   MeshEdit.CreateNode.Offset()
# Desc:    Create a new node by offsetting a distance from the selected node or floating point
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/mesh-edit/MeshEdit.CreateNode.Offset
# ---
# Prepare model
Geometry.Part.Cube()

# Create offset node
newNode = MeshEdit.CreateNode.Offset(vecOffset=[0.003, 0.0, 0.0], crlNodes=[Node(7)])  # [hl]
JPT.Debugger(newNode) # for checking the return value
