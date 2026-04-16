# Title:   JPT.PreviewBCPressureGeneral()
# Desc:    Show preview result of applying general pressure on target
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_PreviewBCPressureGeneral
# ---
# Clear Preview
JPT.ClearPreview()

# Prepare model
Geometry.Part.Cube()

# Preview
color = JPT.ConvertRGBToJPTColor(255,255,87) #yellow
selFace = JPT.GetEntitiesByID(JPT.DItemType.FACE, 26)
JPT.PreviewBCPressureGeneral(selFace,1,color,0.8)  # [hl]
JPT.ViewFitToModel()
