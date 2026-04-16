# Title:   HexModeling.Circular()
# Desc:    A hexahedral mesh model is generated from a hollow axisymmetric model.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/hex-modeling/HexModeling.Circular
# ---
Geometry.Part.Cylinder(bHollow=True, dTopInnerRadius=0.003, dBottomInnerRadius=0.003, iCircularNodes=128)
Geometry.BodyCut.XXYYOnOnePoint(crPart=Part(1), posCutPoint=[0, 0.01, 0.01], iCuttingPlane=2)
Geometry.BodyCut.XXYYOnOnePoint(crPart=Part(1), posCutPoint=[-0.01, 0.01, 0])
Geometry.DeleteEntity.Part(crlParts=[Part(3, 5)])

Meshing.SetMeshAttribute(
    crlParts=[Part(1)], 
    surfaceMesh=SURFACE_MESH(dAvgElemSize=0.002,
        dGeomAngle=0.7853981634, iPerformanceMode=1, 
        dAutoMergeTinyFacesAngle=0.5235987756, 
        bOutputQuadMesh=True, 
        bGeomApprox=True, 
        iNextEntityOffsetId=0))

Meshing.SurfaceMeshing(
    crlParts=[Part(1)], 
    surfaceMesh=SURFACE_MESH(
        dAvgElemSize=0.002, 
        dGeomAngle=0.7853981634, 
        iPerformanceMode=1,
         dAutoMergeTinyFacesAngle=0.5235987756, 
         bOutputQuadMesh=True, 
         bGeomApprox=True, 
         iNextEntityOffsetId=0))

HexModeling.Circular(crlFaces=[58], dAngle=90.0, iLayer=6, vecAxisVect=[0.0, -1.0, 0.0], dBDeleteOriginalParts=1.0)  # [hl]
