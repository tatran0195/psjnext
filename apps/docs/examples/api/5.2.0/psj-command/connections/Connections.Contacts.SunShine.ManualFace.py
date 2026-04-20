# Title:   Connections.Contacts.SunShine.ManualFace()
# Desc:    Define contact settings between specified faces for the TechnoStar Sunshine solver
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/connections/Connections.Contacts.SunShine.ManualFace
# ---
Geometry.Part.Cube()

Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=4803000)

creating_status = Connections.Contacts.SunShine.ManualFace(crlMasterFaces=[Face(24)],  # [hl]
                                                           crlSlaveFaces=[Face(49)],  # [hl]
                                                           strName="ContactSunShine_1",   # [hl]
                                                           sunshineContact=SUNSHINE_CONTACT(dERROR=0.001,   # [hl]
                                                                                            dFRIC=0.5,  # [hl]
                                                                                            dSLIDE=DFLT_DBL,   # [hl]
                                                                                            iICOORD=DFLT_INT,   # [hl]
                                                                                            dSFACT=DFLT_DBL,   # [hl]
                                                                                            dSFACTT=0.5,   # [hl]
                                                                                            dCDAMP=DFLT_DBL),  # [hl]
                                                           iContactColor=16711680)  # [hl]

JPT.Debugger(creating_status)
