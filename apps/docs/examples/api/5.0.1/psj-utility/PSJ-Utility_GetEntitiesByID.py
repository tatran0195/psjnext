# Title:   JPT.GetEntitiesByID()
# Desc:    Get information of the inputted entity ID
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_GetEntitiesByID
# ---
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Get the information of the part with ID = 2 and store it to a list
listParts = JPT.GetEntitiesByID(JPT.DItemType.BODY, 2)  # [hl]

# Print the information of the part
JPT.Debugger(listParts[0])
