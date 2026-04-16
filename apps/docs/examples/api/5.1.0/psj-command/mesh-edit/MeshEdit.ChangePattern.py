# Title:   MeshEdit.ChangePattern()
# Desc:    Change the mesh pattern of faces.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/mesh-edit/MeshEdit.ChangePattern
# ---
# Prepare model and view
Geometry.Part.Cube(iPartColor=6409934)
JPT.Exec('ViewShowMesh(1)')
JPT.ViewFitToModel()

# Change pattern
MeshEdit.ChangePattern(crlFaces=[Face(22)], iPatternType=1)
