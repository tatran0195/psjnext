# Title:   Geometry.BodyCut.By3Points()
# Desc:    Separate a part using the given cutting planes defined by three points to partition the target parts
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/geometry/Geometry.BodyCut.By3Points
# ---
part = Geometry.Part.Torus(strName="Torus_2", iPartColor=14114775)

cutting_status = Geometry.BodyCut.By3Points(crPart=part,   # [hl]
                                            poslPoints=[[-0.038, -0.019, 0.017],  # [hl]
                                                        [-0.019, -0.010, 0.015],   # [hl]
                                                        [0.048, 0.022, -0.006]],   # [hl]
                                            bSharedFace=True,   # [hl]
                                            bSeparateFace=True)  # [hl]

JPT.Debugger(cutting_status)
