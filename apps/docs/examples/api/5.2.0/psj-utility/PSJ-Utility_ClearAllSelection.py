# Title:   JPT.ClearAllSelection()
# Desc:    Clear all the selected entities
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_ClearAllSelection
# ---
# Prepare model
Geometry.Part.Cube(iPartColor=6974164)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=7599987)
JPT.ViewFitToModel()

# Select face with ID = 51
JPT.SelectionByID(JPT.DItemType.FACE, 51, True)

# Deselect all the selected entities
JPT.ClearAllSelection()  # [hl]
