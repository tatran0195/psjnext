# Title:   Geometry.DeleteEntity.Face()
# Desc:    Delete face entities
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/geometry/Geometry.DeleteEntity.Face
# ---
Geometry.Part.Cube()

flag = Geometry.DeleteEntity.Face(crlFaces=[Face(26)])  # [hl]

JPT.Debugger(flag)
