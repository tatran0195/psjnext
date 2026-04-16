# Title:   Geometry.Edge.PerpendicularLineToEdge()
# Desc:    Create an edge perpendicular to the selected edges through a specified point on the selected faces
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/geometry/Geometry.Edge.PerpendicularLineToEdge
# ---
Geometry.Part.Cylinder()

created_edges = Geometry.Edge.PerpendicularLineToEdge(crNode=Node(250),   # [hl]
                                                      crEdge=Edge(1),   # [hl]
                                                      crlFaces=[Face(5)])  # [hl]
JPT.Debugger(created_edges)
