# Title:   MainWindow.RightClick.SelectSurfaceColor()
# Desc:    Select faces that have the same color as the selected face.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/main-window/MainWindow.RightClick.SelectSurfaceColor
# ---
#Prepare Model
Geometry.Part.Cube(
    iPartColor=6409934
    )

Geometry.Part.Cube( 
    dlOrigin=[0.02, 0.0, 0.0], 
    strName="Cube_2", 
    iPartColor=7434735
    )

# Change the color of the specified face (Face 21)
Assembly.RightClick.ChangeEntityColor(
    crlEntities=[Face(48, 50, 47, 21, 23, 22)], 
    iColor=16776960
    )

#Get faces with the same color as Face 21 in the entire model.  # [hl:start]
blue_faces = MainWindow.RightClick.SelectSurfaceColor(
    crFace=Face(21), 
    bSelectFacesInSamePart=False
    )  # [hl:end]
JPT.Debugger(blue_faces)

#Get faces with the same color as Face 21 within its part.  # [hl:start]
blue_faces_in_cube_1 = MainWindow.RightClick.SelectSurfaceColor(
    crFace=Face(21), 
    bSelectFacesInSamePart=True  # [hl:end]
    )
JPT.Debugger(blue_faces_in_cube_1)
