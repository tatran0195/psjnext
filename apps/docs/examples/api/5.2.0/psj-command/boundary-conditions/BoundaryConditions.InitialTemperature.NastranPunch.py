# Title:   BoundaryConditions.InitialTemperature.NastranPunch()
# Desc:    Load the temperature result output in Nastran Punch format and set as the initial temperature
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/boundary-conditions/BoundaryConditions.InitialTemperature.NastranPunch
# ---
# Prepare .pch file for setting
mapping_data_file = "C:/temp/test.pch"  # [hl:start]

Geometry.Part.Cube()
BoundaryConditions.InitialTemperature.NastranPunch(
        strName="InitialTemperature_1",
        iLocalTemperatureUnit=1,   # [hl:end]
        strFilePathName = mapping_data_file,
        crlTargets=[Part(1)])
