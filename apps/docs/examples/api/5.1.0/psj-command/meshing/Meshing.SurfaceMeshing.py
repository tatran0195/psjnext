# Title:   Meshing.SurfaceMeshing()
# Desc:    Do 2D meshing for the selected parts. The Meshing.SetMeshAttribute function will be used as input parameters
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/meshing/Meshing.SurfaceMeshing
# ---
Geometry.Part.Cube()
Meshing.SetMeshAttribute(crlParts=[Part(1)], 
                         surfaceMesh=SURFACE_MESH(dGeomAngle=0.7853981634,
                                                  iOptLevel=5, 
                                                  dAutoMergeTinyFacesAngle=0.5235987756, 
                                                  bGeomApprox=True, 
                                                  iNextEntityOffsetId=0))

meshing_status = Meshing.SurfaceMeshing(crlParts=[Part(1)],   # [hl]
                                        surfaceMesh=SURFACE_MESH(dGeomAngle=0.7853981634,  # [hl]
                                                                 iOptLevel=5,   # [hl]
                                                                 dAutoMergeTinyFacesAngle=0.5235987756,   # [hl]
                                                                 bGeomApprox=True,   # [hl]
                                                                 iNextEntityOffsetId=0))  # [hl]

JPT.Debugger(meshing_status)
