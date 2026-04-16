# Title:   Connections.Contacts.TSSolver.Auto()
# Desc:    Search and creat contact between the existing parts automatically based on the specified conditions
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/connections/Connections.Contacts.TSSolver.Auto
# ---
Geometry.Part.Cube(iPartColor=12537679)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=6250449)

created_contact = Connections.Contacts.TSSolver.Auto(strlNames=["C1_Cube_1(24)_Cube_2(49)"],   # [hl]
                                                     crllMasterFaceTargets=[[Face(24)]],   # [hl]
                                                     crllSlaveFaceTargets=[[Face(49)]],  # [hl]
                                                     crlEdit=[None],  # [hl]
                                                     crlMasterGroups=[None],   # [hl]
                                                     crlSlaveGroups=[None])  # [hl]

JPT.Debugger(created_contact)
