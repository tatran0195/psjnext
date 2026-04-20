# Title:   MainWindow.RightClick.InverseHideAll()
# Desc:    Hide all targets other than the specified face. (Display only the specified faces)
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/main-window/MainWindow.RightClick.InverseHideAll
# ---
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)
JPT.ViewFitToModel()

# Invert hide Part(1)
target = MainWindow.RightClick.InverseHideAll(crlTargets=[Face(26)])  # [hl]
JPT.Debugger(target)
