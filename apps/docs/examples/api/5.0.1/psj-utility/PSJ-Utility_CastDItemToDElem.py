# Title:   JPT.CastDItemToDElem()
# Desc:    Convert DItem object to DElem object
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_CastDItemToDElem
# ---
# Prepare model
Geometry.Part.Cube()
JPT.ViewFitToModel()

# Get Element object as DItem object from the created list of DItem objects
listDItemElems = JPT.GetAllByTypeID(JPT.DItemType.ELEM)
dItemElem = listDItemElems[0]
JPT.Debugger(dItemElem)

# Convert from the above DItem object to DElem object
dElem = JPT.CastDItemToDElem(dItemElem)  # [hl]
JPT.Debugger(dElem)
