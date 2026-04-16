# Title:   JPT.GetAllFaces()
# Desc:    Get all the information of all existing faces
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_GetAllFaces
# ---
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Get the information of all existing faces
listDFaces = JPT.GetAllFaces()  # [hl]
JPT.Debugger(listDFaces)

# Print all the related information of each existing face in list
for face in listDFaces:
    JPT.Debugger(face)
