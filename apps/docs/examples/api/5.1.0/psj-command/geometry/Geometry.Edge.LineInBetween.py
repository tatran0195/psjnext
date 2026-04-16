# Title:   Geometry.Edge.LineInBetween()
# Desc:    Create edges between two selected edges
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/geometry/Geometry.Edge.LineInBetween
# ---
Geometry.Part.Cube(iPartColor=6484066)

between_lines = Geometry.Edge.LineInBetween(crlEdges=[Edge(20, 18)], crlFaces=[Face(26)], numLine=2)  # [hl]

JPT.Debugger(between_lines)
