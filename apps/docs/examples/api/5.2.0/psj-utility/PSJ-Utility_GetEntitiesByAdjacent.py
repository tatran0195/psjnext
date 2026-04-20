# Title:   JPT.GetEntitiesByAdjacent()
# Desc:    Get list of objects by adjacency based on the stop angle
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetEntitiesByAdjacent
# ---
# Prepare model
Geometry.Part.Cube()
JPT.ViewFitToModel()

# Get the faces relating to the face with ID = 26 based on angle = 30
adjacentFaces = JPT.GetEntitiesByAdjacent(JPT.DItemType.FACE, 26, 30)  # [hl]
JPT.Debugger(adjacentFaces)
