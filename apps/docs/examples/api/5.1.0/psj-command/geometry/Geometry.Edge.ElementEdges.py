# Title:   Geometry.Edge.ElementEdges()
# Desc:    Create edges from the selected element edges
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/geometry/Geometry.Edge.ElementEdges
# ---
Geometry.Part.Cube()

created_edges = Geometry.Edge.ElementEdges(crplElemEdges=[CursorPair(Node(443), Node(452)),   # [hl]
                                                          CursorPair(Node(444), Node(445)),   # [hl]
                                                          CursorPair(Node(454), Node(463))])  # [hl]
JPT.Debugger(created_edges)
