# Title:   Geometry.Bar.TwoNodes()
# Desc:    Create a Bar part from two selected nodes
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/geometry/Geometry.Bar.TwoNodes
# ---
Geometry.Part.Cube()

newBar = Geometry.Bar.TwoNodes(crStartNode=Node(5), crEndNode=Node(7))  # [hl]
JPT.Debugger(newBar)
