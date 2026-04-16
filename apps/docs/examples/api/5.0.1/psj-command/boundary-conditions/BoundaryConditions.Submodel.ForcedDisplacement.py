# Title:   BoundaryConditions.Submodel.ForcedDisplacement()
# Desc:    Create a forced displacement boundary condition for node-based submodeling
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/boundary-conditions/BoundaryConditions.Submodel.ForcedDisplacement
# ---
Geometry.Part.Cube()
created_bcs = BoundaryConditions.Submodel.ForcedDisplacement(crlTargets=[Face(26)])  # [hl]
JPT.Debugger(created_bcs)
