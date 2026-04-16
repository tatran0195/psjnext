# Title:   HexModeling.Layer()
# Desc:    Hexahedral and pentahedral elements are created by sweeping a surface mesh (composed of triangular and quadrilateral first-order elements) in the normal direction.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/hex-modeling/HexModeling.Layer
# ---
Geometry.Part.Cube()
Meshing.SurfaceMeshing(
    crlParts=[Part(1)], 
    surfaceMesh=SURFACE_MESH(dAvgElemSize=0.002, dGeomAngle=0.7853981634, 
        iPerformanceMode=1, dAutoMergeTinyFacesAngle=0.5235987756, 
        bOutputQuadMesh=True, bGeomApprox=True, iNextEntityOffsetId=0))
Geometry.DeleteEntity.Face(crlFaces=[Face(24, 22, 25, 23, 21)])
HexModeling.Layer(crlFaces=[26], dFrontWidth=0.001, dBackWidth=0.0015, iFrontLayers=3,   # [hl:start]
                iBackLayers=2, iBaseFaceType=1)  # [hl:end]
