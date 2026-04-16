# Title:   BoundaryConditions.HeatFlux.SurfaceMapping()
# Desc:    Create surface mapping heat flux
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/boundary-conditions/BoundaryConditions.HeatFlux.SurfaceMapping
# ---
result = BoundaryConditions.HeatFlux.SurfaceMapping(strName="MappingHeatFlux",
	crlTargets=[], iMAPPos=0, iViewCp=0, iCp=1, iSrcType=0, iMappedCpIndexArr0=0,
	dScaleFactor=1.0,	posOffset=[0,0,0], posRotate=[0,0,0], dCorScale=1.0, dSearchRange=0.0,
	iUnit=0, strStrpath="",	crEdit=None, iMappingMethod=0, iSubmodeLBCMappingType=4,
	iMappingFromStepNo=0, bSetADVCFile=False, strADVCResultFile="", bSetDetATol=False,
	dDetATol=DFLT_DBL, bSetElementSet=False, strElementSet="all")

print(result) #for checking return value
