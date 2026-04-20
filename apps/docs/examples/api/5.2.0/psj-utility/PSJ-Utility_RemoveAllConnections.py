# Title:   JPT.RemoveAllConnections()
# Desc:    Remove all the existing connections
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_RemoveAllConnections
# ---
# Prepare model
Geometry.Part.Cube(iPartColor=7011837)
Connections.RigidElements.RBE2.OneToMany(
    crlMasterTargets=[Node(446)], crlSlaveTargets=[Node(467)]
)
Connections.RigidElements.RBE2.OneToMany(
    crlMasterTargets=[Node(443)], crlSlaveTargets=[Node(470)], strName="RBE2_2"
)
Connections.RigidElements.RBE3.OneToMany(
    crlMasterTargets=[Node(450)],
    crlSlaveTargets=[Node(455)],
    listRbe3TermConnection=[(0, 63, 1), (1, 7, 1)],
    strName="RBE3_1",
)
Connections.RigidElements.RBE3.OneToMany(
    crlMasterTargets=[Node(463)],
    crlSlaveTargets=[Node(458)],
    listRbe3TermConnection=[(0, 63, 1), (1, 7, 1)],
    strName="RBE3_2",
)
Connections.MPC.General.NodesToNodes(
    crlMasterNodes=[Node(436)],
    crlSlaveNodes=[Node(476)],
    listMpcConnection=[
        MPC_CONNECTION(iDof=1),
        MPC_CONNECTION(iDof=2),
        MPC_CONNECTION(iDof=4),
        MPC_CONNECTION(),
        MPC_CONNECTION(),
        MPC_CONNECTION(),
    ],
    bUpdateDispCS=1,
)
Connections.MPC.General.NodesToNodes(
    strName="MPC_2",
    crlMasterNodes=[Node(437)],
    crlSlaveNodes=[Node(477)],
    listMpcConnection=[
        MPC_CONNECTION(iDof=1),
        MPC_CONNECTION(iDof=2),
        MPC_CONNECTION(iDof=4),
        MPC_CONNECTION(),
        MPC_CONNECTION(),
        MPC_CONNECTION(),
    ],
    bUpdateDispCS=1,
)

# Remove all created connections
JPT.RemoveAllConnections()  # [hl]
