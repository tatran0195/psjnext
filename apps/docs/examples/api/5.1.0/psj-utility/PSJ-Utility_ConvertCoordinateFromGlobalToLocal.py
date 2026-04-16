# Title:   JPT.ConvertCoordinateFromGlobalToLocal()
# Desc:    Convert coordinate from global to local
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_ConvertCoordinateFromGlobalToLocal
# ---
# Prepare model and local coordinate
Geometry.Part.Cube()
JPT.ViewFitToModel()
Tools.Coordinates.ThreeNode(crlNodes=[Node(488, 96, 88)])

# Get all local coordinates
# And convert global coordinate of specified DItemType.NODE into the selected local coordinate
listCoords = JPT.GetAllCoordinates()
convertCoord = JPT.ConvertCoordinateFromGlobalToLocal(JPT.DItemType.NODE, 8, listCoords[0])  # [hl]


# Get node ID and coordinates of DItem.NODE object according to the converted Coordinate System
JPT.Debugger(convertCoord[0].first)
JPT.Debugger(convertCoord[0].second)
