# Title:   JPT.GetAllNodes()
# Desc:    Get all the information of all existing nodes
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetAllNodes
# ---
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Get the information of all existing nodes
listDNodes = JPT.GetAllNodes()  # [hl]
JPT.Debugger(listDNodes)

# Print all the related information of each existing node in list
for node in listDNodes:
    JPT.Debugger(node)
