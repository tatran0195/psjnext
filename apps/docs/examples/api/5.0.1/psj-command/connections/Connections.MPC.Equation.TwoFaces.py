# Title:   Connections.MPC.Equation.TwoFaces()
# Desc:    Create MPC between multiple points of two faces
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/connections/Connections.MPC.Equation.TwoFaces
# ---
Geometry.Part.Cube(iPartColor=7666683)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=12867524)

created_mpc = Connections.MPC.Equation.TwoFaces(strName="MPC_1",   # [hl]
                                                crMasterFace=Face(49),   # [hl]
                                                crSlaveFace=Face(24),  # [hl]
                                                listMpcConnection=[MPC_CONNECTION(dCoef=1.0,   # [hl]
                                                                                  iDof=1),   # [hl]
                                                                   MPC_CONNECTION(dCoef=-1.0,   # [hl]
                                                                                  iDof=1)],   # [hl]
                                                bUpdateDispCS=1)  # [hl]

JPT.Debugger(created_mpc)
