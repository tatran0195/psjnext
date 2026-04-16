# Title:   BoundaryConditions.EnforcedLoads.Displacement()
# Desc:    Create enforced displacement to face, edge or node. User inputs enforced displacement parameters, and it will return enforced displacement to the specified location
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/boundary-conditions/BoundaryConditions.EnforcedLoads.Displacement
# ---
Geometry.Part.Cube()

created_bcs = BoundaryConditions.EnforcedLoads.Displacement(strName="EnforcedDisplacement1",   # [hl]
                                                            iDof=9,  # [hl]
                                                            dDispUx=0.001,   # [hl]
                                                            dDispRx=1.0,   # [hl]
                                                            dPhase=0.0,   # [hl]
                                                            dDelay=0.0,   # [hl]
                                                            crlTargets=[Face(25)])  # [hl]

JPT.Debugger(created_bcs)
