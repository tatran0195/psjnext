# Title:   MainWindow.RightClick.SelectByFace()
# Desc:    Select all targets in the same plane as the selected targets
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/main-window/MainWindow.RightClick.SelectByFace
# ---
# Prepare models
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_3", iPartColor=13259210)
JPT.ViewFitToModel()
Assemble.AssembleFaceEx(ilPairFaceToMakeShareFace=[49, 24, 50, 75], dTolerance=0.0001, \
                        iTypeConnectPos=0, bFitEdge=True)

# Select all faces in the same plane as the specified face
listFaces = MainWindow.RightClick.SelectByFace(iTargetType=3, crlTargets=[Face(26)])  # [hl]
if listFaces is None:
    print("There is no selected faces")
elif len(listFaces) == 1:
    print("One face was selected")
    print(listFaces)
else:
    print(str(len(listFaces)) + " faces were selected")
    print(listFaces)
