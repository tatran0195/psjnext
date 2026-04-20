# Title:   Tools.Coordinates.ThreeNode()
# Desc:    Create a Coordinate System by selecting 3 nodes
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.Coordinates.ThreeNode
# ---
Geometry.Part.Cube()

created_coord = Tools.Coordinates.ThreeNode(crlNodes=[Node(7,   # [hl]
                                                           93,   # [hl]
                                                           477)])  # [hl]

JPT.Debugger(created_coord)
