# Title:   JPT.PreviewBCForceNormal()
# Desc:    Show preview result of applying normal force on target
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_PreviewBCForceNormal
# ---
# Clear Preview
JPT.ClearPreview()

# Prepare model
Geometry.Part.Cube()

# Preview
color = JPT.ConvertRGBToJPTColor(255,255,87) #yellow
selFace = JPT.GetEntitiesByID(JPT.DItemType.FACE, 26)
normalElem = JPT.GetEntitiesByID(JPT.DItemType.ELEM, 1065)
normalElem = JPT.CastDItemToDElem(normalElem[0])
JPT.PreviewBCForceNormal(normalElem,selFace,0,color,0.8)  # [hl]
JPT.ViewFitToModel()
