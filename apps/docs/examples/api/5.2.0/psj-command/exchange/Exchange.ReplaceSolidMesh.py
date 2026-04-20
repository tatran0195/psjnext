# Title:   Exchange.ReplaceSolidMesh()
# Desc:    Replace an adjacent solid part.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/exchange/Exchange.ReplaceSolidMesh
# ---
Geometry.Part.Cube(iPartColor=6409934)
Geometry.Part.Cube(
    dlOrigin=[0.01, 0.0, 0.0],
    ilAxialNodes=[4, 4, 4],
    strName="Cube_3",
    iPartColor=12867524)

Meshing.SolidMeshing(crlParts=[Part(1,2)],
    bTet10=True,
    dGradingFactor=1.05,
    dStretchLimit=0.1,
    iSpeedVsQual=1,
    iRegion=1,
    bSafeMode=False,
    iParallel=16,
    bInternalMeshOnly=False,
    iPartColor=65280)

ret=Exchange.ReplaceSolidMesh(  # [hl:start]
    crlSourceFace=[Face(24)],
    crlTargetFace=[Face(49)],
    dTolerance=0.0005)  # [hl:end]
print(ret)
