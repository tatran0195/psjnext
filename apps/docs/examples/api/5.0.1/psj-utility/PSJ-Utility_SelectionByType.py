# Title:   JPT.SelectionByType()
# Desc:    Select all the existing entities by type
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_SelectionByType
# ---
# Prepare model
Geometry.Part.Cube(iPartColor=6974164)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=7599987)

# Select all the created parts
JPT.SelectionByType(JPT.DItemType.BODY, JPT.BoolType.TRUE_VAL)  # [hl]
