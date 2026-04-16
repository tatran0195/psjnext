# Title:   Tools.Measure.Angle.TwoElemEdges()
# Desc:    
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.Measure.Angle.TwoElemEdges
# ---
Geometry.Part.Cube()

angle = Tools.Measure.Angle.TwoElemEdges(  # [hl:start]
            crpElemEdge1=CursorPair(Node(95), Node(487)), 
            crpElemEdge2=CursorPair(Node(453), Node(462)))  # [hl:end]

JPT.Debugger(angle)
