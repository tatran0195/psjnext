# Title:   Exchange.AssembleSolidMesh()
# Desc:    Assemble solid mesh parts
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/exchange/Exchange.AssembleSolidMesh
# ---
# Prepare model
Geometry.Part.Cube(iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.0101, 0.0, 0.0], strName="Cube_2", iPartColor=14903267)
Meshing.AdjustCircleVertex(crlParts=[Part(2)], bInModeSurfaceMesh=True)
Meshing.SetMeshAttribute(
    crlParts=[Part(2)], 
    surfaceMesh=SURFACE_MESH(
        dAvgElemSize=0.0015,
         dGeomAngle=0.7853981634, 
         iPerformanceMode=1, 
         dAutoMergeTinyFacesAngle=0.5235987756, 
         bGeomApprox=True))
Meshing.SurfaceMeshing(
    crlParts=[Part(2)], 
    surfaceMesh=SURFACE_MESH(
        dAvgElemSize=0.0015, 
        dGeomAngle=0.7853981634, 
        iPerformanceMode=1, 
        dAutoMergeTinyFacesAngle=0.5235987756, 
        bGeomApprox=True), 
    iThreadNum=16)
Meshing.SolidMeshing(
    rlParts=[Part(2, 1)], 
    dGradingFactor=1.05, 
    dStretchLimit=0.1, 
    iSpeedVsQual=1, 
    iRegion=1, 
    bSafeMode=False, 
    iParallel=16, 
    bInternalMeshOnly=False, 
    iPartColor=65280)

# Assemble solid mesh
ret = Exchange.AssembleSolidMesh(crNewPart=Part(2), crlAssembleParts=[Part(1)], dTolerance=0.0002,   # [hl]
    iConnectPosition=1, bRemeshAuto=False, dAvg=0.0012, dMin=0.0001, dMax=0.002)  # [hl]
print(assemble_sretolid)
