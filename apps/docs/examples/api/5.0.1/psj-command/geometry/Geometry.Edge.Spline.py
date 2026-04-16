# Title:   Geometry.Edge.Spline()
# Desc:    Create a spline curve-shaped edge onto a face. At least three nodes on the given faces are specified to create a spline that passes through those nodes
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/geometry/Geometry.Edge.Spline
# ---
Geometry.Part.Cube()

created_splines = Geometry.Edge.Spline(dllPoints=[[0.01, 0.003, 0.01],  # [hl]
                                                  [0.007, 0.003, 0.01],  # [hl]
                                                  [0.005, 0.004, 0.01],   # [hl]
                                                  [0.004, 0.006, 0.01],   # [hl]
                                                  [0.002, 0.007, 0.01],   # [hl]
                                                  [0.0, 0.003, 0.01]],  # [hl]
                                       crlFaces=[Face(26)])  # [hl]

JPT.Debugger(created_splines)
