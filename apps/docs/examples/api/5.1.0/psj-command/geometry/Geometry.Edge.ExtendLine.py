# Title:   Geometry.Edge.ExtendLine()
# Desc:    Extend the specified edges to the specified boundary
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/geometry/Geometry.Edge.ExtendLine
# ---
Geometry.Part.Cube(iPartColor=6215639)

Geometry.Edge.ElementEdges(crplElemEdges=[CursorPair(Node(453), Node(461))])

extended_edges = Geometry.Edge.ExtendLine(crlEdges=[Edge(27)], iEnd=1)  # [hl]

JPT.Debugger(extended_edges)
