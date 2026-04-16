# Title:   JPT.DTVector3dToMacroVector()
# Desc:    Convert DTVector3d object to DTVector3d (Macro string type)
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_DTVector3dToMacroVector
# ---
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Get all the existing Nodes and convert one of them to DTVector3D (Macro string type)
## Get all Nodes from model
listNodes = JPT.GetAllNodes() # List of DNode objects
## Get position (DTVector3D) of 1 node in list
posNode1 = listNodes[0].pos # DTVector3D object
# Return DTVector3D object to a string object, for example, return value = [0,0.00777778,0.00444444]
JPT.Debugger(JPT.DTVector3dToMacroVector(posNode1))  # [hl]
