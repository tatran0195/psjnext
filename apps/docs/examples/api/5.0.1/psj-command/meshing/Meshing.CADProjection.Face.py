# Title:   Meshing.CADProjection.Face()
# Desc:    Project nodes of the meshed faces to the selected CAD (Reference) part
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/meshing/Meshing.CADProjection.Face
# ---
Geometry.Part.Cylinder()
Geometry.Part.Cylinder(dlOrigin=[0.0, 0.0, 0.02], strName="Cylinder_2", iPartColor=6409934)

Geometry.FCircVertexAdjust(crlParts=[Part(1, 2)])
Meshing.SetMeshAttribute(crlParts=[Part(1, 2)],
                         surfaceMesh=SURFACE_MESH(dMaxElemSize=0.015,
                                                  dMinElemSize=0.0005,
                                                  dGeomAngle=0.7853981634,
                                                  dMinStretchVal=0.0,
                                                  iPerformanceMode=1,
                                                  dAutoMergeTinyFacesAngle=0.5235987756,
                                                  bGeomApprox=True,
                                                  iNextEntityOffsetId=0))

Meshing.SurfaceMeshing(crlParts=[Part(1, 2)],
                       surfaceMesh=SURFACE_MESH(dMaxElemSize=0.015,
                                                dMinElemSize=0.0005,
                                                dGeomAngle=0.7853981634,
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

Meshing.CADProjection.Face(crCadPart=RefPart((2, 2)),  # [hl]
                           crlMeshedFaces=[Face(10)],  # [hl]
                           bProjectMidNodes=True,  # [hl]
                           bIDcheck=True)  # [hl]
