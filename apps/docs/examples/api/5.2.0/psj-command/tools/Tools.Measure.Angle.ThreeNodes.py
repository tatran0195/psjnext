# Title:   Tools.Measure.Angle.ThreeNodes()
# Desc:    Measure the angle by using the specified 3 nodes
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.Measure.Angle.ThreeNodes
# ---
Geometry.Part.Cube()

angle = Tools.Measure.Angle.ThreeNodes(crNode1=Node(445),   # [hl]
                                       crNode2=Node(454),  # [hl]
                                       crNode3=Node(469),   # [hl]
                                       strTarget="XY")  # [hl]
JPT.Debugger(angle)
