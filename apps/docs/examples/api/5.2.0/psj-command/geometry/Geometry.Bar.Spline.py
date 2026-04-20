# Title:   Geometry.Bar.Spline()
# Desc:    Create a spline-curve bar part passing though the selected nodes
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/geometry/Geometry.Bar.Spline
# ---
Geometry.Part.Cube()

newBar = Geometry.Bar.Spline(crlNodes=[Node(440, 463, 443, 474)])  # [hl]
JPT.Debugger(newBar)
