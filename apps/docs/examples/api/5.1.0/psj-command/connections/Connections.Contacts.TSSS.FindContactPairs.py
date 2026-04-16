# Title:   Connections.Contacts.TSSS.FindContactPairs()
# Desc:    Find the contact pairs in model
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/connections/Connections.Contacts.TSSS.FindContactPairs
# ---
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_3", iPartColor=13259210)
result = Connections.Contacts.TSSS.FindContactPairs(crlParts=[Part(1, 2, 3)], iSearchArea=0)  # [hl]
JPT.Debugger(result)
