# Title:   Connections.MPC.General.NodesToNodes()
# Desc:    Create MPC between selected nodes
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/connections/Connections.MPC.General.NodesToNodes
# ---
Geometry.Part.Cube(iPartColor=7666683)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=12867524)

created_mpc = Connections.MPC.General.NodesToNodes(strName="MPC_5",   # [hl]
                                                   crlMasterNodes=[Node(760,   # [hl]
                                                                        770)],  # [hl]
                                                   crlSlaveNodes=[Node(323,   # [hl]
                                                                       310)],   # [hl]
                                                   listMpcConnection=[MPC_CONNECTION(dCoef=1.0,   # [hl]
                                                                                     iDof=1),  # [hl]
                                                                      MPC_CONNECTION(dCoef=1.0,   # [hl]
                                                                                     iDof=2),   # [hl]
                                                                      MPC_CONNECTION(dCoef=1.0,   # [hl]
                                                                                     iDof=4),   # [hl]
                                                                      MPC_CONNECTION(),  # [hl]
                                                                      MPC_CONNECTION(),   # [hl]
                                                                      MPC_CONNECTION()],   # [hl]
                                                   bUpdateDispCS=1)  # [hl]
    
JPT.Debugger(created_mpc)
