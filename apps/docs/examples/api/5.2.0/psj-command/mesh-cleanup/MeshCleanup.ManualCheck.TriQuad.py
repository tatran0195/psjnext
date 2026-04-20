# Title:   MeshCleanup.ManualCheck.TriQuad()
# Desc:    Correct the surface mesh (TRI3/TRI6/QUAD4/QUAD8) according to the selected quality standard
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/mesh-cleanup/MeshCleanup.ManualCheck.TriQuad
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
                        iNextEntityOffsetId=0), 
                    bFMesher=True, 
                    iThreadNum=16)

# Check mesh quality
result = MeshCleanup.ManualCheck.TriQuad(crlTargets=[Part(1)],   # [hl:start]
                                        iCheckConditionTri=0, 
                                        dLimitValueTri=0.2, 
                                        iCheckConditionQuad=0, 
                                        dLimitValueQuad=0.1)  # [hl:end]
if result[0] == 1:
    if result[5] > 0:
        print(f'The number of Tri elements that have stretch error is {result[5]}. max value={result[1]}, min value={result[2]}')
        print(f'The error elements are {result[6]}')
    else:
        print("There is no Tri error element")
    if result[12] > 0:
        print(f'The number of Quad elements that have stretch error is {result[12]}. max value={result[8]}, min value={result[9]}')
        print(f'The error elements are {result[13]}')
    else:
        print("There is no Quad error element")
else:
    print("There is no error element")
