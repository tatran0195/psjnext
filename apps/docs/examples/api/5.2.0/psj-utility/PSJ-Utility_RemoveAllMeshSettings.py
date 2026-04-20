# Title:   JPT.RemoveAllMeshSettings()
# Desc:    Remove all the existing local mesh settings
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_RemoveAllMeshSettings
# ---
# Prepare model
Geometry.Part.Cube(iPartColor=5688524)
Meshing.LocalSettings.Face(strName="MeshParam_1",
                           localMesh=LOCAL_MESH(iEntityType=2,
                                                bEnableSizeParams=True,
                                                dAvgElemSize=0.005,
                                                dMaxElemSize=0.01,
                                                dMinElemSize=0.001,
                                                bEnableMeshPattern=True,
                                                iMeshPatternType=1),
                           crlTargets=[Face(26)])
Meshing.LocalSettings.Edge(strName="MeshParam_2",
                           localMesh=LOCAL_MESH(iEntityType=3,
                                                dAvgElemSize=0.005,
                                                dMaxElemSize=0.01,
                                                dMinElemSize=0.001,
                                                dTrimAngle=0.7853981634,
                                                bEnableMeshCount=True,
                                                iNodeCount=1),
                           crlTargets=[Edge(18, 17, 19)])
Meshing.LocalSettings.Part(strName="MeshParam_3",
                           localMesh=LOCAL_MESH(iEntityType=1,
                                                bEnableSizeParams=True,
                                                dAvgElemSize=0.005,
                                                dMaxElemSize=0.01,
                                                dMinElemSize=0.001),
                           crlTargets=[Part(1)])

# Delete all the created local meshing
JPT.RemoveAllMeshSettings()  # [hl]
