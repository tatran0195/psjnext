# Title:   Connections.RigidElements.RBE2.OneToOne()
# Desc:    Create one-to-one (master:slave) RBE2 (rigid element)
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/connections/Connections.RigidElements.RBE2.OneToOne
# ---
# Prepare models
Geometry.Part.Cube(iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_2", iPartColor=7463537)

# Create the connections
rbe2_connection = Connections.RigidElements.RBE2.OneToOne(crlMasterTargets=[Node(496)],   # [hl]
                                            crlSlaveTargets=[Node(7)], strName="RBE2_3")  # [hl]
JPT.Debugger(rbe2_connection)
