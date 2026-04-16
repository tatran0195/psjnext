# Title:   Meshing.CADProjection.NodeToEdge()
# Desc:    Project nodes of the meshed faces to the selected CAD (Reference) edges
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/meshing/Meshing.CADProjection.NodeToEdge
# ---
Geometry.Part.Cylinder(iPartColor=12603072)

Meshing.SetMeshAttribute(crlParts=[Part(1)],
                         surfaceMesh=SURFACE_MESH(dAvgElemSize=0.004,
                                                  dMaxElemSize=0.015,
                                                  dMinElemSize=0.0005,
                                                  dGeomAngle=0.7853981634,
                                                  dGeomMinSize=0.0005,
                                                  dMinStretchVal=0.0,
                                                  iPerformanceMode=1,
                                                  dAutoMergeTinyFacesAngle=0.5235987756,
                                                  bGeomApprox=True,
                                                  iNextEntityOffsetId=0))

Meshing.SurfaceMeshing(crlParts=[Part(1)],
                       surfaceMesh=SURFACE_MESH(dAvgElemSize=0.004,
                                                dMaxElemSize=0.015,
                                                dMinElemSize=0.0005,
                                                dGeomAngle=0.7853981634,
                                                dGeomMinSize=0.0005,
                                                dMinStretchVal=0.0,
                                                iPerformanceMode=1,
                                                dAutoMergeTinyFacesAngle=0.5235987756,
                                                bGeomApprox=True,
                                                iNextEntityOffsetId=0),
                       iThreadNum=4)

Meshing.SolidMeshing(crlParts=[Part(1)],
                     bTet10=True,
                     dGradingFactor=1.05,
                     dStretchLimit=0.1,
                     iSpeedVsQual=1,
                     iRegion=1,
                     bSafeMode=False,
                     iParallel=4,
                     bInternalMeshOnly=False,
                     iPartColor=65280)

targetn=MainWindow.RightClick.AssociatedPick(crlInput=[Edge(1)],
                                             strTarget="Node")

Meshing.CADProjection.NodeToEdge(crCadEdge=RefEdge((1,1)),  # [hl]
                                 crlMeshedNodes=targetn)  # [hl]
