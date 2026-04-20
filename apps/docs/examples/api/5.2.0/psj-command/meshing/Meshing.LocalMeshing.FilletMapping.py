# Title:   Meshing.LocalMeshing.FilletMapping()
# Desc:    Select and mesh all the existing fillet faces
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/meshing/Meshing.LocalMeshing.FilletMapping
# ---
Geometry.Part.Cube()
Geometry.MakeFillet(crlEdges=[Edge(18, 19, 15)])

fillet_faces = Meshing.LocalMeshing.SelectFillet(crlParts=[Part(1)], 
                                                 crlFaces=[])

fillet_meshing = \
Meshing.LocalMeshing.FilletMapping(crlFaces=[Face(*[int(str(_).split(":")[-1].strip())   # [hl]
                                                    for _ in fillet_faces])])  # [hl]

JPT.Debugger(fillet_meshing)
