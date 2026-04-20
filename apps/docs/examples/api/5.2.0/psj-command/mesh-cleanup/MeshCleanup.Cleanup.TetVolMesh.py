# Title:   MeshCleanup.Cleanup.TetVolMesh()
# Desc:    Command for cleaning tetrahedral mesh by Metric:Volume.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/mesh-cleanup/MeshCleanup.Cleanup.TetVolMesh
# ---
Geometry.Part.Cube(
  ilAxialNodes=[3, 3, 3],
  iPartColor=7463537
)

MeshEdit.MoveNode.CADFollows(
  crlNodes=[Node(15)],
  dMovedPosX=10.0,
  dMovedPosY=10.0,
  dMovedPosZ=9.60758
)

Meshing.SolidMeshing(
  crlParts=[Part(1)],
  dGradingFactor=1.05,
  iSpeedVsQual=1,
  iRegion=1,
  bSafeMode=False,
  iParallel=16,
  bInternalMeshOnly=False,
  iPartColor=65280
)

MeshCleanup.ManualCheck.Tet(
  crlTargets=[Part(1)],
  iElemQualityType=2,
  iCheckCondition=0,
  dLimitValue=2e-09
)

MeshCleanup.Cleanup.TetVolMesh(  # [hl:start]
  crlParts=[Part(1)],
  crlElems=[],
  dLimitValue=2e-09,
  iMode=1
)  # [hl:end]

MeshCleanup.ManualCheck.Tet(
  crlTargets=[Part(1)],
  iElemQualityType=2,
  iCheckCondition=0,
  dLimitValue=2e-09
)
