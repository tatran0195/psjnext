# Title:   JPT.PreviewBCForceGeneral()
# Desc:    Show preview result of applying general force on target
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_PreviewBCForceGeneral
# ---
# Clear Preview
JPT.ClearPreview()

# Prepare model
Geometry.Part.Cube()

# Preview
color = JPT.ConvertRGBToJPTColor(255,255,87) #yellow
selFace = JPT.GetEntitiesByID(JPT.DItemType.FACE, 26)
JPT.PreviewBCForceGeneral(selFace,[0.0,10.0,10.0],[0.0,0.0,0.0],0,color,0.8)  # [hl]
JPT.ViewFitToModel()
