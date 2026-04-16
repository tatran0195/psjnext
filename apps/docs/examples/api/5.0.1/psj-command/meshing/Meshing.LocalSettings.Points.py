# Title:   Meshing.LocalSettings.Points()
# Desc:    LocalSettings.Points
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/meshing/Meshing.LocalSettings.Points
# ---
Geometry.Part.Cube(iPartColor=7731705)
Meshing.LocalSettings.Points(strName="MeshParam_1", localMesh=LOCAL_MESH(bEnableSizeParams=True,  # [hl:start]
  dAvgElemSize=0.002, dMaxElemSize=0.01, dMinElemSize=0.001), veclHardPointXYZ=[[0.002078861077076959,
  0.008516764027639453, 0.01]], crlHardPointTarget=[Face(26)])  # [hl:end]
Meshing.SetMeshAttribute(crlParts=[Part(1)], surfaceMesh=SURFACE_MESH(dMinElemSize=0.0005,
  dGeomAngle=0.7853981634, dGeomMinSize=0.0005, iPerformanceMode=1, dAutoMergeTinyFacesAngle=0.5235987756,
  bGeomApprox=True, iNextEntityOffsetId=0))
Meshing.SurfaceMeshing(crlParts=[Part(1)], surfaceMesh=SURFACE_MESH(dMinElemSize=0.0005, dGeomAngle=0.7853981634,
  dGeomMinSize=0.0005, iPerformanceMode=1, dAutoMergeTinyFacesAngle=0.5235987756, bGeomApprox=True,
  iNextEntityOffsetId=0), iThreadNum=4)
