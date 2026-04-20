# Title:   Connections.MassElements()
# Desc:    Connection new mass
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/connections/Connections.MassElements
# ---
Geometry.Part.Cube()
Connections.MassElements(strName="Mass1", crlTargets=[Node(5)], dMass=0.01, iDof=1, bDesigner=True,   # [hl:start]
                        crCoordinate=None, dOffset0=0.0, dOffset1=0.0, dOffset2=0.0, dInertia0=0.0, 
                        dInertia1=0.0, dInertia2=0.0, dInertia3=0.0, dInertia4=0.0, dInertia5=0.0, 
                        crEdit=None, bUpdateDispCS=True)  # [hl:end]
