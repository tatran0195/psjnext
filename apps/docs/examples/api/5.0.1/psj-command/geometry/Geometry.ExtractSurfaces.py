# Title:   Geometry.ExtractSurfaces()
# Desc:    Create a new part by recursively finding adjacent surfaces are at an angle of less than or equal to the specified angle
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/geometry/Geometry.ExtractSurfaces
# ---
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.011, 0.0, 0.0],
                   strName="Cube_2",
                   iPartColor=6409934)
bodies = Geometry.ExtractSurfaces([Face(52, 26)],  # [hl]
                                  dFaceAngle=-1.0,  # [hl]
                                  strName="ExtractFace_4",  # [hl]
                                  bMergePart=True)  # [hl]
JPT.Debugger(bodies)
