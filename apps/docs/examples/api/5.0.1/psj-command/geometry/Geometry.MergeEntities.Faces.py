# Title:   Geometry.MergeEntities.Faces()
# Desc:    Merge the selected faces into a single face
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/geometry/Geometry.MergeEntities.Faces
# ---
Geometry.Part.Cube()
Geometry.Edge.Line(dllPoints=[[0.005, 0, 0.01],
                              [0.006, 0.01, 0.01]],
                   crlFaces=[Face(26)])
Geometry.Edge.Line(dllPoints=[[0.002, 0.002, 0.01],
                              [0.003, 0.005, 0.01]],
                   crlFaces=[Face(26)])
merged_faces = Geometry.MergeEntities.Faces(crlFaces=[Face(26, 28)])  # [hl]
JPT.Debugger(merged_faces)
