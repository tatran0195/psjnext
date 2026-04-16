# Title:   Connections.MPC.Equation.MultiNodes()
# Desc:    Create a MPC connection between a slave node with multi-master nodes
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/connections/Connections.MPC.Equation.MultiNodes
# ---
Geometry.Part.Cube(iPartColor = 7666683)
Geometry.Part.Cube(dlOrigin = [0.02, 0.0, 0.0], 
                   strName = "Cube_2", 
                   iPartColor = 12867524)

created_mpc = Connections.MPC.Equation.MultipleNodes(crlMasterNodes=[Node(340,  # [hl]
                                                                          344,   # [hl]
                                                                          353)],  # [hl]
                                                     crSlaveNode=Node(757),   # [hl]
                                                     listMpcConnection=[MPC_CONNECTION(dCoef=1.0,   # [hl]
                                                                                       iDof=1),  # [hl]
                                                                        MPC_CONNECTION(dCoef=1.0,   # [hl]
                                                                                       iDof=1),   # [hl]
                                                                        MPC_CONNECTION(dCoef=1.0,   # [hl]
                                                                                       iDof=1),  # [hl]
                                                                        MPC_CONNECTION(dCoef=1.0,   # [hl]
                                                                                       iDof=1)],   # [hl]
                                                     bUpdateDispCS=1)  # [hl]

JPT.Debugger(created_mpc)
