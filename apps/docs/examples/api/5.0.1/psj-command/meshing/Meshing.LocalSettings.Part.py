# Title:   Meshing.LocalSettings.Part()
# Desc:    Set the mesh setting for the selected parts (Define the settings before surface mesh creation)
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/meshing/Meshing.LocalSettings.Part
# ---
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.0, 0.01, 0.0], strName="Cube_2", iPartColor=6409934)

Geometry.Part.Cube()

local_mesh = Meshing.LocalSettings.Part(strName="MeshParam_1",   # [hl]
                                        localMesh=LOCAL_MESH(iEntityType=1,  # [hl]
                                                             bEnableSizeParams=True,   # [hl]
                                                             dAvgElemSize=0.002,   # [hl]
                                                             dMaxElemSize=0.01,   # [hl]
                                                             dMinElemSize=0.001),   # [hl]
                                        crlTargets=[Part(1)])  # [hl]

JPT.Debugger(local_mesh)

MeshEdit.CreateNode.Absolute(veclNodeCoord=[[0.001, 0.001, 0.001]], ilNewNodeID=[977])

local_mesh = Meshing.LocalSettings.Part(strName="MeshParam_2",   # [hl]
                                        localMesh=LOCAL_MESH(iEntityType=10,  # [hl]
                                                             dAvgElemSize=0.002,   # [hl]
                                                             dMaxElemSize=0.01,   # [hl]
                                                             dMinElemSize=0.001),  # [hl]
                                        veclHardPointXYZ=[[0.001,   # [hl]
                                                           0.001,   # [hl]
                                                           0.001]],   # [hl]
                                        crlHardPointTarget=[Part(1)])  # [hl]

JPT.Debugger(local_mesh)

Geometry.FCircVertexAdjust(crlParts=[Part(1, 2)])

Meshing.SetMeshAttribute(crlParts=[Part(1, 2)], 
                         surfaceMesh=SURFACE_MESH(dMaxElemSize=0.015,
                                                  dMinElemSize=0.0005, 
                                                  dGeomAngle=0.7853981634, 
                                                  dGeomMinSize=0.0005, 
                                                  dMinStretchVal=0.0, 
                                                  iPerformanceMode=1,
                                                  dAutoMergeTinyFacesAngle=0.5235987756, 
                                                  bGeomApprox=True, 
                                                  iNextEntityOffsetId=0))

Meshing.SurfaceMeshing(crlParts=[Part(1, 2)], 
                       surfaceMesh=SURFACE_MESH(dMaxElemSize=0.015, 
                                                dMinElemSize=0.0005,
                                                dGeomAngle=0.7853981634, 
                                                dGeomMinSize=0.0005, 
                                                dMinStretchVal=0.0, 
                                                iPerformanceMode=1,
                                                dAutoMergeTinyFacesAngle=0.5235987756, 
                                                bGeomApprox=True, 
                                                iNextEntityOffsetId=0), 
                       iThreadNum=4)

Meshing.SolidMeshing(crlParts=[Part(1, 2)], 
                     bTet10=True, 
                     dGradingFactor=1.05, 
                     dStretchLimit=0.1,
                     iSpeedVsQual=1, 
                     iRegion=1, 
                     bSafeMode=False, 
                     iParallel=4, 
                     bInternalMeshOnly=False, 
                     iPartColor=65280)
