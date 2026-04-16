# Title:   Geometry.Edge.PlanarLine()
# Desc:    Create edges at the intersection of the given faces and a planar face defining by 3 points or axis plane
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/geometry/Geometry.Edge.PlanarLine
# ---
Geometry.Part.Cube()

edges = Geometry.Edge.PlanarLine(dllPoints=[[0.01, 0.005, 0.006]],   # [hl]
                                 crlFaces=[Face(24, 26)],   # [hl]
                                 iAxisPlane=1)  # [hl]

JPT.Debugger(edges)
