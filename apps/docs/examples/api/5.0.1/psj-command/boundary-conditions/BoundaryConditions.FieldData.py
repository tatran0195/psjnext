# Title:   BoundaryConditions.FieldData()
# Desc:    Create a field data table that can be used when you set load, the boundary conditions, etc.
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/boundary-conditions/BoundaryConditions.FieldData
# ---
created_lbc = BoundaryConditions.FieldData(strName="XYZ1",  # [hl:start]
                                           iType=1,
                                           ilSheet=[2,
                                                    4,
                                                    1,
                                                    1,
                                                    1,
                                                    10,
                                                    1,
                                                    2,
                                                    1,
                                                    20])  # [hl:end]

JPT.Debugger(created_lbc)
