# Title:   Meshing.GridMesh()
# Desc:    Create a mesh with grid pattern for the selected faces
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/meshing/Meshing.GridMesh
# ---
Geometry.Part.Cube(strName="Cube_2", iPartColor=5820248)
Geometry.MakeFillet(crlEdges=[Edge(18, 19, 15)])

meshed_status = Meshing.GridMesh(listGridMesh=[GRID_MESH(crlFace=[Face(29)],  # [hl:start]
                                                         crlCorner=[Node(1838,
                                                                         1837,
                                                                         1387,
                                                                         1397)],
                                                         ilMeshCount=[3, 3],
                                                         iShape=4),
                                               GRID_MESH(crlFace=[Face(27)],
                                                         crlCorner=[Node(1837,
                                                                         1836,
                                                                         489,
                                                                         499)],
                                                         ilMeshCount=[3, 3],
                                                         iShape=4),
                                               GRID_MESH(crlFace=[Face(28)],
                                                         crlCorner=[Node(1386,
                                                                         1376,
                                                                         1836,
                                                                         1838)],
                                                         ilMeshCount=[3, 3],
                                                         iShape=4),
                                               GRID_MESH(crlFace=[Face(30)],
                                                         crlCorner=[Node(1837,
                                                                         1838,
                                                                         1836)],
                                                         ilMeshCount=[3],
                                                         iShape=3)],
                                 bProjectToCad=True,
                                 strGroupName="GridMeshFace")  # [hl:end]

JPT.Debugger(meshed_status)
