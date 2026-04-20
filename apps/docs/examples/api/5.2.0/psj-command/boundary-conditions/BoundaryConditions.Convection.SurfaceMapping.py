# Title:   BoundaryConditions.Convection.SurfaceMapping()
# Desc:    Create load boundary condition of convection surface mapping
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/boundary-conditions/BoundaryConditions.Convection.SurfaceMapping
# ---
result = BoundaryConditions.Convection.SurfaceMapping(strName="MappingConvection_5",
    crlTargets=[], iPos=0, iViewCp=0, iCp=0, iSrcType=0, iMappedCpIndex0=0,
    iMappedCpIndex1=0, dRScale=1.0, posOffset=[0,0,0], posAxis=[0,0,0], dTScale=1.0,
    dSearchRange=1.0, iHTCUnit=0, iTempUnit=0, strPath="", crEdit=None)

print(result) #for checking return value
