# Title:   Geometry.Edge.PerpendicularLineToEdge()
# Desc:    Create a perpendicular line on the given faces and through a specified point. The created lines can be started from the specified point or extend to the closest edge object
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/geometry/Geometry.Edge.PerpendicularLineToEdge
# ---
Geometry.Part.Cylinder()

created_edges = Geometry.Edge.PerpendicularLineToEdge(crNode=Node(250),   # [hl]
                                                      crEdge=Edge(1),   # [hl]
                                                      crlFaces=[Face(5)])  # [hl]

JPT.Debugger(created_edges)
