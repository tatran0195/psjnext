# Title:   Connections.RigidElements.RigidBodyConstraint.NodesToBody()
# Desc:    Create Rigid Body Constraint (LS-DYNA)
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/connections/Connections.RigidElements.RigidBodyConstraint.NodesToBody
# ---
Geometry.Part.Cube()
Connections.RigidElements.RigidBodyConstraint.NodesToBody(  # [hl:start]
    strName="RBC_1", 
    iMethod=1, 
    crlMasters=[Part(1)], 
    crlSlaves=[Node(460)])  # [hl:end]
