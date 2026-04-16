# Title:   Connections.RigidElements.RBE3.OneToMany()
# Desc:    Create one to many (Slave:Master) RBE3 (Interpolation constraining Element)
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/connections/Connections.RigidElements.RBE3.OneToMany
# ---
# Prepare model
Geometry.Part.Cube(iPartColor=7697908)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_2", iPartColor=14903267)

# Create the connection
Connections.RigidElements.RBE3.OneToMany(crlMasterTargets=[Node(589, 496, 493)],   # [hl:start]
                                        crlSlaveTargets=[Node(84)], 
                                        listRbe3TermConnection=[(0, 63, 1), (1, 7, 3)], 
                                        strName="RBE3_1")  # [hl:end]
