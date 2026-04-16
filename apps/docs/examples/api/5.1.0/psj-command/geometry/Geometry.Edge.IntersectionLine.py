# Title:   Geometry.Edge.IntersectionLine()
# Desc:    Create edge at the intersection line of the two selected faces
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/geometry/Geometry.Edge.IntersectionLine
# ---
Geometry.Part.Cube()
Geometry.Face.Edges(crlEdges=[Edge(20, 10)], bCreatePart=True)
Geometry.Face.Edges(crlEdges=[Edge(18, 12)], bCreatePart=True)
Geometry.DeleteEntity.Part(crlParts=[Part(1)])

intersection_line = Geometry.Edge.IntersectionLine(crlFaces=[Face(27), Face(30)], bBreakFace=True)  # [hl]
JPT.Debugger(intersection_line)
