# Title:   BoundaryConditions.FixedConstraint()
# Desc:    Create a fixed constraint on selected Face, Edge or Node. User inputs the degree of freedom of fixed constraint and it will return a fixed constraint on selected items
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/boundary-conditions/BoundaryConditions.FixedConstraint
# ---
Geometry.Part.Cube()
creating_status = BoundaryConditions.FixedConstraint(crlTargets=[Face(26)])  # [hl]
JPT.Debugger(creating_status)
