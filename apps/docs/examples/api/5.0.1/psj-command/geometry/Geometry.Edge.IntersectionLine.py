# Title:   Geometry.Edge.IntersectionLine()
# Desc:    Create Edge along the intersection line of faces
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/geometry/Geometry.Edge.IntersectionLine
# ---
Geometry.Part.Cube()

Geometry.Face.Edges(crlEdges=[Edge(20, 10)], bCreatePart=True)

Geometry.Face.Edges(crlEdges=[Edge(18, 12)], bCreatePart=True)

Geometry.DeleteEntity.Part(crlParts=[Part(1)])

Geometry.Edge.IntersectionLine(crlFaces=[Face(27), Face(30)], bBreakFace=True)
