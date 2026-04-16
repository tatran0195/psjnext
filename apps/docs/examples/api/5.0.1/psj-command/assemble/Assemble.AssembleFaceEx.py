# Title:   Assemble.AssembleFaceEx()
# Desc:    Make assemble faces (shared faces). User inputs the pair faces output from Assemble.FindMatingFaceEx() function, then it will return a list of new shared faces ID created.
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/assemble/Assemble.AssembleFaceEx
# ---
cube1 = Geometry.Part.Cube()
cube2 = Geometry.Part.Cube(dlOrigin=[0.011, 0.0, 0.0], 
                           strName="Cube_2", 
                           iPartColor=6409934)

pair_faces = Assemble.FindMatingFaceEx(crlTaBodies=[cube1, cube2], 
                                       dMatingTol=0.001)

share_faces = Assemble.AssembleFaceEx(ilPairFaceToMakeShareFace = pair_faces,   # [hl]
                                      dTolerance=0.001,  # [hl]
                                      iTypeConnectPos=0,   # [hl]
                                      bFitEdge=True)  # [hl]

JPT.Debugger(share_faces)
