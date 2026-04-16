# Title:   Geometry.DeleteEntity.Part()
# Desc:    Delete part entities
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/geometry/Geometry.DeleteEntity.Part
# ---
cube = Geometry.Part.Cube()

flag = Geometry.DeleteEntity.Part(crlParts=[cube])  # [hl]

JPT.Debugger(flag)
