# Title:   Meshing.LocalMeshing.SelectFillet()
# Desc:    Select all the existing fillet faces based on the selected entities
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/meshing/Meshing.LocalMeshing.SelectFillet
# ---
Geometry.Part.Cube()
Geometry.MakeFillet(crlEdges=[Edge(18, 19, 15)])

faces = Meshing.LocalMeshing.SelectFillet(crlParts=[Part(1)],   # [hl]
                                          crlFaces=[])  # [hl]
                                        
JPT.Debugger(faces)
