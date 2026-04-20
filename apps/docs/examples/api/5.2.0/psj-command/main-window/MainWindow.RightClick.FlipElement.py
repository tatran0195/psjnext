# Title:   MainWindow.RightClick.FlipElement()
# Desc:    Flip normal of surface.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/main-window/MainWindow.RightClick.FlipElement
# ---
Geometry.Part.Cube()
MainWindow.RightClick.FlipElement(crlTargets=[Face(21, 23, 26)])  # [hl:start]
MainWindow.RightClick.FlipElement(crlTargets=[Elem(1009, 1025, 968)])  # [hl:end]
