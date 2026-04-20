# Title:   JPT.GetAllByTypeID()
# Desc:    Get all the information of all entities by inputting DItemType
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetAllByTypeID
# ---
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Select all parts and store their information to a list of DItem
listDItemParts = JPT.GetAllByTypeID(JPT.DItemType.BODY) # ID = 3  # [hl]
JPT.Debugger(listDItemParts)
