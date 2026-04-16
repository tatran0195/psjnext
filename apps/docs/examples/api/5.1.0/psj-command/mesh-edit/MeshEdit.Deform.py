# Title:   MeshEdit.Deform()
# Desc:    Deform mesh by specifying source and destination face pairs.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/mesh-edit/MeshEdit.Deform
# ---
# Prepare model and view
Geometry.Part.Cube(
  dlLength=[0.01, 0.01, 0.001],
  ilAxialNodes=[10, 10, 3],
  iPartColor=7463537
)
Geometry.Part.Cube(
  dlOrigin=[0.0, 0.0, 0.002],
  strName="Cube_2",
  iPartColor=7961077
)
JPT.ViewFitToModel()
JPT.Exec('ViewShowMesh(1)')

# Deform mesh
MeshEdit.Deform(
  crlFaceSrcObverse=[Face(26)],
  crlFaceDstObverse=[Face(51)],
  crlFaceFixed=[Face(25)]
)
