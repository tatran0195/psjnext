# Title:   Connections.RigidElements.RigidBodyConstraint.Nodes()
# Desc:    Create Rigid Body Constraint (LS-DYNA)
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/connections/Connections.RigidElements.RigidBodyConstraint.Nodes
# ---
Geometry.Part.Cube()
Connections.RigidElements.RigidBodyConstraint.Nodes(  # [hl:start]
    strName="RBC_1", 
    iMethod=3, 
    crlMasters=[Edge(15)])
