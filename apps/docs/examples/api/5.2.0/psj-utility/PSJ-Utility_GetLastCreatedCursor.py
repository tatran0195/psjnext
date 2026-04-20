# Title:   JPT.GetLastCreatedCursor()
# Desc:    Get the information of the last created entity
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetLastCreatedCursor
# ---
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Get the information of the last created part
lastCreatedCursor = JPT.GetLastCreatedCursor()  # [hl]
JPT.Debugger(lastCreatedCursor[0]) # Cube_3
