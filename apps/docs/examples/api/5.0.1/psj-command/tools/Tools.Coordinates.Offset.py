# Title:   Tools.Coordinates.Offset()
# Desc:    Create a Coordinate System by offsetting with a specified value. Besides, it also be used to modify an existing Coordinate System
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/tools/Tools.Coordinates.Offset
# ---
Geometry.Part.Cylinder()
Tools.Coordinates.ThreeNode(veclPoints=[[0.01, 0.01, 0.01], 
                                        [0.002, 0.002, 0.002], 
                                        [0.01, 0.001, 0.01]])

created_coord = Tools.Coordinates.Offset(strName="CRect2",   # [hl]
                                         vecTranslate=[0.01,   # [hl]
                                                       0.01,   # [hl]
                                                       0.01])  # [hl]

JPT.Debugger(created_coord)
