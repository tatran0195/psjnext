# Title:   Geometry.BreakEntity.Part()
# Desc:    Separate parts into separated units based on each closed geometries
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/geometry/Geometry.BreakEntity.Part
# ---
Geometry.Part.Cube(iPartColor=16147556)
Geometry.DeleteEntity.Face([Face(24, 22, 26, 21, 25)])
Geometry.Edge.Line(dllPoints=[[0, 0.0022, 0], 
                              [0, 0.0022, 0.01]], 
                   crlFaces=[Face(23)])
Geometry.Edge.Line(dllPoints=[[0, 0.0067, 0], 
                              [0, 0.0067, 0.01]], 
                   crlFaces=[Face(23)])
Geometry.DeleteEntity.Face([Face(23)])

bodies = Geometry.BreakEntity.Part(crlParts=[Part(1)])  # [hl]

JPT.Debugger(bodies)
