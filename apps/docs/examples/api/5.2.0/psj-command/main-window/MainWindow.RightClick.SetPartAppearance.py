# Title:   MainWindow.RightClick.SetPartAppearance()
# Desc:    Set the appearance of the selected parts
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/main-window/MainWindow.RightClick.SetPartAppearance
# ---
# Prepare model
JPT.Exec('ViewShowMesh(1)')
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_3", iPartColor=13259210)
Geometry.Part.Cube(dlOrigin=[0.03, 0.0, 0.0], strName="Cube_4", iPartColor=7697908)

MainWindow.RightClick.SetPartAppearance(crlParts=[Part(1)], strType="Surface", bShow=False)  # [hl:start]
MainWindow.RightClick.SetPartAppearance(crlParts=[Part(2)], strType="Edge", bShow=False)
MainWindow.RightClick.SetPartAppearance(crlParts=[Part(3)], strType="Mesh", bShow=False)
MainWindow.RightClick.SetPartAppearance(crlParts=[Part(4)], strType="Node", bShow=False)
MainWindow.RightClick.SetPartAppearance(crlParts=[Part(4)], strType="Surface", bShow=False)
MainWindow.RightClick.SetPartAppearance(crlParts=[Part(4)], strType="Mesh", bShow=False)  # [hl:end]

JPT.ViewFitToModel()

