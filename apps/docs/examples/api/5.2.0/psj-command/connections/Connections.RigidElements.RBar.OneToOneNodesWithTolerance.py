# Title:   Connections.RigidElements.RBar.OneToOneNodesWithTolerance()
# Desc:    Create one-to-one (master:slave) RBar (rigid elements) with nodes tolerance
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/connections/Connections.RigidElements.RBar.OneToOneNodesWithTolerance
# ---
# Prepare models
Geometry.Part.Cube(iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.015, 0.0, 0.0], strName="Cube_2", iPartColor=7463537)

# Create the connections
rbar_connection = Connections.RigidElements.RBar.OneToOneNodesWithTolerance(strName="RBar_1",   # [hl:start]
                                                                            crlTargets =[Node(493, 6, 496, 7)], 
                                                                            iUlDOFs=63, 
                                                                            dTol=0.005)  # [hl:end]
JPT.Debugger(rbar_connection)
