# Title:   HexModeling.Curve()
# Desc:    Hexahedral and pentahedral elements are created by sweeping a surface mesh (composed of triangular and quadrilateral first-order elements) along a specified curve.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/hex-modeling/HexModeling.Curve
# ---
Geometry.Part.Cube()
Geometry.Bar.Spline(crlNodes=[Node(1, 8, 7)], strName="Bar_2")
Geometry.Part.Cylinder(dTopOuterRadius=0.001, dBottomOuterRadius=0.001, iPartColor=6409934)

Geometry.DeleteEntity.Face(crlFaces=[Face(32, 34)])
Geometry.DeleteEntity.Part(crlParts=[Part(1)])

Meshing.SetMeshAttribute(crlParts=[Part(3)], 
    surfaceMesh=SURFACE_MESH(
        dAvgElemSize=0.002, 
        dGeomAngle=0.7853981634, 
        iPerformanceMode=1, 
        dAutoMergeTinyFacesAngle=0.5235987756, 
        bOutputQuadMesh=True, bGeomApprox=True, 
        iNextEntityOffsetId=0))

Meshing.SurfaceMeshing(
    crlParts=[Part(3)], 
    surfaceMesh=SURFACE_MESH(
        dAvgElemSize=0.002, 
        dGeomAngle=0.7853981634, 
        iPerformanceMode=1, 
        dAutoMergeTinyFacesAngle=0.5235987756, 
        bOutputQuadMesh=True, 
        bGeomApprox=True, 
        iNextEntityOffsetId=0))

HexModeling.Curve(crFace=Face(33), crlEdges=[Edge(27)], dMeshSize=0.002)  # [hl]
