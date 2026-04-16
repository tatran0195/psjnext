# Title:   BoundaryConditions.TemperatureLoads.NastranPunch()
# Desc:    Create temperature load by using Nastran punch
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/boundary-conditions/BoundaryConditions.TemperatureLoads.NastranPunch
# ---
# Prepare mapping data as .pch
mapping_data_file = "C:/temp/test.pch"

# Prepare model
Geometry.Part.Cube(iPartColor=6409934)

BoundaryConditions.TemperatureLoads.NastranPunch(  # [hl:start]
    strName = "TemperatureLoadsPunch_1", 
    strFilePathName = mapping_data_file)  # [hl:end]
