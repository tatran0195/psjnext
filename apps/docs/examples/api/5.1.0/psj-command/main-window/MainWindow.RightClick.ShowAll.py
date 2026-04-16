# Title:   MainWindow.RightClick.ShowAll()
# Desc:    Show all hidden entities
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/main-window/MainWindow.RightClick.ShowAll
# ---
# Prepare models
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_3", iPartColor=13259210)
Geometry.Part.Cube(dlOrigin=[0.03, 0.0, 0.0], strName="Cube_4", iPartColor=7697908)
JPT.ViewFitToModel()

# Hide some parts
JPT.Exec("Show_Entity([3:2, 3:3], 0)")
# Show all parts again
MainWindow.RightClick.ShowAll()  # [hl]
