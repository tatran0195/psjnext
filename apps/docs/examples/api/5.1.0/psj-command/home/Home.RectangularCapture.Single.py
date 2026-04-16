# Title:   Home.RectangularCapture.Single()
# Desc:    Create a frame for Single capture and save it in the “User Frame” tree of the ViewPoint window. The created frame will be used with the "To PPT" and "To Image" command
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/home/Home.RectangularCapture.Single
# ---
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)

# Create a single frame
Home.RectangularCapture.Single(strFrameName="New_Frame_1 (Single)", iStartPointX=459, iStartPointY=212,   # [hl:start]
                                iWidth=460, iHeight=214)  # [hl:end]
Home.ToPPTX()
