# Title:   JPT.ShowHideAllParts()
# Desc:    Show or Hide all part existing on the screen
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_ShowHideAllParts
# ---
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Show all parts
JPT.ShowHideAllParts(JPT.BoolType.TRUE_VAL)  # [hl]
