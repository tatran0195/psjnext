# Title:   JPT.GetMaxIDEntity()
# Desc:    Get the maximum ID of the inputted DItemType
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_GetMaxIDEntity
# ---
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Get the maximum ID of the created parts
iMaxID = JPT.GetMaxIDEntity(JPT.DItemType.BODY)  # [hl]
JPT.Debugger(iMaxID) # 3
