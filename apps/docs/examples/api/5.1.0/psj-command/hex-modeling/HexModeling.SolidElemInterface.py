# Title:   HexModeling.SolidElemInterface()
# Desc:    make solid element interface
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/hex-modeling/HexModeling.SolidElemInterface
# ---
Geometry.Part.Cube()
Meshing.SurfaceMeshing(
    crlParts=[Part(1)], 
    surfaceMesh=SURFACE_MESH(dAvgElemSize=0.002, dGeomAngle=0.7853981634, 
        iPerformanceMode=1, dAutoMergeTinyFacesAngle=0.5235987756, 
        bOutputQuadMesh=True, bGeomApprox=True, iNextEntityOffsetId=0))
Geometry.DeleteEntity.Face(crlFaces=[Face(24, 22, 25, 23, 21)])
HexModeling.Linear(crlFaces=[Face(26)], dLength=0.01, iLayer=5, vecSweepDirection=[0.0, 0.0, 1.0])
HexModeling.SolidElemInterface(crlFaces=[Face(26)])  # [hl]
