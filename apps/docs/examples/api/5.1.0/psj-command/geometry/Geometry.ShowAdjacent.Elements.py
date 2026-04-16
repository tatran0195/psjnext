# Title:   Geometry.ShowAdjacent.Elements()
# Desc:    Expand the selection in all directions, regardless of the shape of surrounding features or the angle at which objects are joined. It obtained by recursively finding adjacent elements at an angle of less than or equal to the specified angle
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/geometry/Geometry.ShowAdjacent.Elements
# ---
Geometry.Part.Cube()
adjacent_elements = Geometry.ShowAdjacent.Elements(dAngle=5.0, crlStartElems=[Elem(1005)])  # [hl]
JPT.Debugger(adjacent_elements)
