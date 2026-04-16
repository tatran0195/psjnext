# Title:   Connections.MPC.General.FacesToFaces()
# Desc:    Create MPC by connecting selected faces together
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/connections/Connections.MPC.General.FacesToFaces
# ---
Geometry.Part.Cube(iPartColor=7666683)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=12867524)

created_mpc = Connections.MPC.General.FacesToFaces(strName="MPC_10",   # [hl]
                                                   crlMasterFaces=[Face(24)],  # [hl]
                                                   crlSlaveFaces=[Face(49)],   # [hl]
                                                   listMpcConnection=[MPC_CONNECTION(iDof=1),   # [hl]
                                                                      MPC_CONNECTION(iDof=2),  # [hl]
                                                                      MPC_CONNECTION(iDof=4),   # [hl]
                                                                      MPC_CONNECTION(),   # [hl]
                                                                      MPC_CONNECTION(),   # [hl]
                                                                      MPC_CONNECTION()],   # [hl]
                                                   bUpdateDispCS=1,   # [hl]
                                                   crMPCConnection=None)  # [hl]

JPT.Debugger(created_mpc)
