# Title:   JPT.GetElemsByKind()
# Desc:    Get a list of element by inputting their kind (1D, 2D, 3D, etc.)
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetElemsByKind
# ---
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Get the information of all existing 2D elements
list2DElems = JPT.GetElemsByKind(JPT.ElemKind.ELEMKIND_2D)  # [hl]
JPT.Debugger(list2DElems)

# Print all the related information of each existing 2D element in list
for elem in list2DElems:
    JPT.Debugger(elem)
