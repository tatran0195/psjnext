# Title:   BoundaryConditions.LBCCopy.ConnectionCopyTranslate()
# Desc:    Copy boundary conditions by using translation method
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/boundary-conditions/BoundaryConditions.LBCCopy.ConnectionCopyTranslate
# ---
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], 
                   strName="Cube_3", 
                   iPartColor=13259210)

BoundaryConditions.FixedConstraint(crlTargets=[Face(76)])

created_lbc = BoundaryConditions.LBCCopy.LBCCopyTranslate(posVecTrans=[-0.001, 0, 0],   # [hl]
                                                          dMagnitude=0.03,   # [hl]
                                                          dTol=0.1,   # [hl]
                                                          crlTargets=[LbcConstraint(1)])  # [hl]

JPT.Debugger(created_lbc)
