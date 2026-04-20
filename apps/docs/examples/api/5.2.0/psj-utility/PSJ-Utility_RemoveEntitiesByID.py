# Title:   JPT.RemoveEntitiesByID()
# Desc:    Delete specified entity by inputting its type and its ID
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_RemoveEntitiesByID
# ---
# Prepare model
Geometry.Part.Cube(iPartColor=12829526)
Geometry.Part.Cube(strName="Cube_2", iPartColor=8060538)
Geometry.Part.Cube(strName="Cube_3", iPartColor=13787489)
JPT.ViewFitToModel()

# Delete Cube_2 part
JPT.RemoveEntitiesByID(JPT.DItemType.BODY, 2)  # [hl]
