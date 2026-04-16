# Title:   Connections.RigidElements.RBE3.ToCenter()
# Desc:    Create one to many (Slave:Master) RBE3 (Interpolation constraining Element)
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/connections/Connections.RigidElements.RBE3.ToCenter
# ---
Geometry.Part.Cylinder(bHollow=True, dTopInnerRadius=0.005, dBottomInnerRadius=0.005, iPartColor=15658599)

Connections.RigidElements.RBE3.ToCenter(crlMasterTargets=[Edge(1)],   # [hl:start]
                                    listRbe3TermConnection=[(0, 63, 1), (1, 7, 1)], 
                                    strName="RBE3_1", 
                                    dlVirtualNodePos=[0, 0.01, 0])  # [hl:end]
