# Title:   Meshing.CADProjection.NodeToFace()
# Desc:    Project nodes to the selected CAD (Reference) faces
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/meshing/Meshing.CADProjection.NodeToFace
# ---
Geometry.Part.Cylinder(iPartColor=15658599)

Meshing.SetMeshAttribute(crlParts=[Part(1)],
                         surfaceMesh=SURFACE_MESH(dGeomAngle=0.7853981634,
                                                  iPerformanceMode=1,
                                                  dAutoMergeTinyFacesAngle=0.5235987756,
                                                  bGeomApprox=True,
                                                  iNextEntityOffsetId=0))

Meshing.SurfaceMeshing(crlParts=[Part(1)],
                       surfaceMesh=SURFACE_MESH(dGeomAngle=0.7853981634,
                                                iPerformanceMode=1,
                                                dAutoMergeTinyFacesAngle=0.5235987756,
                                                bGeomApprox=True,
                                                iNextEntityOffsetId=0))

Meshing.SolidMeshing(crlParts=[Part(1)],
                     bTet10=True,
                     dGradingFactor=1.05,
                     dStretchLimit=0.1,
                     iSpeedVsQual=1,
                     iRegion=1,
                     bSafeMode=False,
                     iParallel=8,
                     bInternalMeshOnly=False,
                     iPartColor=65280)

Meshing.CADProjection.NodeToFace(crlCadFaces=[RefFace((5,5))],  # [hl]
                                 crlMeshedNodes=[Node(691)])  # [hl]
