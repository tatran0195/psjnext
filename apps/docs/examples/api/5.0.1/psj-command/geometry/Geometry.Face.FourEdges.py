# Title:   Geometry.Face.FourEdges()
# Desc:    Create a face using the given four edges as the face's boundaries. The given edges must form a closed profile and must not contain multiple loops
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/geometry/Geometry.Face.FourEdges
# ---
Geometry.Part.Cube()

Geometry.DeleteEntity.Face(crlFaces=[Face(26)])

created_face = Geometry.Face.FourEdges(crlEdges=[Edge(17, 18, 19, 20)])  # [hl]

JPT.Debugger(created_face)
