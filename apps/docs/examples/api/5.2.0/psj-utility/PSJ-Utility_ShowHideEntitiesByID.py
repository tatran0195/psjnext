# Title:   JPT.ShowHideEntitiesByID()
# Desc:    Show or Hide an entity by inputted its ID
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_ShowHideEntitiesByID
# ---
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Hide all parts
JPT.ShowHideAllParts(JPT.BoolType.FALSE_VAL)

# Show Cube_1
JPT.ShowHideEntitiesByID(JPT.DTableType.DTABLE_BODY, 1, JPT.BoolType.TRUE_VAL)  # [hl]
