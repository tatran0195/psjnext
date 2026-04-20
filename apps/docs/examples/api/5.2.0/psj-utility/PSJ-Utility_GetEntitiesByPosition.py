# Title:   JPT.GetEntitiesByPosition()
# Desc:    Get the entity satisfying the given conditions (X, Y, Z)
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetEntitiesByPosition
# ---
# Prepare model
Geometry.Part.Cube()
JPT.ViewFitToModel()

# Get the information of the created cube
selPart = JPT.GetEntitiesByPosition(JPT.AssociateType.AS_BODY, 10, 10, 10)  # [hl]
JPT.Debugger(selPart[0]) # second element of the created list
