# Title:   Connections.MPC.General.NodesWithTolerance()
# Desc:    Create a one-to-one MPC pair between multiple selected nodes within an arbitrary tolerance
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/connections/Connections.MPC.General.NodesWithTolerance
# ---
Geometry.Part.Cube(iPartColor=7666683)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=12867524)

created_mpc = Connections.MPC.General.NodesWithTolerance(strName="MPC_6",  # [hl]
                                                         crlMasterNodes=[Node(324, 766)],   # [hl]
                                                         listMpcConnection=[MPC_CONNECTION(iDof=1),  # [hl]
                                                                            MPC_CONNECTION(iDof=2),   # [hl]
                                                                            MPC_CONNECTION(iDof=4),   # [hl]
                                                                            MPC_CONNECTION(),   # [hl]
                                                                            MPC_CONNECTION(),  # [hl]
                                                                            MPC_CONNECTION()],   # [hl]
                                                         dSearchTol=0.02,   # [hl]
                                                         bUpdateDispCS=1)  # [hl]
  # [hl]
JPT.Debugger(created_mpc)
