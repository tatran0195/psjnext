# Title:   Tools.Coordinates.Rotate()
# Desc:    Create a Coordinate System by rotating with a specified value. Besides, it also be used to modify an existing Coordinate System
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/tools/Tools.Coordinates.Rotate
# ---
Geometry.Part.Cube()
Tools.Coordinates.ThreeNode(crlNodes=[Node(7, 
                                           63, 
                                           87)])

created_coord = Tools.Coordinates.Rotate(vecRotate=[59.9886811502157, 0.0, 0.0],   # [hl]
                                         bCreateNew=False,  # [hl]
                                         crRefCoord=Coord(1),   # [hl]
                                         crEdit=Coord(1))  # [hl]

JPT.Debugger(created_coord)
