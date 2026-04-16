# Title:   Tools.Coordinates.Align()
# Desc:    Create a Coordinate System by aligning an Axis direction of Coordinate System follow with an Edge or 2 selected Nodes (1D Element). Besides, it also be used to modify an existing Coordinate System
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.Coordinates.Align
# ---
Geometry.Part.Cube()
Tools.Coordinates.ThreeNode(crlNodes=[Node(7, 
                                           63, 
                                           87)])

created_coord = Tools.Coordinates.Align(strName="CRect2",   # [hl]
                                        bCreateNew=False,   # [hl]
                                        crlNodes=[Node(179,   # [hl]
                                                       194)],  # [hl]
                                        crEdit=Coord(1))  # [hl]

JPT.Debugger(created_coord)
