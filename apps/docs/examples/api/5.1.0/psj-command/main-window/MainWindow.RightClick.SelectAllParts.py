# Title:   MainWindow.RightClick.SelectAllParts()
# Desc:    Select all parts in the current document
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/main-window/MainWindow.RightClick.SelectAllParts
# ---
# Prepare models
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_3", iPartColor=13259210)
Geometry.Part.Cube(dlOrigin=[0.03, 0.0, 0.0], strName="Cube_4", iPartColor=7697908)
JPT.Exec("View Fit To Model()")

# Select all parts
listParts = MainWindow.RightClick.SelectAllParts()  # [hl]
print(listParts)
