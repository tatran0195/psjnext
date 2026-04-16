# Title:   Tools.Coordinates.AttachCircle()
# Desc:    Create a Coordinate System at the center of the Circular Edge. Besides, it also be used to modify an existing Coordinate System
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.Coordinates.AttachCircle
# ---
Geometry.Part.Cylinder()
Tools.Coordinates.ThreeNode(veclPoints=[[0.01, 0.01, 0.01], 
                                        [0.002, 0.002, 0.002], 
                                        [0.01, 0.001, 0.01]])

created_coord = Tools.Coordinates.AttachCircle(strName="CRect2",   # [hl]
                                               crEdge=Edge(2),   # [hl]
                                               crEdit=Coord(1))  # [hl]

JPT.Debugger(created_coord)
