# Title:   JPT.GetAllByTableTypeID()
# Desc:    Get all the information of all entities by inputting DTableType
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetAllByTableTypeID
# ---
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Select all parts and store their information to a list of DItem
listDTableParts = JPT.GetAllByTableTypeID(JPT.DTableType.DTABLE_BODY) # ID = 5  # [hl]
JPT.Debugger(listDTableParts)

