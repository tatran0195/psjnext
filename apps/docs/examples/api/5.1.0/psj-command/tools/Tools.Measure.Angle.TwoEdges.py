# Title:   Tools.Measure.Angle.TwoEdges()
# Desc:    Measure the angle created by 2 edges
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.Measure.Angle.TwoEdges
# ---
Geometry.Part.Cube()

angle = Tools.Measure.Angle.TwoEdges(crEdge1=Edge(19),   # [hl]
                                     crEdge2=Edge(18))  # [hl]

JPT.Debugger(angle)
