# Title:   MainWindow.RightClick.AssociatedPick()
# Desc:    pick associated entity
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/main-window/MainWindow.RightClick.AssociatedPick
# ---
Geometry.Part.Cube()
connectFace=MainWindow.RightClick.AssociatedPick(crlInput=[Node(1)], strTarget="Face")  # [hl]
JPT.Debugger(connectFace)
