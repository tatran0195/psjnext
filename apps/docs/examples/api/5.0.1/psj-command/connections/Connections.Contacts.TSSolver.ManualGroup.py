# Title:   Connections.Contacts.TSSolver.ManualGroup()
# Desc:    Define contact settings between specified groups for TS SunShine solver. Create a group with master and slave surfaces beforehand to define the contact in the contact settings
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/connections/Connections.Contacts.TSSolver.ManualGroup
# ---
Geometry.Part.Cube(iPartColor=12537679)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=6250449)

Tools.Group.CreateGroup(strGroupName="ContactAbaqus_1_Manual_Face_M", 
                        crlTargets=[Face(49)])
Tools.Group.CreateGroup(strGroupName="ContactAbaqus_1_Manual_Face_S", 
                        crlTargets=[Face(24)])

created_contact = Connections.Contacts.TSSolver.ManualGroup(strName="ContactTSSolver_2",   # [hl]
                                                            tssolverContact=TSSOLVER_CONTACT(iIshellelemfaceSlave=0,   # [hl]
                                                                                             iIshellelemfaceMaster=0),   # [hl]
                                                            crplTarget=[CursorPair(Group(1),   # [hl]
                                                                                   Group(2))],   # [hl]
                                                            iMethod=1)  # [hl]

JPT.Debugger(created_contact)
