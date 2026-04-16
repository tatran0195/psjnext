# Title:   Geometry.Edge.OffsetLine()
# Desc:    Create new edges by offsetting specified edges
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/geometry/Geometry.Edge.OffsetLine
# ---
Geometry.Part.Cube(iPartColor=6484066)

offset_lines = Geometry.Edge.OffsetLine(crlFaces=[Face(22)],   # [hl]
                                        crlEdges=[Edge(19)],   # [hl]
                                        dOffsetDistance=0.001,   # [hl]
                                        iLayerNumber=6)  # [hl]

JPT.Debugger(offset_lines)
