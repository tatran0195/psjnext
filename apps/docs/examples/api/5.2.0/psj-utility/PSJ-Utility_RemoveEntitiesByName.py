# Title:   JPT.RemoveEntitiesByName()
# Desc:    Remove entities by using the inputted name
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_RemoveEntitiesByName
# ---
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Remove all the parts with their name have the "_" character inside
JPT.RemoveEntitiesByName(JPT.DTableType.DTABLE_BODY, "_", JPT.BoolType.FALSE_VAL)  # [hl]
