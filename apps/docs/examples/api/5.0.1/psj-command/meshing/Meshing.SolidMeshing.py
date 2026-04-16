# Title:   Meshing.SolidMeshing()
# Desc:    Do 3D meshing (Tetrahedral) for the selected parts
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/meshing/Meshing.SolidMeshing
# ---
Geometry.Part.Cube()

meshing_status = Meshing.SolidMeshing(crlParts=[Part(1)],   # [hl]
                                      bTet10=True,   # [hl]
                                      dGradingFactor=1.05,   # [hl]
                                      dStretchLimit=0.1,  # [hl]
                                      iSpeedVsQual=1,   # [hl]
                                      iRegion=1,   # [hl]
                                      bSafeMode=False,   # [hl]
                                      iParallel=24,   # [hl]
                                      bSurfaceNodes=False,   # [hl]
                                      bEdgeNodes=False,  # [hl]
                                      bInternalMeshOnly=False,  # [hl]
                                      iPartColor=65280)  # [hl]

JPT.Debugger(meshing_status)
