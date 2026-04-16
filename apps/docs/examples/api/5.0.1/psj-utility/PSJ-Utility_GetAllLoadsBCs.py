# Title:   JPT.GetAllLoadsBCs()
# Desc:    Get all the information of all existing loads and boundary conditions under DItem format
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_GetAllLoadsBCs
# ---
# Prepare model
Geometry.Part.Cube(iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.012, 0.0, 0.0], strName="Cube_2", iPartColor=13259210)
Geometry.Part.Cube(dlOrigin=[0.024, 0.0, 0.0], strName="Cube_3", iPartColor=7697908)
BoundaryConditions.FixedConstraint(crlTargets=[Face(76)])
BoundaryConditions.Pressure.General(crlTargets=[Face(52)])
JPT.ViewFitToModel()

# Get the information of all existing loads and boundary conditions
listDItemLoadBCs = JPT.GetAllLoadsBCs()  # [hl]
JPT.Debugger(listDItemLoadBCs)

# Print all the related information of each existing load/boundary condition in list
for lbc in listDItemLoadBCs:
    JPT.Debugger(lbc)
