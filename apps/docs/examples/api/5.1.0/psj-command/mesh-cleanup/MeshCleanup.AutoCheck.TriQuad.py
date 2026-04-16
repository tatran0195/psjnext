# Title:   MeshCleanup.AutoCheck.TriQuad()
# Desc:    Correct the surface mesh (TRI3/TRI6/Quad4/Quad8) by using multiple mesh quality standards
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/mesh-cleanup/MeshCleanup.AutoCheck.TriQuad
# ---
# Prepare model
Geometry.Part.Trapezoid(dlLength=[0.01, 0.001, 0.01], 
                        dTopXLength=0.1, 
                        strName="Trapezoid_1", 
                        iPartColor=7697908)
JPT.Exec("View Fit To Model()")
Meshing.SurfaceMeshing(crlParts=[Part(1)], 
                    surfaceMesh=SURFACE_MESH(
                        dMaxElemSize=0.005, 
                        dMinElemSize=0.005, 
                        dGeomAngle=0.7853981634, 
                        dGeomMinSize=0.0001, 
                        dGradingFactor=0.5, 
                        iPerformanceMode=1, 
                        dAutoMergeTinyFacesAngle=0.5235987756, 
                        bOutputQuadMesh=True, 
                        bGeomApprox=True, 
                        iNextEntityOffsetId=0), bFMesher=True, iThreadNum=16)

# Check mesh quality
result = MeshCleanup.AutoCheck.TriQuad(crlTargets=[Part(1)],   # [hl:start]
                                        bStretchCheck=True, 
                                        bEdgeLengthCheck=True, 
                                        dStretchLimitTri=0.1, 
                                        dEdgeLengthLimitTri=0.0001, 
                                        dStretchLimitQuad=0.1, 
                                        dEdgeLengthLimitQuad=0.0001)  # [hl:end]
if result[1] >= 1 and result[2] < 1:
    print("There is no Quad error element")
    print("The number of Tri error elements is " + str(result[1]))
    print("The error elements are " + str(result[3]))
elif result[1] < 1 and result[2] >= 1:
    print("There is no Tri error element")
    print("The number of Quad error elements is " + str(result[2]))
    print("The error elements are " + str(result[3]))
elif result[1] >= 1 and result[2] >= 1:
    print("The number of Tri error elements is " + str(result[1]))
    print("The number of Quad error elements is " + str(result[2]))
    print("The error elements are " + str(result[3]))
else:
    print("There is no Tri Quad error element")
