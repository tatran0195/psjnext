# Title:   MeshCleanup.ManualCheck.Hex()
# Desc:    Correct the solid mesh (Hex8) according to the selected quality standard
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/mesh-cleanup/MeshCleanup.ManualCheck.Hex
# ---
# Prepare model
Geometry.Part.Cube()
Meshing.SurfaceMeshing(crlParts=[Part(1)], 
                    surfaceMesh=SURFACE_MESH(
                        dMaxElemSize=0.005, 
                        dMinElemSize=0.005, 
                        dGeomAngle=0.7853981634, 
                        dMinStretchVal=0.0, 
                        iPerformanceMode=1, 
                        dAutoMergeTinyFacesAngle=0.5235987756, 
                        bOutputQuadMesh=True, 
                        bGeomApprox=True, 
                        iNextEntityOffsetId=0), 
                    bFMesher=True)
HexModeling.Linear(crlFaces=[Face(26)], 
                dLength=0.0001, iLayer=1, 
                vecSweepDirection=[0.0, 0.0, 1.0], 
                bDeleteOriginalParts=True)

# Check mesh quality
result = MeshCleanup.ManualCheck.Hex(crlTargets=[Part(1)], iCheckCondition=0, dLimitValue=0.1)   # [hl]
(success_flag,min,max,avg,target_num,error_num,errors1,errors2) = result
if result[0] == 1:
    print(f'The number of elements that have stretch error is {error_num}. max value={max}, min value={min}')
    print(f'The error elements are {errors1}')
else:
    print("There is no error element")
