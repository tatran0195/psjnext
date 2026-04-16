# Title:   BoundaryConditions.Submodel.ForcedTempertature()
# Desc:    Create a submodel by using temperature field from the coarse model and apply it to the submodel as a boundary condition to get the accurate highly-refined response in the area of interest
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/boundary-conditions/BoundaryConditions.Submodel.ForcedTempertature
# ---
Geometry.Part.Cube()
created_lbc = BoundaryConditions.Submodel.ForcedTempertature(strName="SubmodelForcedTemperature1",  # [hl:start]
                                                             iReferType=-1,
                                                             crlTargets=[Face(26)])  # [hl:end]
JPT.Debugger(created_lbc)
