# Title:   Geometry.Edge.PerpendicularCylinderLine()
# Desc:    Create a perpendicular line to the circular face on the curved face which can offset the imprinted line by specifying an angle value or an edge length value
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/geometry/Geometry.Edge.PerpendicularCylinderLine
# ---
Geometry.Part.Cylinder(iPartColor=5093709)

edges = Geometry.Edge.PerpendicularCylinderLine(crlNodes=[Node(19, 157)],   # [hl]
                                                crlFaces=[Face(5)],  # [hl]
                                                dOffset=1.0,   # [hl]
                                                bOppositeSide=True)  # [hl]

JPT.Debugger(edges)
