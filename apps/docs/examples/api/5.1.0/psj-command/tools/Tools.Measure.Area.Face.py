# Title:   Tools.Measure.Area.Face()
# Desc:    Measure an area of a face or a total area of faces
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.Measure.Area.Face
# ---
Geometry.Part.Cube()

area = Tools.Measure.Area.Face(crlFaces=[Face(26)])  # [hl]

JPT.Debugger(area)
