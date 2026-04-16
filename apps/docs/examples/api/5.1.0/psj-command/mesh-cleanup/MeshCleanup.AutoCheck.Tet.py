# Title:   MeshCleanup.AutoCheck.Tet()
# Desc:    Correct the solid mesh (TET4/TET10) by using multiple mesh quality standard
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/mesh-cleanup/MeshCleanup.AutoCheck.Tet
# ---
# Prepare model
Geometry.Part.Cube(dlLength=[0.01, 0.01, 0.0001], 
                    ilAxialNodes=[10, 10, 2], 
                    iPartColor=7697908)
JPT.Exec("View Fit To Model()")
Meshing.SolidMeshing(crlParts=[Part(1)], 
                    dGradingFactor=1.05, 
                    dStretchLimit=0.1, 
                    iSpeedVsQual=1, 
                    iRegion=1, 
                    bSafeMode=False, 
                    iParallel=16, 
                    bInternalMeshOnly=False, 
                    iPartColor=65280)

# Check mesh quality
result = MeshCleanup.AutoCheck.Tet(crlTargets=[Part(1)],   # [hl:start]
                                    bTetSkewCheck=True, 
                                    dTetSkewLimit=0.9)  # [hl:end]
if result[1] >=1:
    print("The number of error elements is " + str(result[1]))
    print("The error elements are " + str(result[2]))
else:
    print("There is no error element")
