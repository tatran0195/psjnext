# Title:   BoundaryConditions.InitialTemperature.WholeMapping()
# Desc:    Create initial temperature whole mapping
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/boundary-conditions/BoundaryConditions.InitialTemperature.WholeMapping
# ---
# Prepare model
Geometry.Part.Cube(iPartColor=6409934)
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
    PartColor=65280)

# Assume nastran result include temperature more than 6 steps is at C:/Temp/transient.op2

BoundaryConditions.InitialTemperature.WholeMapping(  # [hl:start]
    strName="TemperatureInitsWholeMapping_3", 
    crlTargets=[Part(1)], 
    strPath="C:/Temp/transient.op2",
    iMappingFromStepNo=5, 
    iLocalUnit=1)  # [hl:end]
