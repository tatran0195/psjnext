# Title:   BoundaryConditions.TemperatureLoads.WholeMapping()
# Desc:    Map temperagure load from solver data or csv.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/boundary-conditions/BoundaryConditions.TemperatureLoads.WholeMapping
# ---
# Put solver data that includes temperature data.
mapping_data_file = "C:/Temp/sol159.op2"

# Prepare model
Geometry.Part.Cube(iPartColor=6409934)

# Map temperature load
BoundaryConditions.TemperatureLoads.WholeMapping(  # [hl:start]
    strName = "TemperatureLoadsWholeMapping_1", 
    strPath = mapping_data_file, 
    iMappingFromStepNo = 0)  # [hl:end]
