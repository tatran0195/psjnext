# Title:   Connections.Contacts.TSSS.ContactTable()
# Desc:    Create contacts for TS Sunshine solver by using table
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/connections/Connections.Contacts.TSSS.ContactTable
# ---
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.0, 0.01, 0.0], 
                   strName="Cube_3", 
                   iPartColor=6417130)
Geometry.Part.Cube(dlOrigin=[0.01, 0.01, 0.0], 
                   strName="Cube_4", 
                   iPartColor=6053060)

Tools.Group.CreateGroup(strGroupName="Cube_3(73)-G0002", 
                        crlTargets=[Face(73)])
Tools.Group.CreateGroup(strGroupName="Cube_1(22)-G0001", 
                        crlTargets=[Face(22)])

created_contact_1 = Connections.Contacts.TSSS.ContactTable(strName="C0001_Cube_3-G0002_Cube_1-G0001",   # [hl]
                                                           sunshineContact=SUNSHINE_CONTACT(iType=1,   # [hl]
                                                                                            dERROR=0.001,   # [hl]
                                                                                            dFRIC=DFLT_DBL,   # [hl]
                                                                                            dSLIDE=DFLT_DBL,   # [hl]
                                                                                            iICOORD=DFLT_INT,   # [hl]
                                                                                            dSFACT=DFLT_DBL,   # [hl]
                                                                                            dSFACTT=0.5,   # [hl]
                                                                                            dCDAMP=DFLT_DBL,   # [hl]
                                                                                            iIshellelemfaceSlave=1,   # [hl]
                                                                                            iIshellelemfaceMaster=1),   # [hl]
                                                           crplTarget=[CursorPair(Group(1),   # [hl]
                                                                                  Group(2))],   # [hl]
                                                           iColor=65280)  # [hl]

Tools.Group.CreateGroup(strGroupName="Cube_4(99)-G0004", 
                        crlTargets=[Face(99)])
Tools.Group.CreateGroup(strGroupName="Cube_2(48)-G0003", 
                        crlTargets=[Face(48)])

created_contact_2 = Connections.Contacts.TSSS.ContactTable(strName="C0002_Cube_4-G0004_Cube_2-G0003",   # [hl]
                                                           sunshineContact=SUNSHINE_CONTACT(iType=1,   # [hl]
                                                                                            dERROR=0.001,   # [hl]
                                                                                            dFRIC=DFLT_DBL,   # [hl]
                                                                                            dSLIDE=DFLT_DBL,   # [hl]
                                                                                            iICOORD=DFLT_INT,   # [hl]
                                                                                            dSFACT=DFLT_DBL,   # [hl]
                                                                                            dSFACTT=0.5,   # [hl]
                                                                                            dCDAMP=DFLT_DBL,   # [hl]
                                                                                            iIshellelemfaceSlave=1,   # [hl]
                                                                                            iIshellelemfaceMaster=1),   # [hl]
                                                           crplTarget=[CursorPair(Group(3),   # [hl]
                                                                                  Group(4))],   # [hl]
                                                           iColor=65280)  # [hl]

Tools.Group.CreateGroup(strGroupName="Cube_2(49)-G0006", 
                        crlTargets=[Face(49)])
Tools.Group.CreateGroup(strGroupName="Cube_1(24)-G0005", 
                        crlTargets=[Face(24)])

created_contact_3 = Connections.Contacts.TSSS.ContactTable(strName="C0003_Cube_2-G0006_Cube_1-G0005",   # [hl]
                                                           sunshineContact=SUNSHINE_CONTACT(iType=1,   # [hl]
                                                                                            dERROR=0.001,   # [hl]
                                                                                            dFRIC=DFLT_DBL,   # [hl]
                                                                                            dSLIDE=DFLT_DBL,   # [hl]
                                                                                            iICOORD=DFLT_INT,  # [hl]
                                                                                            dSFACT=DFLT_DBL,   # [hl]
                                                                                            dSFACTT=0.5,   # [hl]
                                                                                            dCDAMP=DFLT_DBL,   # [hl]
                                                                                            iIshellelemfaceSlave=1,   # [hl]
                                                                                            iIshellelemfaceMaster=1),   # [hl]
                                                           crplTarget=[CursorPair(Group(5),   # [hl]
                                                                                  Group(6))],   # [hl]
                                                           iColor=65280)  # [hl]

Tools.Group.CreateGroup(strGroupName="Cube_3(76)-G0007", 
                        crlTargets=[Face(76)])
Tools.Group.CreateGroup(strGroupName="Cube_4(101)-G0008", 
                        crlTargets=[Face(101)])

created_contact_4 = Connections.Contacts.TSSS.ContactTable(strName="C0004_Cube_3-G0007_Cube_4-G0008",   # [hl]
                                                           sunshineContact=SUNSHINE_CONTACT(iType=1,   # [hl]
                                                                                            dERROR=0.001,   # [hl]
                                                                                            dFRIC=DFLT_DBL,   # [hl]
                                                                                            dSLIDE=DFLT_DBL,   # [hl]
                                                                                            iICOORD=DFLT_INT,   # [hl]
                                                                                            dSFACT=DFLT_DBL,   # [hl]
                                                                                            dSFACTT=0.5,   # [hl]
                                                                                            dCDAMP=DFLT_DBL,   # [hl]
                                                                                            iIshellelemfaceSlave=1,   # [hl]
                                                                                            iIshellelemfaceMaster=1),   # [hl]
                                                           crplTarget=[CursorPair(Group(7),   # [hl]
                                                                                  Group(8))],   # [hl]
                                                           iColor=65280)  # [hl]

Tools.Group.CreateGroup(strGroupName="Cube_4(99)-G0010", 
                        crlTargets=[Face(99, 101)])
Tools.Group.CreateGroup(strGroupName="Cube_1(22)-G0009", 
                        crlTargets=[Face(22, 24)])

created_contact_5 = Connections.Contacts.TSSS.ContactTable(strName="C0005_Cube_4-G0010_Cube_1-G0009",   # [hl]
                                                           sunshineContact=SUNSHINE_CONTACT(iType=1,   # [hl]
                                                                                            dERROR=0.001,   # [hl]
                                                                                            dFRIC=DFLT_DBL,   # [hl]
                                                                                            dSLIDE=DFLT_DBL,   # [hl]
                                                                                            iICOORD=DFLT_INT,   # [hl]
                                                                                            dSFACT=DFLT_DBL,   # [hl]
                                                                                            dSFACTT=0.5,   # [hl]
                                                                                            dCDAMP=DFLT_DBL,   # [hl]
                                                                                            iIshellelemfaceSlave=1,   # [hl]
                                                                                            iIshellelemfaceMaster=1),   # [hl]
                                                           crplTarget=[CursorPair(Group(9),   # [hl]
                                                                                  Group(10))],   # [hl]
                                                           iColor=65280)  # [hl]

Tools.Group.CreateGroup(strGroupName="Cube_3(73)-G0012", 
                        crlTargets=[Face(73, 76)])
Tools.Group.CreateGroup(strGroupName="Cube_2(48)-G0011", 
                        crlTargets=[Face(48, 49)])

created_contact_6 = Connections.Contacts.TSSS.ContactTable(strName="C0006_Cube_3-G0012_Cube_2-G0011",   # [hl]
                                                           sunshineContact=SUNSHINE_CONTACT(iType=1,   # [hl]
                                                                                            dERROR=0.001,   # [hl]
                                                                                            dFRIC=DFLT_DBL,   # [hl]
                                                                                            dSLIDE=DFLT_DBL,   # [hl]
                                                                                            iICOORD=DFLT_INT,   # [hl]
                                                                                            dSFACT=DFLT_DBL,   # [hl]
                                                                                            dSFACTT=0.5,   # [hl]
                                                                                            dCDAMP=DFLT_DBL,   # [hl]
                                                                                            iIshellelemfaceSlave=1,   # [hl]
                                                                                            iIshellelemfaceMaster=1),   # [hl]
                                                           crplTarget=[CursorPair(Group(11),   # [hl]
                                                                                  Group(12))],   # [hl]
                                                           iColor=65280)  # [hl]

JPT.Debugger(created_contact_1)
JPT.Debugger(created_contact_2)
JPT.Debugger(created_contact_3)
JPT.Debugger(created_contact_4)
JPT.Debugger(created_contact_5)
JPT.Debugger(created_contact_6)
