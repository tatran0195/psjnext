# Title:   MeshEdit.CreateNode.CircleCenter()
# Desc:    Create a node/floating node at the center of the selected circular edge
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/mesh-edit/MeshEdit.CreateNode.CircleCenter
# ---
# Prepare model
Geometry.Part.Cube()
Geometry.Edge.Circle(veclPositions=[[0.005555555555555556, 0.005555555555555556, 0.01]], 
                                    crlTargetFace=[Face(26)], dOutRadius=1.5)

# Create center node of circle
newNode = MeshEdit.CreateNode.CircleCenter(crlEdges=[Edge(55)], iNewNodeID=540)  # [hl]
JPT.Debugger(newNode) # for checking the return value
