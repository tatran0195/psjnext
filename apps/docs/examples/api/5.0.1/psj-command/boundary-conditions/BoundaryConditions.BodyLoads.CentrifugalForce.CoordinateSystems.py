# Title:   BoundaryConditions.BodyLoads.CentrifugalForce.CoordinateSystems()
# Desc:    Create the centrifugal force load to refer to the coordinate system in the analysis model
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/boundary-conditions/BoundaryConditions.BodyLoads.CentrifugalForce.CoordinateSystems
# ---
Geometry.Part.Cube()
Tools.Coordinates.ThreeNode(crlNodes=[Node(5, 8, 7)])

created_lbc = BoundaryConditions.BodyLoads.CentrifugalForce.CoordinateSystems(crlTargets=[Part(1)],  # [hl]
                                                                              dVelocity=10.0,  # [hl]
                                                                              dAcceleration=10.0,  # [hl]
                                                                              iAxisDirection=2,  # [hl]
                                                                              crCurCoord=Coord(1))  # [hl]

JPT.Debugger(created_lbc)
