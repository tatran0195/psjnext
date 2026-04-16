# Title:   JPT.PreviewMirror()
# Desc:    Show preview result of body mirror
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_PreviewMirror
# ---
# Clear Preview
JPT.ClearPreview()

# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=13259210)

# Preview
color = JPT.ConvertRGBToJPTColor(255,255,87) #yellow
parts = JPT.GetAllParts()
JPT.PreviewMirror(parts,[[0.0055,0.01,0.0055],[0.005,0.01,0.0044],[0.0044,0.01,0.0044]],0,color,0.8)  # [hl]
JPT.ViewFitToModel()
