# Title:   JPT.SelectionByID()
# Desc:    Select an entity by using its ID
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_SelectionByID
# ---
# Prepare model
Geometry.Part.Cube(iPartColor=6974164)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=7599987)
JPT.ViewFitToModel()

# Select face with ID = 51
JPT.SelectionByID(JPT.DItemType.FACE, 51, JPT.BoolType.TRUE_VAL)  # [hl]
