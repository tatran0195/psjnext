# Title:   Tools.Measure.Radius.ThreeNodes()
# Desc:    Measure arc radius by using 3 nodes
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/tools/Tools.Measure.Radius.ThreeNodes
# ---
Geometry.Part.Cylinder()

radius = Tools.Measure.Radius.ThreeNodes(crNode13=Node(18),   # [hl]
                                         crNode23=Node(14),   # [hl]
                                         crNode33=Node(8))  # [hl]

JPT.Debugger(radius)
