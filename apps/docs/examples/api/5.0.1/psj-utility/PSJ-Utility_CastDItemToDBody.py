# Title:   JPT.CastDItemToDBody()
# Desc:    Convert DItem object to DBody object
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_CastDItemToDBody
# ---
# Prepare model
Geometry.Part.Cube()
JPT.ViewFitToModel()

# Get Part object as DItem object from the created list of DItem objects
listDItemParts = JPT.GetAllByTypeID(JPT.DItemType.BODY)
dItemPart = listDItemParts[0]
JPT.Debugger(dItemPart)

# Convert from the above DItem object to DBody object
dBodyPart = JPT.CastDItemToDBody(dItemPart)  # [hl]
JPT.Debugger(dBodyPart)
