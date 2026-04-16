# Title:   Assembly.RightClick.RestoreOriginalPart()
# Desc:    Replace the current part by using its reference. In case the number of reference = 0, it will keep the current part without changing anything
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/assembly/Assembly.RightClick.RestoreOriginalPart
# ---
Geometry.Part.Cube()
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

restore_status = Assembly.RightClick.RestoreOriginalPart(crlBodies=[Part(1)])  # [hl]

JPT.Debugger(restore_status)
