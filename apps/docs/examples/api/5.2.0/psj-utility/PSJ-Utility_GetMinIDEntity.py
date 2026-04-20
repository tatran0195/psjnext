# Title:   JPT.GetMinIDEntity()
# Desc:    Get the minimum ID of the inputted DItemType
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetMinIDEntity
# ---
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Get the minimum ID of the created parts
iMinID = JPT.GetMinIDEntity(JPT.DItemType.BODY)  # [hl]
JPT.Debugger(iMinID) # 1
