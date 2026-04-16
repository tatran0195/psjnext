# Title:   Geometry.ExtractRefSurface()
# Desc:    Create a new part by recursively finding adjacent surfaces that are at an angle of less than or equal to the specified angle
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/geometry/Geometry.ExtractRefSurface
# ---
cube1 = Geometry.Part.Cube()

cube2 = Geometry.Part.Cube(dlOrigin=[0.011, 0.0, 0.0], 
                           strName="Cube_2", 
                           iPartColor=6409934)

Assembly.RightClick.AddToReference(crSrcPart=cube1, 
                                   crDestPart=cube1)

Assembly.RightClick.AddToReference(crSrcPart=cube2, 
                                   crDestPart=cube2)

created_part = Geometry.ExtractRefSurfaces(crlRefFaces=[RefFace((52,   # [hl]
                                                                 26))],   # [hl]
                                           dFaceAngle=-1.0,   # [hl]
                                           strName="ExtractFace_3",  # [hl]
                                           bIsMergePart=True)  # [hl]

JPT.Debugger(created_part)
