# Title:   BoundaryConditions.FixedConstraint()
# Desc:    Create a fixed constraint on selected Face, Edge or Node. User inputs the degree of freedom of fixed constraint and it will return a fixed constraint on selected items
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/boundary-conditions/BoundaryConditions.FixedConstraint
# ---
Geometry.Part.Cube()
creating_status = BoundaryConditions.FixedConstraint(crlTargets=[Face(26)])  # [hl]
JPT.Debugger(creating_status)
