# Title:   JPT.GetCenterOfEntities()
# Desc:    Get center coordinate of selected entities
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetCenterOfEntities
# ---
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Get the center coordinate of the inputted entities
listParts = JPT.GetAllByTypeID(3)
JPT.Debugger(JPT.GetCenterOfEntities(listParts))  # [hl]
