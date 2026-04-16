# Title:   Geometry.ShowAdjacent.Faces()
# Desc:    Expand the selection in all directions, regardless of the shape of surrounding features or the angle at which objects are joined. It obtained by recursively finding adjacent faces at an angle of less than or equal to the specified angle
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/geometry/Geometry.ShowAdjacent.Faces
# ---
Geometry.Part.Cube()
adjacent_faces = Geometry.ShowAdjacent.Faces(dAngle=0, iNumOfLayers=100, crlStartFaces=[Face(26)])  # [hl]
JPT.Debugger(adjacent_faces)
