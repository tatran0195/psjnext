# Title:   Connections.MPC.General.NodeToNode()
# Desc:    Create a MPC connection between slave nodes to master nodes one-to-one correspondingly. The sequence of nodes selection is the first master node, the first slave node, the second master node, the second slave node and so on
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/connections/Connections.MPC.General.NodeToNode
# ---
Geometry.Part.Cube(iPartColor=7666683)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=12867524)

created_mpc = Connections.MPC.General.TwoNodes(strName="MPC_10",   # [hl]
                                               crlMasterNodes=[Node(757)],  # [hl]
                                               crlSlaveNodes=[Node(347)],   # [hl]
                                               listMpcConnection=[MPC_CONNECTION(iDof=1),   # [hl]
                                                                  MPC_CONNECTION(iDof=2),  # [hl]
                                                                  MPC_CONNECTION(iDof=4),   # [hl]
                                                                  MPC_CONNECTION(),   # [hl]
                                                                  MPC_CONNECTION(),   # [hl]
                                                                  MPC_CONNECTION()],  # [hl]
                                               bUpdateDispCS=1)  # [hl]

JPT.Debugger(created_mpc)
