# Title:   Connections.Contacts.CheckPattern()
# Desc:    Check the mesh pattern on the selected faces. The matched/unmatched mesh pattern between selected entities will be shown based on the selected option
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/connections/Connections.Contacts.CheckPattern
# ---
Geometry.Part.Cube(iPartColor=12276667)

Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0],
                   strName="Cube_2",
                   iPartColor=14511581)

Connections.Contacts.NXNastran.ManualFace(crlFaceMasters=[Face(24)],
                                          crlFaceSlaves=[Face(49)],
                                          dSearchDist=10.0,
                                          dPenaltyFactor=1.0,
                                          iContactColor=16711680)

checking_status = Connections.Contacts.CheckPattern(crlParts=[Part(1, 2)])  # [hl]

JPT.Debugger(checking_status)
