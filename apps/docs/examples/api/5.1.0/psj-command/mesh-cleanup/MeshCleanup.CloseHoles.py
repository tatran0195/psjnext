# Title:   MeshCleanup.CloseHoles()
# Desc:    close holes
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/mesh-cleanup/MeshCleanup.CloseHoles
# ---
# Prepare a model - a cylinder with holes 
Geometry.Part.Cylinder(
    bHollow=True, 
    dTopInnerRadius=0.003, 
    dBottomInnerRadius=0.003, 
    iPartColor=7829501
)

JPT.Exec('DeleteFace([7], 1)')

# Find hole edges
result = MeshCleanup.FindHoles()
flag, edge_list = JPT.MacroResultParser(result,["number","list_cursor"])

# Input edges to close hole
MeshCleanup.CloseHoles(
    crlEdges=edge_list, 
    dAreaMin=0.0, 
    dAreaMax=0.54321, 
    bMergeFace=False, 
    bMergeEdge=False
)
