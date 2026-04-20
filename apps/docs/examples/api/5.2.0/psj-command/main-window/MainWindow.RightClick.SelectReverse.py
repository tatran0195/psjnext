# Title:   MainWindow.RightClick.SelectReverse()
# Desc:    Reverse the selection on the displaying bodies.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/main-window/MainWindow.RightClick.SelectReverse
# ---
# Prepare models
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_3", iPartColor=13259210)
JPT.ViewFitToModel()

# Revert selection from Face(26)
revertFaces = MainWindow.RightClick.SelectReverse(iTargetType=3, crlTargets=[Face(26)])  # [hl]
print(revertFaces)
