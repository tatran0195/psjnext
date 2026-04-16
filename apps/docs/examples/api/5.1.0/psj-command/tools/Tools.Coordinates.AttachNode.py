# Title:   Tools.Coordinates.AttachNode()
# Desc:    Create a Coordinate System at the specific node. Besides, it also be used to modify an existing Coordinate System
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.Coordinates.AttachNode
# ---
Geometry.Part.Cylinder()
Tools.Coordinates.ThreeNode(veclPoints=[[0.01, 0.01, 0.01], 
                                        [0.002, 0.002, 0.002], 
                                        [0.01, 0.001, 0.01]])

created_coord = Tools.Coordinates.AttachNode(strName="CRect3",   # [hl]
                                             crNode=Node(141),   # [hl]
                                             crEdit=Coord(1))  # [hl]

JPT.Debugger(created_coord)
