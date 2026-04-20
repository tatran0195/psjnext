# Title:   MeshCleanup.Cleanup.TetTriangleHeight()
# Desc:    Command for cleaning tetrahedral mesh by Metric:Triangle Height.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/mesh-cleanup/MeshCleanup.Cleanup.TetTriangleHeight
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

result = MeshCleanup.ManualCheck.Tet(
  crlTargets=[Part(1)],
  iElemQualityType=9,
  iCheckCondition=0,
  dLimitValue=0.0003
)

print(f"Number of the error elements: {result[5]}")

# Cleanup
MeshCleanup.Cleanup.TetTriangleHeight(  # [hl:start]
  crlParts=[Part(1)],
  crlElems=[],
  dLimitValue=0.0003,
  iCondition=0
)  # [hl:end]

result = MeshCleanup.ManualCheck.Tet(
  crlTargets=[Part(1)],
  iElemQualityType=9,
  iCheckCondition=0,
  dLimitValue=0.0003
)

print(f"Number of the error elements: {result[5]}")
