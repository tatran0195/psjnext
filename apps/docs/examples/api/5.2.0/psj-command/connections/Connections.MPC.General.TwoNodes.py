# Title:   Connections.MPC.General.TwoNodes()
# Desc:    Create a MPC connection between slave nodes to master nodes one-to-one correspondingly. The sequence of nodes selection is the first master node, the first slave node, the second master node, the second slave node and so on
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/connections/Connections.MPC.General.TwoNodes
# ---
Geometry.Part.Cube(iPartColor=7666683)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=12867524)

created_mpc = Connections.MPC.General.TwoNodes(strName="MPC_10",   # [hl:start]
                                               crlMasterNodes=[Node(757)],
                                               crlSlaveNodes=[Node(347)], 
                                               listMpcConnection=[MPC_CONNECTION(iDof=1), 
                                                                  MPC_CONNECTION(iDof=2),
                                                                  MPC_CONNECTION(iDof=4), 
                                                                  MPC_CONNECTION(), 
                                                                  MPC_CONNECTION(), 
                                                                  MPC_CONNECTION()],
                                               bUpdateDispCS=1)  # [hl:end]

JPT.Debugger(created_mpc)
