# Title:   MainWindow.RightClick.ShowHideFlip()
# Desc:    Toggle the display of hidden parts or faces on the current document
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/main-window/MainWindow.RightClick.ShowHideFlip
# ---
# Prepare models
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_3", iPartColor=13259210)
Geometry.Part.Cube(dlOrigin=[0.03, 0.0, 0.0], strName="Cube_4", iPartColor=7697908)
JPT.ViewFitToModel()

# Show hide flip parts
flipPart = MainWindow.RightClick.ShowHideFlip(iType=0)  # [hl]
print(flipPart)
