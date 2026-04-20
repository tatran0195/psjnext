# Title:   MeshCleanup.ManualCheck.Tet()
# Desc:    Correct the solid mesh (Tet4/Tet10) according to the selected quality standard
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/mesh-cleanup/MeshCleanup.ManualCheck.Tet
# ---
# Prepare model
Geometry.Part.Cube(dlLength=[0.01, 0.01, 0.0001], 
                ilAxialNodes=[10, 10, 2], 
                strName="Cube_1", 
                iPartColor=13259210)

Meshing.SurfaceMeshing(crlParts=[Part(1)], 
                    surfaceMesh=SURFACE_MESH(
                        dMaxElemSize=0.1, 
                        dGeomAngle=0.7853981634, 
                        dMinStretchVal=0.0, 
                        iPerformanceMode=1, 
                        dAutoMergeTinyFacesAngle=0.5235987756, 
                        bGeomApprox=True, 
                        iNextEntityOffsetId=0))

Meshing.SolidMeshing(crlParts=[Part(1)], 
                    bTet10=True, 
                    dGradingFactor=1.0, 
                    iSpeedVsQual=1, 
                    bSafeMode=False, 
                    iParallel=8, 
                    bSurfaceNodes=False, 
                    bEdgeNodes=False, 
                    bInternalMeshOnly=False, 
                    iPartColor=65280)

# Check mesh quality
result = MeshCleanup.ManualCheck.Tet(crlTargets=[Part(1)], iCheckCondition=0, dLimitValue=0.1)  # [hl]
(success_flag,min,max,avg,target_num,error_num,errors1,errors2) = result
if result[0] == 1:
    print(f'The number of elements that have stretch error is {error_num}. max value={max}, min value={min}')
    print(f'The error elements are {errors1}')
else:
    print("There is no error element")
