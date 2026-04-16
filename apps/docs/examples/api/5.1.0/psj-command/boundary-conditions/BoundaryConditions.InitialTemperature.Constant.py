# Title:   BoundaryConditions.InitialTemperature.Constant()
# Desc:    Create initial temperature with constant value
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/boundary-conditions/BoundaryConditions.InitialTemperature.Constant
# ---
Geometry.Part.Cube()
BoundaryConditions.InitialTemperature.Constant(  # [hl:start]
        strName="InitialTemperature_1",
        iLocalTemperatureUnit=1, 
        dFTemp=278.15, 
        bUseDefault=True, 
        crlTargets=[Part(1)])  # [hl:end]
