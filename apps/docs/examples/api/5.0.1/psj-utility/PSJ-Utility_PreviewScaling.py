# Title:   JPT.PreviewScaling()
# Desc:    Show preview result of body scaling
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_PreviewScaling
# ---
# Clear Preview
JPT.ClearPreview()

# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.0, 0.01, 0.0], strName="Cube_2", iPartColor=13259210)

# Preview
color = JPT.ConvertRGBToJPTColor(255,255,87) #yellow
parts = JPT.GetAllParts()
JPT.PreviewScaling(parts,[2.1,1.1,1.1],[0,0,0],color,0.2)  # [hl]
JPT.ViewFitToModel()
