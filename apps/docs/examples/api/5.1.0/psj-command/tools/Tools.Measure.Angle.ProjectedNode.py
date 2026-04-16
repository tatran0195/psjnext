# Title:   Tools.Measure.Angle.ProjectedNode()
# Desc:    Measure the projection angle onto the coordinate system plane
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.Measure.Angle.ProjectedNode
# ---
Geometry.Part.Cube(strName="Cube_2", iPartColor=7697908)
angle = Tools.Measure.Angle.ProjectedNode(crNode=Node(461))  # [hl]
JPT.Debugger(angle)
