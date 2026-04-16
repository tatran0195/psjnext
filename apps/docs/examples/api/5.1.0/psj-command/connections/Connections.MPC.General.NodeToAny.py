# Title:   Connections.MPC.General.NodeToAny()
# Desc:    Create MPC between a selected node and any types of entities such as nodes, edges or faces
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/connections/Connections.MPC.General.NodeToAny
# ---
Geometry.Part.Cube(iPartColor=7666683)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=12867524)

created_mpc = Connections.MPC.General.NodeToAny(strName="MPC_7",   # [hl]
                                                crMasterNode=Node(757),  # [hl]
                                                crlSlaveEntities=[Node(333),   # [hl]
                                                                  Edge(14)],   # [hl]
                                                listMpcConnection=[MPC_CONNECTION(iDof=1),  # [hl]
                                                                   MPC_CONNECTION(iDof=2),   # [hl]
                                                                   MPC_CONNECTION(iDof=4),   # [hl]
                                                                   MPC_CONNECTION(),   # [hl]
                                                                   MPC_CONNECTION(),  # [hl]
                                                                   MPC_CONNECTION()],   # [hl]
                                                bUpdateDispCS=1)  # [hl]
    
JPT.Debugger(created_mpc)
