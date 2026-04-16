# Title:   JPT.PreviewTranslation()
# Desc:    Show preview result of body translation
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_PreviewTranslation
# ---
# Clear Preview
JPT.ClearPreview()

# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.0, 0.01, 0.0], strName="Cube_2", iPartColor=13259210)
Tools.Coordinates.ThreeNode(iOrder=-1, crlNodes=[Node(496, 578, 590)])

# Preview
color = JPT.ConvertRGBToJPTColor(255,255,87) #yellow
parts = JPT.GetAllParts()
coord = JPT.GetAllCoordinates()
JPT.PreviewTranslation(parts,[0.02,0.01,0.01],color,1,coord[0])  # [hl]
JPT.ViewFitToModel()
