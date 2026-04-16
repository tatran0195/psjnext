# Title:   Connections.Contacts.ADVC.FindContactPairs()
# Desc:    Find contact pairs.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/connections/Connections.Contacts.ADVC.FindContactPairs
# ---
Geometry.Part.Cube(
  iPartColor=6409934)
Geometry.Part.Cube(
  dlOrigin=[0.01, 0.0, 0.0], 
  strName="Cube_2", 
  iPartColor=7463537)
Geometry.Part.Cube(
  dlOrigin=[0.02, 0.0, 0.0], 
  strName="Cube_3", 
  iPartColor=7666683)

cont=Connections.Contacts.ADVC.FindContactPairs(  # [hl:start]
    crlParts=[Part(1, 2, 3)], 
    dFindTolerance=0.0002, 
    dTolForTIED=0.1)  # [hl:end]

for c in cont:
    c.stAdvcParam.dClearance=0.1234

Connections.Contacts.ADVC.ContactTable_Advc(cont)
