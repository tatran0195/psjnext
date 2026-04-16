# Title:   Connections.MPC.General.TwoEdges()
# Desc:    Create MPC between two edges
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/connections/Connections.MPC.General.TwoEdges
# ---
Geometry.Part.Cube(iPartColor=7666683)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=12867524)

created_mpc = Connections.MPC.General.TwoEdges(strName="MPC_11",   # [hl]
                                               crMasterEdge=Edge(46),  # [hl]
                                               crSlaveEdge=Edge(10),   # [hl]
                                               listMpcConnection=[MPC_CONNECTION(iDof=1),   # [hl]
                                                                  MPC_CONNECTION(iDof=2),  # [hl]
                                                                  MPC_CONNECTION(iDof=4),   # [hl]
                                                                  MPC_CONNECTION(iDof=8),   # [hl]
                                                                  MPC_CONNECTION(),  # [hl]
                                                                  MPC_CONNECTION(iDof=32)],   # [hl]
                                               bUpdateDispCS=1)  # [hl]

JPT.Debugger(created_mpc)
