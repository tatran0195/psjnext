# Title:   Meshing.SetMeshAttribute()
# Desc:    Set mesh attribute for the selected part
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/meshing/Meshing.SetMeshAttribute
# ---
Geometry.Part.Cube()

Geometry.FCircleAdjustVertex(crlParts=[Part(1)])

mesh_attribute = Meshing.SetMeshAttribute(crlParts=[Part(1)],   # [hl]
                                          surfaceMesh=SURFACE_MESH(dAvgElemSize=0.004,  # [hl]
                                                                   dMaxElemSize=0.015,   # [hl]
                                                                   dMinElemSize=0.0005,   # [hl]
                                                                   dGeomAngle=0.7853981634,   # [hl]
                                                                   dGeomMinSize=0.0005,  # [hl]
                                                                   dMinStretchVal=0.0,   # [hl]
                                                                   iPerformanceMode=1,   # [hl]
                                                                   dAutoMergeTinyFacesAngle=0.5235987756,   # [hl]
                                                                   bGeomApprox=True,  # [hl]
                                                                   iNextEntityOffsetId=0))  # [hl]

JPT.Debugger(mesh_attribute)

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
