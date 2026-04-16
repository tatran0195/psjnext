# Title:   JPT.GetEntitiesByName()
# Desc:    Get information of the inputted entity name
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_GetEntitiesByName
# ---
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Get the information of the part with name = "_" and store it to a list
listParts = JPT.GetEntitiesByName(JPT.DTableType.DTABLE_BODY, "_", JPT.BoolType.FALSE_VAL)  # [hl]
print(listParts[0].name) # Cube_1
print(listParts[2].name) # Cube_3
print(listParts[2].id) # 3
