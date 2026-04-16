# Title:   Geometry.Transform.Scaling()
# Desc:    Resize an part about its centroid or a coordinate system. It can resize different dimensions at different scales
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/geometry/Geometry.Transform.Scaling
# ---
Geometry.Part.Cube()

scaling_status = Geometry.Transform.Scaling(crlParts=[Part(1)],   # [hl]
                                            dlScaleVector=[1.5,   # [hl]
                                                           0.5,   # [hl]
                                                           0.5],   # [hl]
                                            bCreateNew=True)  # [hl]

JPT.Debugger(scaling_status)
