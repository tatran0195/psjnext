# Title:   Geometry.DeleteEntity.Edge()
# Desc:    Delete the selected edge entities
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/geometry/Geometry.DeleteEntity.Edge
# ---
Geometry.Part.Cube()

flag = Geometry.DeleteEntity.Edge(crlEdges=[Edge(15, 18, 19)])  # [hl]

JPT.Debugger(flag)
