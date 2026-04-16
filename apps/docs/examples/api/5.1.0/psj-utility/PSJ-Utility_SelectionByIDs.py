# Title:   JPT.SelectionByIDs()
# Desc:    Select entities by using their list of IDs
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_SelectionByIDs
# ---
# Prepare model
Geometry.Part.Cube(iPartColor=6974164)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=7599987)
JPT.ViewFitToModel()

# Select face with IDs = [50, 51, 52]
JPT.SelectionByIDs(JPT.DItemType.FACE, [50, 51, 52], JPT.BoolType.TRUE_VAL)  # [hl]
