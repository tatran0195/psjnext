# Title:   MainWindow.RightClick.InverseHide()
# Desc:    Invert hide targets by context menu
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/main-window/MainWindow.RightClick.InverseHide
# ---
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)
JPT.ViewFitToModel()

# Invert hide Part(1)
target = MainWindow.RightClick.InverseHide(crlTargets=[Part(1)])  # [hl]
JPT.Debugger(target)
