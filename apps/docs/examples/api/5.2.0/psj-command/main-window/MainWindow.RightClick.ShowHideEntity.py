# Title:   MainWindow.RightClick.ShowHideEntity()
# Desc:    Show/hide the specified targets
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/main-window/MainWindow.RightClick.ShowHideEntity
# ---
# Prepare the model
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_3", iPartColor=13259210)

# Hide faces
target = MainWindow.RightClick.ShowHideEntity(crlTargets=[Face(26, 52, 78)], bShow=False)  # [hl]
JPT.Debugger(target)

# Show Face(26) only
target = MainWindow.RightClick.ShowHideEntity(crlTargets=[Face(26)], bShow=True)  # [hl]
JPT.Debugger(target)
