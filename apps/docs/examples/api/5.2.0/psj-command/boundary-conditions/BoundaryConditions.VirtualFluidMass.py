# Title:   BoundaryConditions.VirtualFluidMass()
# Desc:    Create a virtual fluid mass.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/boundary-conditions/BoundaryConditions.VirtualFluidMass
# ---
Geometry.Part.Cube(
    ilAxialNodes=[4, 4, 4], 
    strName="Cube_2", 
    iPartColor=14903267)
    
Meshing.SolidMeshing(
    crlParts=[Part(1)], 
    bTet10=True, 
    dGradingFactor=1.05, 
    dStretchLimit=0.1, 
    iSpeedVsQual=1, 
    iRegion=1, 
    bSafeMode=False, 
    iParallel=16, 
    bInternalMeshOnly=False, 
    iPartColor=65280)

BoundaryConditions.VirtualFluidMass(  # [hl:start]
    crlTargetFaces=[Face(26, 24, 22, 23, 21)], 
    crlNegativeSideTargets=[Face(24, 22, 23, 21)],
    dFluidDensity=1000000000000000.0)  # [hl:end]
