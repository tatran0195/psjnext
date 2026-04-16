# Title:   Geometry.Edge.Line()
# Desc:    Create edges based on the selected nodes
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/geometry/Geometry.Edge.Line
# ---
Geometry.Part.Cube(iPartColor=6215639)

created_edges = Geometry.Edge.Line(dllPoints=[[0.01, 0, 0.01],   # [hl]
                                              [0, 0.01, 0.01]],   # [hl]
                                   crlFaces=[Face(26)])  # [hl]

JPT.Debugger(created_edges)
