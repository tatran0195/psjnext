# Title:   Geometry.Edge.ClosedLine()
# Desc:    Imprint closed lines onto face
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/geometry/Geometry.Edge.ClosedLine
# ---
Geometry.Part.Cube()

closed_lines = Geometry.Edge.ClosedLine(veclPositions=[[0.0058, 0.0028, 0.01],   # [hl:start]
                                        [0.0038, 0.0029, 0.01], 
                                        [0.0040, 0.0047, 0.01], 
                                        [0.0063, 0.0046, 0.01]],
                                         crlTargetsFace=[Face(26)])  # [hl:end]
JPT.Debugger(closed_lines)
