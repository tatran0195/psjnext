# Title:   JPT.GetCountByType()
# Desc:    Get total number of entities by inputting DItemType
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetCountByType
# ---
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Count the total number of bodies existing on the current Jupiter
iPartCount = JPT.GetCountByType(JPT.DItemType.BODY)
print(iPartCount) # 3  # [hl]
