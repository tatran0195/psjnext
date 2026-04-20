# Title:   Geometry.Face.SmoothFace()
# Desc:    Create geometric face from given boundaries set by selected edges.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/geometry/Geometry.Face.SmoothFace
# ---
Geometry.Part.Sphere()
Geometry.Edge.Angle(
    [CursorPair(Node(146), Node(147)), 
    CursorPair(Node(148), Node(168)), 
    CursorPair(Node(267), Node(268)), 
    CursorPair(Node(224), Node(244))])
Geometry.DeleteEntity.Face(crlFaces=[Face(2)])

created_face = Geometry.Face.SmoothFace(crlTargets=[Edge(3)])  # [hl]
JPT.Debugger(created_face)
