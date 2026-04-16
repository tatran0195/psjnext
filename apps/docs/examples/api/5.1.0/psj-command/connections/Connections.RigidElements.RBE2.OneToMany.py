# Title:   Connections.RigidElements.RBE2.OneToMany()
# Desc:    Create one-to-many (master:slave) RBE2 (rigid elements)
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/connections/Connections.RigidElements.RBE2.OneToMany
# ---
# Prepare models
Geometry.Part.Cube(iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_2", iPartColor=7463537)

# Create the connections
rbe2_connection = Connections.RigidElements.RBE2.OneToMany(crlMasterTargets=[Node(496)],   # [hl]
        crlSlaveTargets=[Face(24)], strName="RBE2_2", iUlDOFs=7, iEnableCornerOnly=1)  # [hl]
JPT.Debugger(rbe2_connection)
