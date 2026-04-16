# Title:   JPT.GetAllEdges()
# Desc:    Get all the information of all existing edges
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetAllEdges
# ---
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Get the information of all existing edges
listDEdges = JPT.GetAllEdges()  # [hl]
JPT.Debugger(listDEdges)

# Print all the related information of each existing edge in list
for edge in listDEdges:
    JPT.Debugger(edge)
