# Title:   JPT.PreviewRotate()
# Desc:    Show preview result of body rotation
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_PreviewRotate
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
JPT.PreviewRotate(parts,[0,0,0],[0,1,0],45,color,0.8,coord[0])  # [hl]
JPT.ViewFitToModel()
