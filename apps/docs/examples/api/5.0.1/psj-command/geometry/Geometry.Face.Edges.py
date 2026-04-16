# Title:   Geometry.Face.Edges()
# Desc:    Create a face using the given edges as the face's boundaries. It will create a face by creating the geometry consisting of the underlying surface, associated edges, and vertices. The planar surfaces and smooth surfaces are switched by changing the related arguments
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/geometry/Geometry.Face.Edges
# ---
Geometry.Part.Cube()

created_face = Geometry.Face.Edges(crlEdges=[Edge(9, 19)])  # [hl]

JPT.Debugger(created_face)
