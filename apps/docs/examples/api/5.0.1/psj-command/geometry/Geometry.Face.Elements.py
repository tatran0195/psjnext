# Title:   Geometry.Face.Elements()
# Desc:    Create faces from the selected elements
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/geometry/Geometry.Face.Elements
# ---
Geometry.Part.Cube()

faces = Geometry.Face.Elements(crlElems=[Elem(1008,  # [hl]
                                              1007,  # [hl]
                                              989,  # [hl]
                                              990,  # [hl]
                                              1005,  # [hl]
                                              1006,  # [hl]
                                              988,  # [hl]
                                              987)])  # [hl]

JPT.Debugger(faces)
