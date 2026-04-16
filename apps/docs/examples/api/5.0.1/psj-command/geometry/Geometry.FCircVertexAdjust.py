# Title:   Geometry.FCircVertexAdjust()
# Desc:    Align the vertexes positions on the circles. Cylinder faces can also be split by 90 degree, for creating mapped mesh
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/geometry/Geometry.FCircVertexAdjust
# ---
# Make a cylinder with 2 misaligned vertex
Geometry.Part.Cylinder()
Geometry.BreakEntity.Edge(crlNodes=[Node(66)])
Geometry.BreakEntity.Edge(crlNodes=[Node(51)])

# Align vertex positions on 2 circles of the cylinder
adjust_status = Geometry.FCircVertexAdjust(crlParts=[Part(1)])  # [hl]

JPT.Debugger(adjust_status)
