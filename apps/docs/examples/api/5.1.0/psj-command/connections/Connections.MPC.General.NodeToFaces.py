# Title:   Connections.MPC.General.NodeToFaces()
# Desc:    Create a MPC between a node and multiple faces
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/connections/Connections.MPC.General.NodeToFaces
# ---
Geometry.Part.Cube(iPartColor=7666683)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=12867524)

created_mpc = Connections.MPC.General.NodeToFaces(strName="MPC_9",   # [hl]
                                                  crMasterNode=Node(758),  # [hl]
                                                  crlSlaveFaces=[Face(24)],   # [hl]
                                                  listMpcConnection=[MPC_CONNECTION(iDof=1),   # [hl]
                                                                     MPC_CONNECTION(iDof=2),  # [hl]
                                                                     MPC_CONNECTION(iDof=4),   # [hl]
                                                                     MPC_CONNECTION(),   # [hl]
                                                                     MPC_CONNECTION(),   # [hl]
                                                                     MPC_CONNECTION()],  # [hl]
                                                  bUpdateDispCS=1)  # [hl]

JPT.Debugger(created_mpc)
