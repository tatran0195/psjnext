# Title:   Connections.Contacts.MSCNastran.ManualFace()
# Desc:    Define contact settings between specified faces for the MSC Nastran solver
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/connections/Connections.Contacts.MSCNastran.ManualFace
# ---
Geometry.Part.Cube(iPartColor=15132254)
Geometry.Part.Cube(dlOrigin=[0.011, 0.0, 0.0],
                   strName="Cube_2",
                   iPartColor=6013120)
Geometry.Part.Cube(dlOrigin=[0.011, 0.01, 0.0],
                   strName="Cube_3",
                   iPartColor=5395146)
Tools.Group.CreateGroup(strGroupName="Group1",
                        crlTargets=[Face(73)])
Tools.Group.CreateGroup(strGroupName="Group2",
                        crlTargets=[Face(48)])
Assembly.RightClick.Rename(strNewName="Master",
                           crItem=Group(1))
Assembly.RightClick.Rename(strNewName="Slave",
                           crItem=Group(2))
Meshing.SolidMeshing(crlParts=[Part(1, 2, 3)],
                     bTet10=True,
                     dGradingFactor=1.05,
                     dStretchLimit=0.1,
                     iSpeedVsQual=1,
                     iRegion=1,
                     bSafeMode=False,
                     iParallel=12,
                     bInternalMeshOnly=False,
                     iPartColor=65280)

creating_status = Connections.Contacts.MSCNastran.ManualFace(crlMasterFaces=[Face(24)],  # [hl]
                                                             crlSlaveFaces=[Face(49)],  # [hl]
                                                             nastranContact=NASTRAN_CONTACT(dRROR=0.0005),  # [hl]
                                                             iColor=16711680)  # [hl]

JPT.Debugger(creating_status)
