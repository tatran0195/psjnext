# Title:   Assemble.ConvertToSharedFaces()
# Desc:    If a pair of Tri elements that share all three vertices exists within the document or on the specified surface, they are converted into a shared surface between the two parts to which they belong.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/assemble/Assemble.ConvertToSharedFaces
# ---
Geometry.Part.Cube(iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=7463537)
MeshEdit.MergeNodes(dTolerance=0.1, iKeepType=2, crlTargets=[Face(49, 24)])

shared_face = Assemble.ConvertToSharedFaces(crlFaces=[Face(24, 49)])  # [hl]
JPT.Debugger(shared_face)
