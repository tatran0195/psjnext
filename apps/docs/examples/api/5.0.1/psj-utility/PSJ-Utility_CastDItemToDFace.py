# Title:   JPT.CastDItemToDFace()
# Desc:    Convert DItem object to DFace object
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_CastDItemToDFace
# ---
# Prepare model
Geometry.Part.Cube()
JPT.ViewFitToModel()

# Get Face object as DItem object from the created list of DItem objects
listDItemFaces = JPT.GetAllByTypeID(JPT.DItemType.FACE)
dItemFace = listDItemFaces[0]
JPT.Debugger(dItemFace)

# Convert from the above DItem object to DFace object
dFace = JPT.CastDItemToDFace(dItemFace)  # [hl]
JPT.Debugger(dFace)
