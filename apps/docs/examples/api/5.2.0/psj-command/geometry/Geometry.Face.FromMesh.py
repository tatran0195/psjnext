# Title:   Geometry.Face.FromMesh()
# Desc:    Create a new geometric face from the specified mesh face
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/geometry/Geometry.Face.FromMesh
# ---
Geometry.Part.Cube()

created_face = Geometry.Face.FromMesh(crFace=Face(26))  # [hl]
JPT.Debugger(created_face)
