# Title:   JPT.GetAllElems()
# Desc:    Get all the information of all existing elements
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetAllElems
# ---
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Get the information of all existing elements
listDElems = JPT.GetAllElems()  # [hl]
JPT.Debugger(listDElems)

# Print all the related information of each existing element in list
for elem in listDElems:
    JPT.Debugger(elem)
