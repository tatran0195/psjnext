# Title:   Meshing.LocalRemesh.Surface()
# Desc:    Remesh the selected faces
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/meshing/Meshing.LocalRemesh.Surface
# ---
Geometry.Part.Cube()

creating_status = Meshing.LocalRemesh.Surface(crlTargets=[Face(26)],   # [hl]
                                              surfaceMesh=SURFACE_MESH(dAvgElemSize=0.0005,  # [hl]
                                                                       dMaxElemSize=0.001,   # [hl]
                                                                       dMinElemSize=0.0001,   # [hl]
                                                                       dGeomAngle=0.7853981853,   # [hl]
                                                                       iPerformanceMode=1,  # [hl]
                                                                       dAutoMergeTinyFacesAngle=0.5235987902,   # [hl]
                                                                       bLocalRemesh=True,   # [hl]
                                                                       iNextEntityOffsetId=8985,   # [hl]
                                                                       iNextElemOffsetId=2601),  # [hl]
                                              bGrading=True,   # [hl]
                                              iOverrideType=0)  # [hl]

JPT.Debugger(creating_status)
