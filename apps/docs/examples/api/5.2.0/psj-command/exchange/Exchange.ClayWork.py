# Title:   Exchange.ClayWork()
# Desc:    Make a simple design change for solid mesh parts
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/exchange/Exchange.ClayWork
# ---
# Prepare model
Geometry.Part.Cube(iPartColor=6409934)
Meshing.SolidMeshing(
	crlParts=[Part(1)], 
	dGradingFactor=1.05, 
	dStretchLimit=0.1, 
	iSpeedVsQual=1, 
	iRegion=1, 
	bSafeMode=False, 
	iParallel=16, 
	bInternalMeshOnly=False, 
	iPartColor=65280)

# Add spheres
ret1 = Exchange.ClayWork(  # [hl:start]
		iProcesstype=0, 
		dlSphereCenter=[
			[0.006, 0.01, 0.002], [0.006, 0.01, 0.003], [0.006, 0.01, 0.004], [0.006, 0.01, 0.006], 
			[0.006, 0.01, 0.007], [0.004, 0.01, 0.007], [0.004, 0.01, 0.006], [0.004, 0.01, 0.004], 
			[0.004, 0.01, 0.003], [0.004, 0.01, 0.002]], 
		dSphereRadius=0.002)  # [hl:end]
print(ret1)

# Pile up the wrapped sphere
ret2 = Exchange.ClayWork(iProcesstype=1, iWrappingType=1, iFactor = 0.6, crTargetPart=Part(1))  # [hl]
print(ret2)
