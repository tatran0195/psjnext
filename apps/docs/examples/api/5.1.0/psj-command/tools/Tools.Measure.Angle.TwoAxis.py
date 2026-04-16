# Title:   Tools.Measure.Angle.TwoAxis()
# Desc:    Measure the angle created by 2 Axis.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.Measure.Angle.TwoAxis
# ---
Geometry.Part.Cube()
Tools.Coordinates.ThreeNode(crlNodes=[Node(7, 8, 5)])
Tools.Coordinates.ThreeNode(strName="CRect2", crlNodes=[Node(3, 7, 2)])

angle = Tools.Measure.Angle.TwoAxis(dlXyz1=[0.0, -1.0, 0.0], dlXyz2=[1.0, 0.0, 0.0])  # [hl]

JPT.Debugger(angle)
