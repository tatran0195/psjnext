# Title:   Meshing.CADProjection.Part()
# Desc:    Project nodes of the meshed part to the selected CAD (Reference) part.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/meshing/Meshing.CADProjection.Part
# ---
cyl=Geometry.Part.Cylinder()

Meshing.SetMeshAttribute(crlParts=[cyl],
                         surfaceMesh=SURFACE_MESH(dMinElemSize=0.0005,
                                                  dGeomAngle=0.7853981634,
                                                  dGeomMinSize=0.0005,
                                                  iPerformanceMode=1,
                                                  dAutoMergeTinyFacesAngle=0.5235987756,
                                                  bGeomApprox=True,
                                                  iNextEntityOffsetId=0))

Meshing.SurfaceMeshing(crlParts=[cyl],
                       surfaceMesh=SURFACE_MESH(dMinElemSize=0.0005,
                                                dGeomAngle=0.7853981634,
                                                dGeomMinSize=0.0005,
                                                iPerformanceMode=1,
                                                dAutoMergeTinyFacesAngle=0.5235987756,
                                                bGeomApprox=True,
                                                iNextEntityOffsetId=0),
                       iThreadNum=4)

Meshing.SolidMeshing(crlParts=[cyl],
                     bTet10=True,
                     dGradingFactor=1.05,
                     dStretchLimit=0.1,
                     iSpeedVsQual=1,
                     iRegion=1,
                     bSafeMode=False,
                     iParallel=4,
                     bInternalMeshOnly=False,
                     iPartColor=65280)

Meshing.CADProjection.Part(crCadPart=RefPart((1,1)),  # [hl]
                           crMeshedPart=cyl,  # [hl]
                           bProjectCornerNodes=True)  # [hl]
