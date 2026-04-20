# Title:   JPT.RemoveAllCoordinates()
# Desc:    Remove all the existing local coordinate systems
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_RemoveAllCoordinates
# ---
# Prepare model
Geometry.Part.Cube()
Tools.Coordinates.ThreeNode(crlNodes=[Node(436, 452, 438)])
Tools.Coordinates.ThreeNode(strName="CRect2", crlNodes=[Node(7, 93, 86)])
Tools.Coordinates.ThreeNode(strName="CCyl1", iCoordType=1, crlNodes=[Node(22, 3, 31)])
Tools.Coordinates.ThreeNode(strName="CSph1", iCoordType=2, crlNodes=[Node(4, 26, 39)])

# Delete all the created coordinates
JPT.RemoveAllCoordinates()  # [hl]
