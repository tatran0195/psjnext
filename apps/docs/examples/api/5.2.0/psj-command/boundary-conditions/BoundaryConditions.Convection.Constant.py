# Title:   BoundaryConditions.Convection.Constant()
# Desc:    Create natural convection condition on selected face, element or group. User inputs external temperature and convection coefficient in scalar or in a table format, then it will return convection load to the specified location
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/boundary-conditions/BoundaryConditions.Convection.Constant
# ---
Geometry.Part.Cube()

created_bcs = BoundaryConditions.Convection.Constant(strName="Convection_26",  # [hl]
                                                     dExternalTemp=373.15,   # [hl]
                                                     dConvectionCoef=1E-3,   # [hl]
                                                     crlTargets=[Face(26)])  # [hl]

JPT.Debugger(created_bcs)
