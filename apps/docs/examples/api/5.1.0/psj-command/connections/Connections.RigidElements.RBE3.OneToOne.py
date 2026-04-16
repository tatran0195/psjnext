# Title:   Connections.RigidElements.RBE3.OneToOne()
# Desc:    Create one to one (Slave:Master) RBE3 (Interpolation constraining Element)
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/connections/Connections.RigidElements.RBE3.OneToOne
# ---
Geometry.Part.Cube(
    ilAxialNodes=[4, 4, 4], strName="Cube_2", iPartColor=14903267)

Geometry.Part.Cube(
    dlOrigin=[0.012, 0.0, 0.0], 
    ilAxialNodes=[4, 4, 4], 
    strName="Cube_3", 
    iPartColor=7829501)

Connections.RigidElements.RBE3.OneToOne(
    crlMasterTargets=[Node(61, 87, 88, 64, 57, 71, 72, 60)],   # [hl:start]
    crlSlaveTargets=[Node(6, 27, 28, 7, 2, 11, 12, 3)],
     listRbe3TermConnection=[(0, 63, 8), (1, 7, 8)],
     strName="RBE3_3")
