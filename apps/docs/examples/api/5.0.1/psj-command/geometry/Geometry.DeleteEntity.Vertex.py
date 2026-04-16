# Title:   Geometry.DeleteEntity.Vertex()
# Desc:    Delete the specified vertexes
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/geometry/Geometry.DeleteEntity.Vertex
# ---
Geometry.Part.Cube()

Geometry.BreakEntity.Edge(crlEdges=[Edge(18)],
                          crlNodes=[Node(85)])

deleting_status = Geometry.DeleteEntity.Vertex(crlVertices=[Vertex(27)])  # [hl]

JPT.Debugger(deleting_status)
