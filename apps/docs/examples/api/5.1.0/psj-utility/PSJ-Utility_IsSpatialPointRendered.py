# Title:   JPT.IsSpatialPointRendered()
# Desc:    Check if a specified point (node) that has the spatial coordinates (X, Y, Z) is rendered in the current view
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_IsSpatialPointRendered
# ---
# Prepare model
Geometry.Part.Cube(iPartColor=6974164)
JPT.ViewFitToModel()

# Select a node with ID = 7
JPT.SelectionByID(JPT.DItemType.NODE, 7, True)
listSelNodes = JPT.GetSelectedNodes()

# Check if the selected node is rendered
result=JPT.IsSpatialPointRendered(listSelNodes[0].pos.x, listSelNodes[0].pos.y, listSelNodes[0].pos.z)  # [hl]
print(result)
