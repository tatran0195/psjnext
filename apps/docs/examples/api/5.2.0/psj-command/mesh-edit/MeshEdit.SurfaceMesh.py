# Title:   MeshEdit.SurfaceMesh()
# Desc:    Command for converting solid mesh of specified parts to surface mesh.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/mesh-edit/MeshEdit.SurfaceMesh
# ---
# Prepare model and view
Geometry.Part.Cube(iPartColor=6409934)
Meshing.AdjustCircleVertex(
  crlParts=[Part(1)],
  bInModeSurfaceMesh=True
)
Meshing.SetMeshAttribute(
  crlParts=[Part(1)],
  surfaceMesh=SURFACE_MESH(
    dAvgElemSize=0.003,
    dGeomAngle=0.7853981634,
    iPerformanceMode=1,
    dAutoMergeTinyFacesAngle=0.5235987756,
    bOutputQuadMesh=True,
    bGeomApprox=True
  )
)
Meshing.SurfaceMeshing(
  crlParts=[Part(1)],
  surfaceMesh=SURFACE_MESH(
    dAvgElemSize=0.003,
    dGeomAngle=0.7853981634,
    iPerformanceMode=1,
    dAutoMergeTinyFacesAngle=0.5235987756,
    bOutputQuadMesh=True,
    bGeomApprox=True
  ),
  iThreadNum=16
)
JPT.ViewFitToModel()
JPT.Exec('ViewShowMesh(1)')

# Convert to Quad8
MeshEdit.SurfaceMesh(crlParts=[Part(1)])
