# Title:   Connections.MPC.Equation.SemiAuto()
# Desc:    Creates the MPC between the nodes with a distance tolerance
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/connections/Connections.MPC.Equation.SemiAuto
# ---
Geometry.Part.Cube(iPartColor=7666683)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=12867524)

created_mpc = Connections.MPC.Equation.SemiAuto(crlMasterEntities=[Face(24)],   # [hl]
                                                crlSlaveEntities=[Face(49)],   # [hl]
                                                listMpcConnection=[MPC_CONNECTION(dCoef=20.0,   # [hl]
                                                                                  iDof=1),   # [hl]
                                                                   MPC_CONNECTION(dCoef=-20.0,   # [hl]
                                                                                  iDof=1)],   # [hl]
                                                dConstantValue=10.0,   # [hl]
                                                bUpdateDispCS=1)  # [hl]

JPT.Debugger(created_mpc)
