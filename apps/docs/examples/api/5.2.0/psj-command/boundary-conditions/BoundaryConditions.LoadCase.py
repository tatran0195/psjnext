# Title:   BoundaryConditions.LoadCase()
# Desc:    Create a load case that bundles loads and constraints. Load cases can be referenced when creating analysis solver input data
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/boundary-conditions/BoundaryConditions.LoadCase
# ---
Geometry.Part.Cube()

BoundaryConditions.Pressure.General(dPressure=1000000.0, 
                                    crlTargets=[Face(24)])

BoundaryConditions.Pressure.General(strName="Pressure2", 
                                    dPressure=2000000.0,
                                    crlTargets=[Face(21)])

BoundaryConditions.Pressure.General(strName="Pressure3", 
                                    dPressure=3000000.0,
                                    crlTargets=[Face(25)])

created_bcs = BoundaryConditions.LoadCase(crlTargets=[LbcGPressure(1, 2, 3)],   # [hl]
                                          iExportId=4,  # [hl]
                                          dlTargetFactor=[1.0, 1.0, 1.0])  # [hl]

JPT.Debugger(created_bcs)
