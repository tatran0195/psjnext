# Title:   MainWindow.RightClick.SelectByAttached()
# Desc:    Select all attachments from the specified targets
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/main-window/MainWindow.RightClick.SelectByAttached
# ---
# Prepare models
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_3", iPartColor=13259210)
JPT.ViewFitToModel()

# Select on displaying faces  
attachFaces = MainWindow.RightClick.SelectByAttached(iTargetType=3, crlTargets=[Face(26)])  # [hl]
if attachFaces is None:
    print("There is no selected face")
elif len(attachFaces) == 1:
    print("One face was selected")
    print(attachFaces)
else:
    print(str(len(attachFaces)) + " faces were selected")
    print(attachFaces)
