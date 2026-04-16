# Title:   MeshCleanup.Cleanup.TetInteriorAngle()
# Desc:    Command for cleaning tetrahedral mesh by Metric:Interior Angle.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/mesh-cleanup/MeshCleanup.Cleanup.TetInteriorAngle
# ---
Geometry.Part.Cube()

Meshing.SolidMeshing(
  crlParts=[Part(1)],
  bTet10=True, 
  dGradingFactor=1.05,
  iSpeedVsQual=1,
  bSafeMode=False,
  iParallel=16,
  bInternalMeshOnly=False,
  iPartColor=65280
)

# 110 elements found
result = MeshCleanup.ManualCheck.Tet(
  crlTargets=[Part(1)],
  iElemQualityType=10,
  iCheckCondition=0,
  dLimitValue=30
)
print(f"Number of error elements is {result[5]}")

# Cleanup
MeshCleanup.Cleanup.TetInteriorAngle(  # [hl:start]
  crlParts=[Part(1)],
  crlElems=[],
  dLimitValue=30
)  # [hl:end]

# Half of them are cleanupped
result = MeshCleanup.ManualCheck.Tet(
  crlTargets=[Part(1)],
  iElemQualityType=10,
  iCheckCondition=0,
  dLimitValue=30
)
print(f"Number of error elements is {result[5]}")
