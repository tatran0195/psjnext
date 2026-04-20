# Title:   BoundaryConditions.BodyLoads.CentrifugalForce.TwoPositions()
# Desc:    Create the centrifugal force load in the analysis model
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/boundary-conditions/BoundaryConditions.BodyLoads.CentrifugalForce.TwoPositions
# ---
Geometry.Part.Cube()

created_lbc = BoundaryConditions.BodyLoads.CentrifugalForce.TwoPositions(crlTargets=[Part(1),  # [hl]
                                                                                     Node(5, 3)],  # [hl]
                                                                         dBasePointZ=0.01,  # [hl]
                                                                         dTipPointX=0.01,  # [hl]
                                                                         dTipPointY=0.01,  # [hl]
                                                                         dVelocity=10.0,  # [hl]
                                                                         dAcceleration=10.0)  # [hl]

JPT.Debugger(created_lbc)
