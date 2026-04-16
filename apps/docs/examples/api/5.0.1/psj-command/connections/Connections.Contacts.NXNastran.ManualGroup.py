# Title:   Connections.Contacts.NXNastran.ManualGroup()
# Desc:    Define contact settings between specified groups for the NX solver
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/connections/Connections.Contacts.NXNastran.ManualGroup
# ---
Geometry.Part.Cube(iPartColor=12537679)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=6250449)

Tools.Group.CreateGroup(strGroupName="ContactAbaqus_1_Manual_Face_M", 
                        crlTargets=[Face(49)])
Tools.Group.CreateGroup(strGroupName="ContactAbaqus_1_Manual_Face_S", 
                        crlTargets=[Face(24)])

created_contact = Connections.Contacts.NXNastran.ManualGroup(crFaceMaster=Group(1),   # [hl]
                                                             crFaceSlave=Group(2),   # [hl]
                                                             dSearchDist=10.0,   # [hl]
                                                             dPenatlyFactor=1.0,   # [hl]
                                                             iColor=16711680,   # [hl]
                                                             iMethod=1)  # [hl]

JPT.Debugger(created_contact)
