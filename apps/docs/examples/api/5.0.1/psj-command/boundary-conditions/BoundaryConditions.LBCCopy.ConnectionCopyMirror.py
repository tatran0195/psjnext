# Title:   BoundaryConditions.LBCCopy.ConnectionCopyMirror()
# Desc:    Copy boundary conditions by using mirror method
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/boundary-conditions/BoundaryConditions.LBCCopy.ConnectionCopyMirror
# ---
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], 
                   strName="Cube_3", 
                   iPartColor=13259210)

BoundaryConditions.FixedConstraint(crlTargets=[Face(76)])

MeshEdit.CreateNode.Between2Nodes(iNodeID=1465, 
                                  dX=1.5e-05, 
                                  dY=1e-05, 
                                  dZ=1e-05, 
                                  iNumberofNodes=1, 
                                  crlNodes=[Node(581, 580)])
MeshEdit.CreateNode.Between2Nodes(iNodeID=1466, 
                                  dX=1.5e-05, 
                                  dY=1e-05, 
                                  iNumberofNodes=1, 
                                  crlNodes=[Node(517, 516)])
MeshEdit.CreateNode.Between2Nodes(iNodeID=1467, 
                                  dX=1.5e-05, 
                                  dZ=1e-05, 
                                  iNumberofNodes=1, 
                                  crlNodes=[Node(565, 564)])

created_lbc = BoundaryConditions.LBCCopy.LBCCopyMirror(poslPoints=[[0.015, 0, 0.01],   # [hl]
                                                                   [0.015, 0.01, 0.01],   # [hl]
                                                                   [0.015, 0.01, 0]],   # [hl]
                                                       dTol=0.1,   # [hl]
                                                       crlTargets=[LbcConstraint(1)])  # [hl]

JPT.Debugger(created_lbc)
