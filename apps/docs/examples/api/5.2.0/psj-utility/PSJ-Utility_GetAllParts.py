# Title:   JPT.GetAllParts()
# Desc:    Get all the information of all existing parts
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetAllParts
# ---
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Get the information of all existing parts
listDBodies = JPT.GetAllParts()  # [hl]
JPT.Debugger(listDBodies)

# Print all the related information of each existing part in list
for part in listDBodies:
    JPT.Debugger(part)
