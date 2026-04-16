# Title:   Tools.Measure.Distance.TwoNodes()
# Desc:    Measure distance between two nodes
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/tools/Tools.Measure.Distance.TwoNodes
# ---
Geometry.Part.Cube()

distance = Tools.Measure.Distance.TwoNodes(crNode1=Node(454),   # [hl]
                                           crNode2=Node(472),   # [hl]
                                           strTarget="Dist")  # [hl]
  # [hl]
JPT.Debugger(distance)

print_str = ", ".join([str(value) for value in distance])
print(print_str)
