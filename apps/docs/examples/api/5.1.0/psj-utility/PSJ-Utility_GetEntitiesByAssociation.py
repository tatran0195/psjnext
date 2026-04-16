# Title:   JPT.GetEntitiesByAssociation()
# Desc:    Get list of objects by associating from the inputted entity ID and its type
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetEntitiesByAssociation
# ---
# Prepare model
Geometry.Part.Cube()
JPT.ViewFitToModel()

# Get all the associating faces existing on the part with ID = 1
listAssociatedEntities = JPT.GetEntitiesByAssociation(JPT.DItemType.BODY, JPT.AssociateType.AS_FACE, 1)  # [hl]
JPT.Debugger(listAssociatedEntities) # return value is a list DItem has size = 6
