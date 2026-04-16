# Title:   Geometry.BodyCut.BySurface()
# Desc:    Separate a part using the given cutting planes (By selecting face) to partition the target parts
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/geometry/Geometry.BodyCut.BySurface
# ---
Geometry.Part.Cube()
Geometry.Part.Cylinder(dlOrigin=[0.005, -0.002, 0.005], 
                       dTopOuterRadius=0.002,
                       dBottomOuterRadius=0.002, 
                       dHeight=0.014)

Geometry.DeleteEntity.Face(crlFaces=[Face(29, 30)])

separated_bodies = Geometry.BodyCut.BySurface(crlParts=[Part(1)],   # [hl]
                                              crCutter=Part(2),   # [hl]
                                              bSharedFace=True)  # [hl]

JPT.Debugger(separated_bodies)
