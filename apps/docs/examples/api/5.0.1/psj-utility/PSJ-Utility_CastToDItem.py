# Title:   JPT.CastToDItem()
# Desc:    Convert the selected object to DItem object
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_CastToDItem
# ---
# Prepare model
Geometry.Part.Cube()
JPT.ViewFitToModel()

# Get Part object as DBody object from the created list of DBody objects
listDBodyParts = JPT.GetAllParts()
dBodyPart = listDBodyParts[0]
JPT.Debugger(dBodyPart)

# Convert from the above DBody object to DItem object
dItemPart = JPT.CastToDItem(dBodyPart)  # [hl]
JPT.Debugger(dItemPart)
