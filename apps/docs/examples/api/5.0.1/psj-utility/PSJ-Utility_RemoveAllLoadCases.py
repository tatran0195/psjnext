# Title:   JPT.RemoveAllLoadCases()
# Desc:    Remove all the existing load cases
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_RemoveAllLoadCases
# ---
# Prepare model
Geometry.Part.Cube(iPartColor=13259210)
Geometry.Part.Cube(dlOrigin=[0.04, 0.0, 0.0], strName="Cube_2", iPartColor=7697908)
Geometry.Part.Cube(dlOrigin=[0.08, 0.0, 0.0], strName="Cube_3", iPartColor=7463537)
BoundaryConditions.FixedConstraint(crlTargets=[Face(78, 52)])
BoundaryConditions.FixedConstraint(strName="Constraint2", crlTargets=[Face(50)])
BoundaryConditions.FixedConstraint(strName="Constraint3", crlTargets=[Face(24)])
BoundaryConditions.FixedConstraint(strName="Constraint4", crlTargets=[Face(26)])
BoundaryConditions.Pressure.General(crlTargets=[Face(51)])
BoundaryConditions.Pressure.General(strName="Pressure2", crlTargets=[Face(77)])
BoundaryConditions.Pressure.General(strName="Pressure3", crlTargets=[Face(25)])
BoundaryConditions.Force.General("Force1",
                                 forceLBC=FORCE_LBC(vecForce=[1.0, DFLT_DBL, DFLT_DBL]),
                                 crlTargets=[Face(22)])
BoundaryConditions.Force.General("Force2",
                                 forceLBC=FORCE_LBC(vecForce=[1.0, DFLT_DBL, DFLT_DBL]),
                                 crlTargets=[Face(48)])
BoundaryConditions.Force.General("Force3",
                                 forceLBC=FORCE_LBC(vecForce=[1.0, DFLT_DBL, DFLT_DBL]),
                                 crlTargets=[Face(74)])
BoundaryConditions.LoadCase(crlTargets=[LbcConstraint(1, 2)],
                            iExportId=5, dlTargetFactor=[1.0, 1.0])
BoundaryConditions.LoadCase(strName="LoadCase2",
                            crlTargets=[LbcConstraint(1, 3)], iExportId=6,
                            dlTargetFactor=[1.0, 1.0])
BoundaryConditions.LoadCase(strName="LoadCase3",
                            crlTargets=[LbcConstraint(2, 3)], iExportId=7,
                            dlTargetFactor=[1.0, 1.0])

# Remove all the created load cases
JPT.RemoveAllLoadCases()  # [hl]
