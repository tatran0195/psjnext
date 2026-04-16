# Title:   Geometry.DeleteEntity.Part()
# Desc:    Delete part entities
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/geometry/Geometry.DeleteEntity.Part
# ---
cube = Geometry.Part.Cube()

flag = Geometry.DeleteEntity.Part(crlParts=[cube])  # [hl]

JPT.Debugger(flag)
