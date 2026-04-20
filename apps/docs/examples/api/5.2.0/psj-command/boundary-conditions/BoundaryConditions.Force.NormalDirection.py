# Title:   BoundaryConditions.Force.NormalDirection()
# Desc:    Create a force in the normal direction applies on selected Face, Edge, Node/MidNode, Normal(Element). User inputs the force value, and it will apply the force to the selected items
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/boundary-conditions/BoundaryConditions.Force.NormalDirection
# ---
Geometry.Part.Cube()

created_bcs = BoundaryConditions.Force.NormalDirection(strName="ForceNormal1",   # [hl]
                                                       dForce=1,   # [hl]
                                                       crElemForNormal=Elem(1008),  # [hl]
                                                       crlTargets=[Face(26)])  # [hl]

JPT.Debugger(created_bcs)
