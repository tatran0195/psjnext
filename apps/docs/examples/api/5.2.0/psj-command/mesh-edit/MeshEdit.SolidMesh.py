# Title:   MeshEdit.SolidMesh()
# Desc:    Command for converting surface mesh of specified parts to solid mesh.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/mesh-edit/MeshEdit.SolidMesh
# ---
# Prepare model and view
HexModeling.BallHexa(crPart=None, dRadius=0.005, dMeshSize=0.001, strPartName="HexBall_1")
JPT.ViewFitToModel()
JPT.Exec('ViewShowMesh(1)')

# Convert to Tet4
MeshEdit.SolidMesh(crlParts=[Part(1)], iType=3)
