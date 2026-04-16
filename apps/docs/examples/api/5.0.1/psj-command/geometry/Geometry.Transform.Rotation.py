# Title:   Geometry.Transform.Rotation()
# Desc:    Rotate given parts by the specified angle
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/geometry/Geometry.Transform.Rotation
# ---
Geometry.Part.Cube()

rotate_status = Geometry.Transform.Rotation(crlParts=[Part(1)],   # [hl]
                                            vecAxis=[0.0, 0.001, 0.0],  # [hl]
                                            dAngle=0.5,  # [hl]
                                            bCreateNewPart=True,   # [hl]
                                            iCopyCount=3,  # [hl]
                                            dTol=1e-05)  # [hl]

JPT.Debugger(rotate_status)
