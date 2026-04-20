# Title:   Connections.RigidElements.RBE2.ToCenter()
# Desc:    Create one-to-many (master:slave) RBE2 (rigid element)
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/connections/Connections.RigidElements.RBE2.ToCenter
# ---
# Prepare models
Geometry.Part.Cube(iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_2", iPartColor=7463537)

# Create the connections
rbe2_connection = Connections.RigidElements.RBE2.ToCenter(crlSlaveTargets=[Node(496, 493, 489, 492, 7, 6, 2, 3)],   # [hl]
                                         iUlDOFs=45, dlVirtualNodePos=[0.015, 0.005, 0.005], iEnableCornerOnly=1)  # [hl]
JPT.Debugger(rbe2_connection)
