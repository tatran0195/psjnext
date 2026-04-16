# Title:   Geometry.Edge.Angle()
# Desc:    Create a new edge by convert angle
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/geometry/Geometry.Edge.Angle
# ---
Geometry.Part.Cube()

edges = Geometry.Edge.Angle(crplElemEdges=[CursorPair(Node(461), Node(470)),   # [hl]
                                           CursorPair(Node(445), Node(446))],   # [hl]
                            dEdgeAngle=135.0,   # [hl]
                            bCurvature=False,   # [hl]
                            bBreakFace=True)  # [hl]

JPT.Debugger(edges)
