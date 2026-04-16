# Title:   Geometry.BreakEntity.Face()
# Desc:    Break the faces into separate units that are surrounded by edges
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/geometry/Geometry.BreakEntity.Face
# ---
Geometry.Part.Cube()

Geometry.Edge.Line(dllPoints=[[0.01, 0, 0.01], 
                              [0, 0.01, 0.01]], 
                   crlFaces=[Face(26)],
                   bBreakFace=False)

faces = Geometry.BreakEntity.Face(crlFaces=[Face(26)])  # [hl]

JPT.Debugger(faces)
