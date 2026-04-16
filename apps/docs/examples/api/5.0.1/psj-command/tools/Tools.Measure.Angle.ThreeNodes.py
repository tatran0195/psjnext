# Title:   Tools.Measure.Angle.ThreeNodes()
# Desc:    Measure the angle by using the specified 3 nodes
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/tools/Tools.Measure.Angle.ThreeNodes
# ---
Geometry.Part.Cube()

angle = Tools.Measure.Angle.ThreeNodes(crNode1=Node(445),   # [hl]
                                       crNode2=Node(454),  # [hl]
                                       crNode3=Node(469),   # [hl]
                                       strTarget="XY")  # [hl]

JPT.Debugger(angle)

if type(angle) is list:
    for value in angle:
        print_str += str(value) + ", "
else:
    print_str += str(angle)

print(print_str)
