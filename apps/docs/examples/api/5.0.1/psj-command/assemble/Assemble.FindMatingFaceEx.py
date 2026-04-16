# Title:   Assemble.FindMatingFaceEx()
# Desc:    Find the mating faces which can be used in Assemble.AssembleFaceEx() function
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/assemble/Assemble.FindMatingFaceEx
# ---
cube1 = Geometry.Part.Cube()
cube2 = Geometry.Part.Cube(dlOrigin=[0.011, 0.0, 0.0], 
                           strName="Cube_2", 
                           iPartColor=6409934)

pair_faces = Assemble.FindMatingFaceEx(crlTaBodies=[cube1, cube2],   # [hl]
                                      dMatingTol=0.001)  # [hl]

JPT.Debugger(pair_faces)
