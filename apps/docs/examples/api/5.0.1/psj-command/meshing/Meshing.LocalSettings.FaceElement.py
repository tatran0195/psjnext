# Title:   Meshing.LocalSettings.FaceElement()
# Desc:    Set the mesh setting for the selected elements (Define the settings before surface mesh creation)
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/meshing/Meshing.LocalSettings.FaceElement
# ---
Geometry.Part.Cube()

created_local_mesh_setting = Meshing.LocalSettings.FaceElement(strName="MeshParam_1",   # [hl]
                                                               localMesh=LOCAL_MESH(iEntityType=2,  # [hl]
                                                                                    bEnableSizeParams=True,   # [hl]
                                                                                    dAvgElemSize=0.005,   # [hl]
                                                                                    dMaxElemSize=0.01,   # [hl]
                                                                                    dMinElemSize=0.001),   # [hl]
                                                               crlTargets=[Elem(970)])  # [hl]

JPT.Debugger(created_local_mesh_setting)
