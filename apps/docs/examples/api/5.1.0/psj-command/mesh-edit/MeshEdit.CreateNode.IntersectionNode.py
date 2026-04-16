# Title:   MeshEdit.CreateNode.IntersectionNode()
# Desc:    Create floating nodes at the intersection of a part or face with edges or a line segment defined by 2 nodes
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/mesh-edit/MeshEdit.CreateNode.IntersectionNode
# ---
# Prepare model
Geometry.Part.Cube(iPartColor=7697908)
MeshEdit.CreateNode.Offset(vecOffset=[0.003, 0.0, 0.0], crlNodes=[Node(324)])
MeshEdit.CreateNode.Offset(vecOffset=[-0.003, 0.0, 0.0], crlNodes=[Node(259)])

# Create Intersection Node
newNode = MeshEdit.CreateNode.IntersectionNode(crlFaces=[Face(24, 23)], crlParts=[], crlEdges=[],   # [hl:start]
                                                crlNodes=[Node(489, 490)])  # [hl:end]
JPT.Debugger(newNode) # for checking the return value
