# Title:   Connections.RigidElements.RBE2.OneToOneNodesWithTolerance()
# Desc:    Create one-to-one (master:slave) RBE2 (rigid elements) with nodes tolerance
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/connections/Connections.RigidElements.RBE2.OneToOneNodesWithTolerance
# ---
# Prepare models
Geometry.Part.Cube(iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.015, 0.0, 0.0], strName="Cube_2", iPartColor=7463537)

# Create the connections
rbe2_connection = Connections.RigidElements.RBE2.OneToOneNodesWithTolerance(crlTargets =[Node(493, 6, 496, 7)],   # [hl:start]
                                                                            strName="RBE2_1", 
                                                                            dTolerance=0.005, 
                                                                            iUlDOFs=7)  # [hl:end]
JPT.Debugger(rbe2_connection)
