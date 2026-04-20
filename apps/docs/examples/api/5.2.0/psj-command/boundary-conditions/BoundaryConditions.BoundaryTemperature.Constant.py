# Title:   BoundaryConditions.BoundaryTemperature.Constant()
# Desc:    Create a constant temperature load to part, face, edge or node. User inputs temperature in scalar or in a table format, then it will return temperature load to the specified location
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/boundary-conditions/BoundaryConditions.BoundaryTemperature.Constant
# ---
Geometry.Part.Cube()

created_bcs = BoundaryConditions.BoundaryTemperature.Constant(strName="BoundaryTemperature_21",  # [hl]
                                                              dFTemp=373.15,   # [hl]
                                                              crlTargets=[Face(21)])  # [hl]

JPT.Debugger(created_bcs)
