# Title:   Geometry.FindFeature.Face()
# Desc:    Find and select the specific faces according to their characteristic
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/geometry/Geometry.FindFeature.Face
# ---
cube = Geometry.Part.Cube()
faces = Geometry.FindFeature.Face(crlParts=[cube])  # [hl]
JPT.Debugger(faces)
