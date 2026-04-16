# Title:   Connections.Contacts.NXNastran.ManualFace()
# Desc:    Define contact settings between specified faces for the NX Nastran solver
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/connections/Connections.Contacts.NXNastran.ManualFace
# ---
Geometry.Part.Cube(iPartColor=4962231)

Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0],
                   strName="Cube_2", 
                   iPartColor=4803000)

creating_status = Connections.Contacts.NXNastran.ManualFace(crlFaceMasters=[Face(24)],   # [hl]
                                                            crlFaceSlaves=[Face(49)],  # [hl]
                                                            dSearchDist=10.0,   # [hl]
                                                            dPenaltyFactor=1.0,   # [hl]
                                                            iContactColor=16711680)  # [hl]

JPT.Debugger(creating_status)
