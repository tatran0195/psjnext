# Title:   MeshEdit.CreateNode.Point()
# Desc:    Create a node by referring to the coordinate value of the arbitrary point
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/mesh-edit/MeshEdit.CreateNode.Point
# ---
# Prepare model
Geometry.Part.Cube()

# Create node at point
newNode = MeshEdit.CreateNode.Point(iNewNodeID=490,   # [hl:start]
                                    posPoint=[0.008331683464348316, 0.003326606005430222, 0.009999999776482582], 
                                    bImprint=False, crTarget=Face(26))  # [hl:end]
JPT.Debugger(newNode) # for checking the return value
