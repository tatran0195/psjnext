# Title:   Assemble.SeparateFaces.Solid()
# Desc:    Separate a shared face between parts into distinct faces
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/assemble/Assemble.SeparateFaces.Solid
# ---
Geometry.Part.Cube(iPartColor=15658599)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=7961077)
Assemble.AssembleFaceEx(ilPairFaceToMakeShareFace=[49, 24], 
                        dTolerance=0.001, 
                        iTypeConnectPos=0)

faces = Assemble.SeparateFaces.Solid(crlParts=[Part(1, 2)],   # [hl]
                                     iCreateGroup=2)  # [hl]
JPT.Debugger(faces)
