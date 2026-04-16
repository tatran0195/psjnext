# Title:   BoundaryConditions.EnforcedLoads.Velocity()
# Desc:    Create enforced velocity to face, edge or node. User inputs enforced velocity parameters, and it will return enforced velocity to the specified location
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/boundary-conditions/BoundaryConditions.EnforcedLoads.Velocity
# ---
Geometry.Part.Cube()

created_bcs = BoundaryConditions.EnforcedLoads.Velocity(enforceVelocity=ENFORCED_VELOCITY_LBC(iDwDof=1,  # [hl]
                                                                                              dVelocityTX=0.001),   # [hl]
                                                        crlTargets=[Face(24)])  # [hl]

JPT.Debugger(created_bcs)
