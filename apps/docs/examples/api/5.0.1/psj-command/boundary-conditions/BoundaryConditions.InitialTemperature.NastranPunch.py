# Title:   BoundaryConditions.InitialTemperature.NastranPunch()
# Desc:    Load the temperature result output in Nastran Punch format and set as the initial temperature
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/boundary-conditions/BoundaryConditions.InitialTemperature.NastranPunch
# ---
Geometry.Part.Cube()
BoundaryConditions.InitialTemperature.NastranPunch(strFilePathName="C:/Desktop/test.pch",
	crlTargets=[Part(1)])
