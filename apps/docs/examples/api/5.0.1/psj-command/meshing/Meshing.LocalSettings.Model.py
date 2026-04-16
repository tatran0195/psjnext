# Title:   Meshing.LocalSettings.Model()
# Desc:    Set the mesh setting for the whole model (Define the settings before surface mesh creation)
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/meshing/Meshing.LocalSettings.Model
# ---
Geometry.Part.Cube()

Meshing.LocalSetting.SearchTargetFaces(dlLength=[0.003, 0.003, 0.003],
                                       dlAxisPt1=[0.0, 0.0, 0.01],
                                       dlAxisPt2=[0.005, 0.0, 0.0])

created_local_mesh_setting = Meshing.LocalSettings.Model(strName="MeshParam_1",  # [hl]
                                                         localMesh=LOCAL_MESH(iEntityType=11,  # [hl]
                                                                              bEnableSizeParams=True,  # [hl]
                                                                              dAvgElemSize=0.001,  # [hl]
                                                                              dMaxElemSize=0.01,  # [hl]
                                                                              dMinElemSize=0.0005,  # [hl]
                                                                              dTrimAngle=0.7853981634),  # [hl]
                                                         spaceMesh=SPACE_MESH(vLength=[0.003, 0.003, 0.003],  # [hl]
                                                                              vAxisPt2=[0.005, 0.0, 0.0],  # [hl]
                                                                              dMinElemSize=0.001),  # [hl]
                                                         crlTargets=[Face(21, 23, 25)])  # [hl]

JPT.Debugger(created_local_mesh_setting)
