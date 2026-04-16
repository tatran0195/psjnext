# Title:   Connections.Contacts.MSCNastran.ManualGroup()
# Desc:    Define contact settings between specified groups for MSC Nastran solver. Create a group with master and slave surfaces beforehand to define the contact in the contact settings
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/connections/Connections.Contacts.MSCNastran.ManualGroup
# ---
Geometry.Part.Cube(iPartColor=12537679)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=6250449)

Tools.Group.CreateGroup(strGroupName="ContactAbaqus_1_Manual_Face_M", 
                        crlTargets=[Face(49)])
Tools.Group.CreateGroup(strGroupName="ContactAbaqus_1_Manual_Face_S", 
                        crlTargets=[Face(24)])

created_contact = Connections.Contacts.MSCNastran.ManualGroup(strName="ContactMSCNastran_1",   # [hl]
                                                              nastranContact=NASTRAN_CONTACT(dRROR=0.0005),   # [hl]
                                                              crplTarget=[CursorPair(Group(1),   # [hl]
                                                                                     Group(2))],   # [hl]
                                                              iColor=16711680)  # [hl]

JPT.Debugger(created_contact)
