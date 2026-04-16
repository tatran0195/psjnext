# Title:   Tools.Measure.Radius.Edge()
# Desc:    Measure arc radius of the specified edge
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.Measure.Radius.Edge
# ---
Geometry.Part.Cylinder()

radius = Tools.Measure.Radius.Edge(crEdge=Edge(1))  # [hl]

JPT.Debugger(radius)
