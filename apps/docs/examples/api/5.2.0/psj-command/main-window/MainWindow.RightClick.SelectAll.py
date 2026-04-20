# Title:   MainWindow.RightClick.SelectAll()
# Desc:    Select all faces or shell elements according to the specified target type
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/main-window/MainWindow.RightClick.SelectAll
# ---
# Prepare models
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)
JPT.ViewFitToModel()

# Select all faces
listFaces = MainWindow.RightClick.SelectAll(iTargetType=3)  # [hl]
print(listFaces)

# Select all 2D elements
listElems= MainWindow.RightClick.SelectAll(iTargetType=7)  # [hl]
print(listElems)
