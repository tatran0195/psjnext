# Title:   Meshing.LocalSettings.Edge()
# Desc:    Set the mesh setting for the selected edges (Define the settings before surface mesh creation)
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/meshing/Meshing.LocalSettings.Edge
# ---
Geometry.Part.Cube()

local_mesh = Meshing.LocalSettings.Edge(strName="MeshParam_1",   # [hl]
                                        localMesh=LOCAL_MESH(iEntityType=3,   # [hl]
                                                             dAvgElemSize=0.005,   # [hl]
                                                             dMaxElemSize=0.01,   # [hl]
                                                             dMinElemSize=0.001,   # [hl]
                                                             dTrimAngle=0.7853981634,   # [hl]
                                                             bEnableMeshCount=True,   # [hl]
                                                             iNodeCount=8),   # [hl]
                                        crlTargets=[Edge(18)])  # [hl]

JPT.Debugger(local_mesh)

Geometry.FCircVertexAdjust(crlParts=[Part(1)])

Meshing.SetMeshAttribute(crlParts=[Part(1)], 
                         surfaceMesh=SURFACE_MESH(dMaxElemSize=0.015, 
                                                  dMinElemSize=0.0005,
                                                  dGeomAngle=0.7853981634, 
                                                  dGeomMinSize=0.0005, 
                                                  dMinStretchVal=0.0, 
                                                  iPerformanceMode=1, 
                                                  dAutoMergeTinyFacesAngle=0.5235987756,
                                                  bGeomApprox=True, 
                                                  iNextEntityOffsetId=0))

Meshing.SurfaceMeshing(crlParts=[Part(1)], 
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
