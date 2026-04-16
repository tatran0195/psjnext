# Title:   BoundaryConditions.LBCCopy.ConnectionCopyRotate()
# Desc:    Copy boundary conditions by using rotation method
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/boundary-conditions/BoundaryConditions.LBCCopy.ConnectionCopyRotate
# ---
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], 
                   strName="Cube_3", 
                   iPartColor=13259210)

BoundaryConditions.FixedConstraint(crlTargets=[Face(76)])

created_lbc = BoundaryConditions.LBCCopy.LBCCopyRotate(posAxis=[0, 0.001, 0],   # [hl]
                                                       posCenter=[0.015, 0.005, 0.005],   # [hl]
                                                       dAngle=180.0,   # [hl]
                                                       dTol=0.1,   # [hl]
                                                       crlTargets=[LbcConstraint(1)])  # [hl]

JPT.Debugger(created_lbc)
