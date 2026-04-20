# Title:   Geometry.Edge.Circle()
# Desc:    Imprint circular edges onto the specified face
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/geometry/Geometry.Edge.Circle
# ---
Geometry.Part.Cube()

circle_lines = Geometry.Edge.Circle(veclPositions=[[0.006666666666666666, 0.005555555555555556, 0.01],   # [hl:start]
                                                [0.002222222222222222, 0.006666666666666666, 0.01]], 
                                                crlTargetFace=[Face(26)], 
                                                dOutRadius=2.0)  # [hl:end]
JPT.Debugger(circle_lines)
