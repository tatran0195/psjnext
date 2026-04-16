# Title:   Geometry.Edge.PerpendicularLineOfEdge()
# Desc:    Create a perpendicular edge through a line defined by two nodes. The first selected node will be start point of new line
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/geometry/Geometry.Edge.PerpendicularLineOfEdge
# ---
Geometry.Part.Cube(iPartColor=6215639)

created_edge = Geometry.Edge.PerpendicularLineOfEdge(crlNodes=[Node(344, 339)],   # [hl]
                                                     crlFaces=[Face(24,   # [hl]
                                                                    22,   # [hl]
                                                                    26,   # [hl]
                                                                    25,   # [hl]
                                                                    21,   # [hl]
                                                                    23)])  # [hl]

JPT.Debugger(created_edge)
