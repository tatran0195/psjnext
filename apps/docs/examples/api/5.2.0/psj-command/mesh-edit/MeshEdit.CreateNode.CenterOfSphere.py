# Title:   MeshEdit.CreateNode.CenterOfSphere()
# Desc:    Create node at the center sphere or the center of curvature of 4 nodes.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/mesh-edit/MeshEdit.CreateNode.CenterOfSphere
# ---
# Prepare model
Geometry.Part.Sphere(iPartColor=6409934)

# Create center node of sphere
newNode = MeshEdit.CreateNode.CenterOfSphere(crlTargets=[Face(1)], iNewNodeID=383)  # [hl]
JPT.Debugger(newNode) # for checking the return value
