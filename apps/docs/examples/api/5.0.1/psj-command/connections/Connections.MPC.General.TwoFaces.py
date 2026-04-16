# Title:   Connections.MPC.General.TwoFaces()
# Desc:    Create MPC between two faces
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/connections/Connections.MPC.General.TwoFaces
# ---
Geometry.Part.Cube(iPartColor=7666683)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=12867524)

created_mpc = Connections.MPC.General.TwoFaces(strName="MPC_12",   # [hl]
                                               crMasterFace=Face(49),  # [hl]
                                               crSlaveFace=Face(24),   # [hl]
                                               listMpcConnection=[MPC_CONNECTION(iDof=1),   # [hl]
                                                                  MPC_CONNECTION(iDof=2),  # [hl]
                                                                  MPC_CONNECTION(iDof=4),   # [hl]
                                                                  MPC_CONNECTION(),   # [hl]
                                                                  MPC_CONNECTION(),  # [hl]
                                                                  MPC_CONNECTION()],   # [hl]
                                               bUpdateDispCS=1)  # [hl]

JPT.Debugger(created_mpc)
