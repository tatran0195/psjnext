# Title:   Tools.Measure.Angle.TwoNodesAxis()
# Desc:    Measure the angle created by 2 nodes and Axis.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.Measure.Angle.TwoNodesAxis
# ---
Geometry.Part.Cube()

angle=Tools.Measure.Angle.TwoNodesAxis(  # [hl:start]
    crNode1=Node(462), 
    crNode2=Node(466), 
    dlAxis=[0.0, 1.0, 0.0])  # [hl:end]

JPT.Debugger(angle)
