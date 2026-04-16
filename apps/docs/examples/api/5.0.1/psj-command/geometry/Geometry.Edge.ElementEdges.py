# Title:   Geometry.Edge.ElementEdges()
# Desc:    Create edges by selecting individual element edges
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/geometry/Geometry.Edge.ElementEdges
# ---
Geometry.Part.Cube()

created_edges = Geometry.Edge.ElementEdges(crplElemEdges=[CursorPair(Node(443),   # [hl]
                                                                     Node(452)),   # [hl]
                                                          CursorPair(Node(444),   # [hl]
                                                                     Node(445)),   # [hl]
                                                          CursorPair(Node(454),   # [hl]
                                                                     Node(463))])  # [hl]

JPT.Debugger(created_edges)
