# Title:   Connections.BoltConnections.AutoBoltConnection()
# Desc:    Create bolt connection for all the detected bolt holes at one time
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/connections/Connections.BoltConnections.AutoBoltConnection
# ---
Geometry.Part.Cylinder(bHollow=True, 
  dTopInnerRadius=0.002, 
  dBottomInnerRadius=0.002, 
  iPartColor=6250447)
Geometry.Part.Cylinder(
  strName="Cylinder_2", 
  bHollow=True, 
  dlOrigin=[0.0, 0.01, 0.0], 
  dTopInnerRadius=0.002, 
  dBottomInnerRadius=0.002, 
  iPartColor=12537679)

Connections.BoltConnections.FindAutoBoltConnection(
  crMasterPart=Part(2), 
  crSlavePart=Part(1), 
  dMinCircleDiameter=0.00368, 
  dMaxCircleDiameter=0.0045)
ret = Connections.BoltConnections.AutoBoltConnection(
    strName="Bolt",   # [hl:start]
    listBoltHoles=[BOLT_HOLE_FACE(crlMasterFaces=[Face(15)], crlSlaveFaces=[Face(7)], 
    dlCenterPoint=[0, 0.01, 0], 
    dlMasterPoint=[0, 0.02, 0])], 
    crlMatingFaces=[Face(14, 5)])  # [hl:end]
print(ret)
