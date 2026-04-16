# Title:   BoundaryConditions.InitialTemperature.Constant()
# Desc:    Create initial temperature with constant value
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/boundary-conditions/BoundaryConditions.InitialTemperature.Constant
# ---
Geometry.Part.Cube()
BoundaryConditions.InitialTemperature.Constant(strName="InitialTemperature4",
	dFTemp=278.15, bUseDefault=True, crlTargets=[Part(1)])
