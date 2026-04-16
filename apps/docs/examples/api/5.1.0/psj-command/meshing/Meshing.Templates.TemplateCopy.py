# Title:   Meshing.Templates.TemplateCopy()
# Desc:    Copy local mesh setting from one to another
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/meshing/Meshing.Templates.TemplateCopy
# ---
Geometry.Part.Cube(iPartColor=12999622)
Geometry.MakeFillet(crlEdges=[Edge(18, 19, 15)])
Meshing.LocalSettings.Face(strName="MeshParam_1",
                           localMesh=LOCAL_MESH(iEntityType=2,
                                                bEnableSizeParams=True,
                                                dAvgElemSize=0.002,
                                                dMaxElemSize=0.01,
                                                dMinElemSize=0.001,
                                                bEnableMeshPattern=True,
                                                iMeshPatternType=1),
                           crlTargets=[Face(27, 28, 29)])

Geometry.Part.Cube(strName="Cube_2", iPartColor=7731705)
Geometry.MakeFillet(crlEdges=[Edge(93, 90, 94)])

copy_status = Meshing.Templates.TemplateCopy(crlReferent=[Part(1)],  # [hl]
                                             crlTargets=[Part(2)],  # [hl]
                                             dTolerance=1e-06)  # [hl]

JPT.Debugger(copy_status)
