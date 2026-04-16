# Title:   JPT.HidePreview()
# Desc:    Hide preview render on the main screen
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_HidePreview
# ---
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.0, 0.01, 0.0], strName="Cube_2", iPartColor=13259210)
JPT.ViewFitToModel()

#Preview:
color = JPT.ConvertRGBToJPTColor(255,255,87) #yellow
parts = JPT.GetAllParts()
JPT.PreviewScaling(parts,[2,1.1,1.1],[0,0,0],color,0.2)

#Hide Preview:
JPT.HidePreview()  # [hl]
