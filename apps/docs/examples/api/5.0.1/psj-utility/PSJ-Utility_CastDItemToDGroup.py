# Title:   JPT.CastDItemToDGroup()
# Desc:    Convert DItem object to DGroup object
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_CastDItemToDGroup
# ---
# Prepare model
Geometry.Part.Cube()
Tools.Group.CreateGroup(strGroupName="Group1", crlTargets=[Face(26)])
JPT.ViewFitToModel()

# Get Group object as DItem object from the created list of DItem objects
listDItemGroups = JPT.GetAllByTypeID(JPT.DItemType.GROUP)
dItemGroup = listDItemGroups[0]
JPT.Debugger(dItemGroup)

# Convert from the above DItem object to DGroup object
dGroup = JPT.CastDItemToDGroup(dItemGroup)  # [hl]
JPT.Debugger(dGroup)
