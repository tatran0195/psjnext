# Title:   Tools.Measure.Distance.TwoEdges()
# Desc:    Measure the distance between two edges
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/tools/Tools.Measure.Distance.TwoEdges
# ---
Geometry.Part.Cube()

distance = Tools.Measure.Distance.TwoEdges(crEdge1=Edge(20),   # [hl]
                                           crEdge2=Edge(18))  # [hl]

JPT.Debugger(distance)
