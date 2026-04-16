# Title:   Connections.Contacts.TSSS.ManualGroup()
# Desc:    Define contact settings between specified groups for TechnoStar SunShine solver
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/connections/Connections.Contacts.TSSS.ManualGroup
# ---
Geometry.Part.Cube()

Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=4803000)

Connections.Contacts.SunShine.ManualFace(crlMasterFaces=[Face(24)], crlSlaveFaces=[Face(49)],
    strName="ContactSunShine_1", sunshineContact=SUNSHINE_CONTACT(dERROR=0.001, dFRIC=0.5,
    dSLIDE=DFLT_DBL, iICOORD=DFLT_INT, dSFACT=DFLT_DBL, dSFACTT=0.5, dCDAMP=DFLT_DBL),
    iContactColor=16711680)

Connections.Contacts.TSSS.ManualGroup(strName="ContactSunShine_2", iColor=16711680,  # [hl:start]
    sunshineContact=SUNSHINE_CONTACT(dERROR=1e-06, dFRIC=0.5, dSLIDE=DFLT_DBL, iICOORD=DFLT_INT,
    dSFACT=DFLT_DBL, dSFACTT=0.5, dCDAMP=DFLT_DBL), crplTarget=[CursorPair(Group(1), Group(2))])  # [hl:end]
