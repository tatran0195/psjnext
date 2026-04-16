# Title:   Geometry.Bar.Arc()
# Desc:    Create an arc-shaped bar part passing though the 3 selected nodes
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/geometry/Geometry.Bar.Arc
# ---
Geometry.Part.Cube()

newBar = Geometry.Bar.Arc(crlNodes=[Node(446, 451, 474)])  # [hl]
JPT.Debugger(newBar)
