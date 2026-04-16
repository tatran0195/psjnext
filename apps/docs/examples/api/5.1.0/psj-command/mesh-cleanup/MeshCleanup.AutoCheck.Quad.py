# Title:   MeshCleanup.AutoCheck.Quad()
# Desc:    Correct the surface mesh (QUAD4/QUAD8) by using multiple mesh quality standards
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/mesh-cleanup/MeshCleanup.AutoCheck.Quad
# ---
# Prepare model
Geometry.Part.Cube(dlLength=[0.01, 0.01, 0.0001], 
                    ilAxialNodes=[10, 10, 2], 
                    iPartColor=7697908)
JPT.Exec("View Fit To Model()")
Meshing.SurfaceMeshing(crlParts=[Part(1)], 
                    surfaceMesh=SURFACE_MESH(
                        dMaxElemSize=0.005, 
                        dMinElemSize=0.005, 
                        dGeomAngle=0.7853981634, 
                        dGradingFactor=0.5, iPerformanceMode=1, 
                        dAutoMergeTinyFacesAngle=0.5235987756, 
                        bOutputQuadMesh=True, 
                        bGeomApprox=True, 
                        iNextEntityOffsetId=0), 
                        bFMesher=True, 
                        iThreadNum=16)

# Check mesh quality
result = MeshCleanup.AutoCheck.Quad(crlTargets=[Part(1)],   # [hl:start]
                                    bStretchCheck=True, 
                                    bWarpingCheck=True, 
                                    dStretchLimit=0.1, 
                                    dWarpingLimit=0.0174533)  # [hl:end]
if result[1] >=1:
    print("The number of error elements is " + str(result[1]))
    print("The error elements are " + str(result[2]))
else:
    print("There is no error element")
