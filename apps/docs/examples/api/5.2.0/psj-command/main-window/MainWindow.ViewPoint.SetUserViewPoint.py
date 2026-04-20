# Title:   MainWindow.ViewPoint.SetUserViewPoint()
# Desc:    Set the user ViewPoint
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/main-window/MainWindow.ViewPoint.SetUserViewPoint
# ---
JPT.Exec('ViewReset()')
JPT.Exec('ViewControl_Rotate([0, -60, 0])')
JPT.Exec('ViewControl_SetCenter([0.005, 0.005, 0.005])')
JPT.Exec('AddUserViewPoint("New View Point")')
JPT.Exec('ViewReset()')
MainWindow.ViewPoint.SetUserViewPoint(strName="New View Point")  # [hl]
