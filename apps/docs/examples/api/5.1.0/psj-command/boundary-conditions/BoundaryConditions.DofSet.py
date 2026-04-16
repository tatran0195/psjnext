# Title:   BoundaryConditions.DofSet()
# Desc:    Create the degrees of freedom in the analysis set(ASET) in TS-Solver
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/boundary-conditions/BoundaryConditions.DofSet
# ---
Geometry.Part.Cube()

created_lbc = BoundaryConditions.DofSet(crlTargets=[Face(26)],  # [hl]
                                        strName="DofSet1",  # [hl]
                                        iDwDof=7)  # [hl]

JPT.Debugger(created_lbc)
