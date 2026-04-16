# Title:   Geometry.Edge.PerpendicularCylinderLine()
# Desc:    Create an edge perpendicular to the circular face on the curved face which can offset the imprinted line by specifying an angle value or an edge length value
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/geometry/Geometry.Edge.PerpendicularCylinderLine
# ---
Geometry.Part.Cylinder(iPartColor=5093709)

created_edges = Geometry.Edge.PerpendicularCylinderLine(crlNodes=[Node(19, 157)],   # [hl]
                                                crlFaces=[Face(5)],  # [hl]
                                                dOffset=1.0,   # [hl]
                                                bOppositeSide=True)  # [hl]
JPT.Debugger(created_edges)
