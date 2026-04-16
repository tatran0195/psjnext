# Title:   BoundaryConditions.EnforcedLoads.Acceleration()
# Desc:    Create enforced acceleration to face, edge or node. User inputs enforced acceleration parameters, and it will return enforced acceleration to the specified location
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/boundary-conditions/BoundaryConditions.EnforcedLoads.Acceleration
# ---
Geometry.Part.Cube()

created_bcs = BoundaryConditions.EnforcedLoads.Acceleration(dAccelUz=0.01,   # [hl]
                                                            crlTargets=[Face(26)])  # [hl]

JPT.Debugger(created_bcs)
