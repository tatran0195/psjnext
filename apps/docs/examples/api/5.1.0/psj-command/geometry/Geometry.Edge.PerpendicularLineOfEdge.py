# Title:   Geometry.Edge.PerpendicularLineOfEdge()
# Desc:    Create an edge perpendicular to the line defined by two nodes in the selected faces
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/geometry/Geometry.Edge.PerpendicularLineOfEdge
# ---
Geometry.Part.Cube(iPartColor=6215639)

created_edges = Geometry.Edge.PerpendicularLineOfEdge(crlNodes=[Node(344, 339)],   # [hl]
                                                     crlFaces=[Face(24,   # [hl]
                                                                    22,   # [hl]
                                                                    26,   # [hl]
                                                                    25,   # [hl]
                                                                    21,   # [hl]
                                                                    23)])  # [hl]
JPT.Debugger(created_edges)
