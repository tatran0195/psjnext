# Title:   MeshCleanup.AutoCheck.Tri()
# Desc:    Correct the surface mesh (TRI3/TRI6) by using multiple mesh quality standard
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/mesh-cleanup/MeshCleanup.AutoCheck.Tri
# ---
# Prepare model
Geometry.Part.Cube(dlLength=[0.01, 0.01, 0.0001], 
                    ilAxialNodes=[10, 10, 2], 
                    iPartColor=7697908)
Meshing.SurfaceMeshing(crlParts=[Part(1)], 
                    surfaceMesh=SURFACE_MESH(
                        dAvgElemSize=0.001, 
                        dMinElemSize=0.0001, 
                        dGeomAngle=0.7853981634, 
                        dGeomMinSize=0.0001, 
                        dGradingFactor=0.5, 
                        iPerformanceMode=1, 
                        dAutoMergeTinyFacesAngle=0.5235987756, 
                        bGeomApprox=True, 
                        iNextEntityOffsetId=0), 
                        iThreadNum=16)

# Check mesh quality
result = MeshCleanup.AutoCheck.Tri(crlTargets=[Part(1)],   # [hl:start]
                                bEdgeLengthCheck=True, 
                                dEdgeLengthLimit=0.0001)  # [hl:end]
if result[1] >=1:
    print("The number of error elements is " + str(result[1]))
    print("The error elements are " + str(result[2]))
else:
    print("There is no error element")
