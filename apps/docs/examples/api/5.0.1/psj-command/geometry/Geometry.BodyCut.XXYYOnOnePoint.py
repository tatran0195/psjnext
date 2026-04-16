# Title:   Geometry.BodyCut.XXYYOnOnePoint()
# Desc:    Separate a part along the specified coordinate plane with one node as a starting point
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/geometry/Geometry.BodyCut.XXYYOnOnePoint
# ---
Torus = Geometry.Part.Torus(strName="Torus_2", iPartColor=14114775)

separate_status = Geometry.BodyCut.XXYYOnOnePoint(crPart=Torus,   # [hl]
                                                  posCutPoint=[-0.015,  # [hl]
                                                               -0.005,   # [hl]
                                                               0.006],  # [hl]
                                                  iCuttingPlane=1,   # [hl]
                                                  bSharedFace=True,   # [hl]
                                                  bSeparateFace=True)  # [hl]

JPT.Debugger(separate_status)
