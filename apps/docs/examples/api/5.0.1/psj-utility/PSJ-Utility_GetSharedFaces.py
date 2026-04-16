# Title:   JPT.GetSharedFaces()
# Desc:    Get all information of the shared faces
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_GetSharedFaces
# ---
# Prepare model
Geometry.Part.Cube(iPartColor=6217822)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6908379)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_3", iPartColor=7138924)
Geometry.Part.Cube(dlOrigin=[0.03, 0.0, 0.0], strName="Cube_4", iPartColor=15753968)
JPT.ViewFitToModel()

# Create shared faces
JPT.Exec('AssembleFaceMatingStep([], [], [3:1, 3:2, 3:3, 3:4], 1e-05)')
JPT.Exec('AssembleFaceEx([49, 24, 50, 75, 101, 76], 1e-05, 0, 0)')

# Get the information of all shared faces
listParts = JPT.GetAllByType(JPT.DItemType.BODY)
listSharedFaces = JPT.GetSharedFaces(listParts)  # [hl]
JPT.Debugger(listSharedFaces)
