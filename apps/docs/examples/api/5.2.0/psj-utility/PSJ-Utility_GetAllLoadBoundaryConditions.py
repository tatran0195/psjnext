# Title:   JPT.GetAllLoadBoundaryConditions()
# Desc:    Get all the information of all existing loads and boundary conditions
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetAllLoadBoundaryConditions
# ---
# Prepare model
Geometry.Part.Cube(iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.012, 0.0, 0.0], strName="Cube_2", iPartColor=13259210)
Geometry.Part.Cube(dlOrigin=[0.024, 0.0, 0.0], strName="Cube_3", iPartColor=7697908)
BoundaryConditions.FixedConstraint(crlTargets=[Face(76)])
BoundaryConditions.Pressure.General(crlTargets=[Face(52)])
JPT.ViewFitToModel()

# Get the information of all existing loads and boundary conditions
listDLoadBCs = JPT.GetAllLoadBoundaryConditions()  # [hl]
JPT.Debugger(listDLoadBCs)

# Print all the related information of each existing load/boundary condition in list
for lbc in listDLoadBCs:
    JPT.Debugger(lbc)
