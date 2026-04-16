# Title:   Assemble.SeparateFaces.AllSharedNodes()
# Desc:    Separate all shared nodes existing on the current model (Also separate all the existing shared faces)
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/assemble/Assemble.SeparateFaces.AllSharedNodes
# ---
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=6409934)

Assemble.FindMatingFaceEx(crlTaBodies=[Part(1, 2)], 
                          dMatingTol=0.000222222)
Assemble.AssembleFaceEx(ilPairFaceToMakeShareFace=[49, 24], 
                        dTolerance=0.000222222, 
                        iTypeConnectPos=0, 
                        bFitEdge=True)

separate_nodes = Assemble.SeparateFaces.AllSharedNodes()  # [hl]

JPT.Debugger(separate_nodes)
