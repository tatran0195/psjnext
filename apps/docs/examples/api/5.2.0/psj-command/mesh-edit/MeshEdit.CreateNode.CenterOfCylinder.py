# Title:   MeshEdit.CreateNode.CenterOfCylinder()
# Desc:    Create a floating node at the center of the cylindrical surface in the longitudinal direction
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/mesh-edit/MeshEdit.CreateNode.CenterOfCylinder
# ---
# Prepare model
Geometry.Part.Cylinder()

# Create center node of cylinder
newNode = MeshEdit.CreateNode.CenterOfCylinder(crlFaces=[Face(5)], iNewNodeID=363)  # [hl]
JPT.Debugger(newNode) # for checking the return value
