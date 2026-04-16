# Title:   Geometry.AdjustHalfCylinder()
# Desc:    Adjust the split position of the cylinder face (For example, The bolt or bolt hole). By using this function, unevenly meshing caused by the difference of split positions can be avoided
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/geometry/Geometry.AdjustHalfCylinder
# ---
Geometry.Part.Cylinder(strName="Cylinder_4", 
                       iPartColor=13259210)
Geometry.Part.Cylinder(strName="Cylinder_5", 
                       dlOrigin=[0.0, 0.01, 0.0], 
                       dTopOuterRadius=0.005,
                       dBottomOuterRadius=0.005, 
                       iPartColor=7697908)

flag1 = Geometry.AdjustHalfCylinder(poslPoint=[[-2.775557561562891e-16,   # [hl]
                                                0,   # [hl]
                                                -5.551115123125783e-17]],  # [hl]
                                    crlFaces=[Face(5)],   # [hl]
                                    iAxisPlane=2)  # [hl]

JPT.Debugger(flag1)

flag2 = Geometry.AdjustHalfCylinder(poslPoint=[[0,   # [hl]
                                                0.009999999999999898,   # [hl]
                                                6.938893903907228e-18]],  # [hl]
                                    crlFaces=[Face(10)],   # [hl]
                                    iAxisPlane=2)  # [hl]

JPT.Debugger(flag2)
