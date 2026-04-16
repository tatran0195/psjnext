# Title:   JPT.RemoveAllByTableType()
# Desc:    Remove all the entities relating to the inputted DTableType
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_RemoveAllByTableType
# ---
# Prepare model
Geometry.Part.Cube(iPartColor=5955674)
Geometry.Part.Cube(strName="Cube_2", iPartColor=5682356)
Geometry.Part.Cube(strName="Cube_3", iPartColor=12237393)
Geometry.Part.Cube(strName="Cube_4", iPartColor=6740326)
Geometry.Part.Cube(strName="Cube_5", iPartColor=7335919)

# Remove all the created parts
JPT.RemoveAllByTableType(JPT.DTableType.DTABLE_BODY)  # [hl]
