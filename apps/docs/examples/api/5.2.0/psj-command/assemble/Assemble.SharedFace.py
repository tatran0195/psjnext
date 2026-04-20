# Title:   Assemble.SharedFace()
# Desc:    Create an assembled face/shared face group
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/assemble/Assemble.SharedFace
# ---
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=15658599)
Geometry.Part.Cube(dlOrigin=[0.01, 0.01, 0.0], 
                   strName="Cube_3", 
                   iPartColor=14903267)

Assemble.FindMatingFaceEx(crlTaBodies=[Part(1, 
                                            2, 
                                            3)], 
                          dMatingTol=0.000222222)
Assemble.AssembleFaceEx(ilPairFaceToMakeShareFace=[48, 
                                                   73, 
                                                   49, 
                                                   24], 
                        dTolerance=0.000222222, 
                        iTypeConnectPos=0, 
                        bFitEdge=True)

created_shared_faces = Assemble.SharedFace()  # [hl]

JPT.Debugger(created_shared_faces)
