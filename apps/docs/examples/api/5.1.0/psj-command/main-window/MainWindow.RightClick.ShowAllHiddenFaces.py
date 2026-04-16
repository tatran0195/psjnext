# Title:   MainWindow.RightClick.ShowAllHiddenFaces()
# Desc:    Show all hidden faces of displaying bodies
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/main-window/MainWindow.RightClick.ShowAllHiddenFaces
# ---
# Prepare models
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_3", iPartColor=13259210)
Geometry.Part.Cube(dlOrigin=[0.03, 0.0, 0.0], strName="Cube_4", iPartColor=7697908)
JPT.ViewFitToModel()

# Hide some faces
JPT.Exec("Show_Entity([6:52, 6:78], 0)")

# Show all hidden faces
MainWindow.RightClick.ShowAllHiddenFaces()  # [hl]
