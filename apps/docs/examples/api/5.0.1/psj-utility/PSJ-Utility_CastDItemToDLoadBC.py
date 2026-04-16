# Title:   JPT.CastDItemToDLoadBC()
# Desc:    Convert DItem object to DLoadBC object to get the information of the selected coordinate system
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_CastDItemToDLoadBC
# ---
# Prepare simple sample
Geometry.Part.Cube(iPartColor=6409934)
BoundaryConditions.Pressure.General(crlTargets=[Face(26)])
JPT.ViewFitToModel()

# Get LBC object (Pressure) as DItem object from the created list of DItem objects
listDItemLoadBCs = JPT.GetAllByTypeID(JPT.DItemType.LBC_G_PRESSURE)
dItemLoadBC = listDItemLoadBCs[0]
JPT.Debugger(dItemLoadBC)

# Convert from the above DItem object to DLoadBC object
dLoadBC = JPT.CastDItemToDLoadBC(dItemLoadBC)  # [hl]
JPT.Debugger(dLoadBC)
