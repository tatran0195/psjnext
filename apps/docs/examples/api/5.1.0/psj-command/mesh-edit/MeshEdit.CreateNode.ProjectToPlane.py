# Title:   MeshEdit.CreateNode.ProjectToPlane()
# Desc:    Create a node by projecting the selected node/floating node to the selected face
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/mesh-edit/MeshEdit.CreateNode.ProjectToPlane
# ---
# Prepare model
Geometry.Part.Cube()
Meshing.GridMesh(listGridMesh=[GRID_MESH(crlFace=[Face(26)], crlCorner=[Node(6, 7, 8, 5)], 
                ilMeshCount=[5, 5], iShape=4, bOptimize=True)], bProjectToCad=True)

# Create plan projected node
newNode = MeshEdit.CreateNode.ProjectToPlane(crlNodes=[Node(501)], crlFaces=[Face(25)])  # [hl]
JPT.Debugger(newNode) # for checking the return value
