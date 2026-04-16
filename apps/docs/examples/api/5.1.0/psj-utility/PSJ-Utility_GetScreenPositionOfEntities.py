# Title:   JPT.GetScreenPositionOfEntities()
# Desc:    Obtains the position of the specified item in the Main Window.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetScreenPositionOfEntities
# ---
# Prepare model
Geometry.Part.Cube(iPartColor=13290083)
Geometry.Part.Cube(dlOrigin=[0.012, 0.0, 0.0], strName="Cube_2", iPartColor=6149981)
JPT.ViewFitToModel()

# Check screen position of parts in Main Window.
ditem_list=JPT.GetAllByTypeID(JPT.DItemType.BODY)  # [hl]
pos=JPT.GetScreenPositionOfEntities(ditem_list)
JPT.Debugger(pos)
