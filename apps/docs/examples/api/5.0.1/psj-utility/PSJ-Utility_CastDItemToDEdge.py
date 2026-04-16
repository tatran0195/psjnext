# Title:   JPT.CastDItemToDEdge()
# Desc:    Convert DItem object to DEdge object
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_CastDItemToDEdge
# ---
# Prepare model
Geometry.Part.Cube()
JPT.ViewFitToModel()

# Get Edge object as DItem object from the created list of DItem objects
listDItemEdges = JPT.GetAllByTypeID(JPT.DItemType.EDGE)
dItemEdge = listDItemEdges[0]
JPT.Debugger(dItemEdge)

# Convert from the above DItem object to DEdge object
dEdge = JPT.CastDItemToDEdge(dItemEdge)  # [hl]
JPT.Debugger(dEdge)
