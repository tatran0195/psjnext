# Title:   Geometry.Face.ExtendFace()
# Desc:    Create a face extended from an edge.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/geometry/Geometry.Face.ExtendFace
# ---
Geometry.Part.Cube()
created_face = Geometry.Face.ExtendFace(crEdge=Edge(19),   # [hl:start]
                                      extendFaceDirection=EXTEND_FACE_DIRECTION(
                                          dComponentX=0, 
                                          dComponentZ=0), 
                                      extendFaceMesh=EXTEND_FACE_MESH(), 
                                      extendFaceOption=EXTEND_FACE_OPTION())  # [hl:end]
JPT.Debugger(created_face)
