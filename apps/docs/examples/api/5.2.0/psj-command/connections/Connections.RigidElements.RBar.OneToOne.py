# Title:   Connections.RigidElements.RBar.OneToOne()
# Desc:    Create one-to-one (master:slave) RBar (rigid elements)
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/connections/Connections.RigidElements.RBar.OneToOne
# ---
# Prepare models
Geometry.Part.Cube(iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_2", iPartColor=7463537)

# Create the connections
rbar_connection = Connections.RigidElements.RBar.OneToOne(strName="RBar_1", crlMasterTargets=[Node(496)],   # [hl]
                                    crlSlaveTargets=[Node(7)], iUlDOFs=63, dTol=0.0, bUpdateDispCS=True)  # [hl]
JPT.Debugger(rbar_connection)
