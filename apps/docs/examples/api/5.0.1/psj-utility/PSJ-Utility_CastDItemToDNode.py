# Title:   JPT.CastDItemToDNode()
# Desc:    Convert DItem object to DNode object
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_CastDItemToDNode
# ---
# Prepare model
Geometry.Part.Cube()
JPT.ViewFitToModel()

# Get LBC object (Pressure) as DItem object from the created list of DItem objects
listDItemNodes = JPT.GetAllByTypeID(JPT.DItemType.NODE)
dItemNode = listDItemNodes[0]
JPT.Debugger(dItemNode)

# Convert from the above DItem object to DNode object
dNode = JPT.CastDItemToDNode(dItemNode)  # [hl]
JPT.Debugger(dNode)
