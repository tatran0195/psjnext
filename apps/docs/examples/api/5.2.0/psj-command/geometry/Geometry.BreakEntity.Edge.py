# Title:   Geometry.BreakEntity.Edge()
# Desc:    Break an edge into separate units at the given points or specified angle
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/geometry/Geometry.BreakEntity.Edge
# ---
Geometry.Part.Cube(iPartColor=6215639)

edges = Geometry.BreakEntity.Edge(crlNodes=[Node(86, 83)])  # [hl]

JPT.Debugger(edges)
