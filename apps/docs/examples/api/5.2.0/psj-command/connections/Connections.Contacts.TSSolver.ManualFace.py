# Title:   Connections.Contacts.TSSolver.ManualFace()
# Desc:    Define contact settings between specified faces for the TS solver
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/connections/Connections.Contacts.TSSolver.ManualFace
# ---
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.015, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=6409934)

Tools.Group.CreateGroup(strGroupName="ContactTSSolver_1_Manual_Face_M", 
                        crlTargets=[Face(49)])
Tools.Group.CreateGroup(strGroupName="ContactTSSolver_1_Manual_Face_S", 
                        crlTargets=[Face(24)])

created_contact = Connections.Contacts.TSSolver.ManualFace(tssolverContact=TSSOLVER_CONTACT(iIshellelemfaceSlave=0,   # [hl]
                                                                                            iIshellelemfaceMaster=0),   # [hl]
                                                           crplTarget=[CursorPair(Group(1),   # [hl]
                                                                                  Group(2))])  # [hl]

JPT.Debugger(created_contact)
