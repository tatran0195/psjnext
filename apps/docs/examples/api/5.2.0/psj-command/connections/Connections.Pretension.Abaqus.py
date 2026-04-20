# Title:   Connections.Pretension.Abaqus()
# Desc:    Create bolt pretension for the Abaqus solver
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/connections/Connections.Pretension.Abaqus
# ---
Geometry.Part.Cylinder(dHeight=0.04,
                       iPartColor=6447843)
MeshEdit.CreateNode.Between2Nodes(iNodeID=363,
                                  dX=7.66044e-06, 
                                  dY=2e-05, 
                                  dZ=-6.42788e-06, 
                                  iNumberofNodes=1, 
                                  crlNodes=[Node(65, 
                                                 66)])
MeshEdit.CreateNode.Between2Nodes(iNodeID=364, 
                                  dX=-1.73648e-06, 
                                  dY=2e-05, 
                                  dZ=9.84808e-06, 
                                  iNumberofNodes=1, 
                                  crlNodes=[Node(21, 
                                                 22)])
MeshEdit.CreateNode.Between2Nodes(iNodeID=365, 
                                  dX=-3.4202e-06, 
                                  dY=2e-05, 
                                  dZ=-9.39693e-06, 
                                  iNumberofNodes=1, 
                                  crlNodes=[Node(51, 
                                                 52)])
Geometry.BodyCut.By3Points(crPart=Part(1), 
                           poslPoints=[[-0.003420201433256686, 0.02, -0.009396926207859084], 
                                       [0.007660444431189778, 0.02, -0.006427876096865396], 
                                       [-0.001736481776669303, 0.02, 0.00984807753012208]], 
                           bSplitOnly=True)
MeshEdit.DeleteNode()

max_node_id=JPT.GetMaxIDEntity(JPT.EntityType.NODE)  # [hl]
  # [hl]
creating_status = Connections.Pretension.Abaqus(crlTargets=[Face(11)],   # [hl]
                                                dForceValue=1000000.0,   # [hl]
                                                dlForceDirection=[0.000000,  # [hl]
                                                                  -1.000000,  # [hl]
                                                                  0.000000],  # [hl]
                                                dlControlNode=[0.001419156,   # [hl]
                                                               0.02, 
                                                               0.00012416],
                                                iRefNodeID=max_node_id+1)

JPT.Debugger(creating_status)
