# Title:   MeshCleanup.Cleanup.TetCollapse()
# Desc:    Command for cleaning tetrahedral mesh by Metric:Tet Collapse.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/mesh-cleanup/MeshCleanup.Cleanup.TetCollapse
# ---
Geometry.Part.Cube(
  ilAxialNodes=[3, 3, 3],
  iPartColor=7463537
)

MeshEdit.CreateNode.Point(
  iNewNodeID=27,
  posPoint=[
    0.005026630125939846,
    0.009999999776482582,
    0.004957450088113546,
  ],
  crTarget=Face(22)
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
  iElemQualityType=4,
  iCheckCondition=0,
  dLimitValue=0.02
)
print(f"Number of error elements: {result[5]}")

# Cleanup
MeshCleanup.Cleanup.TetCollapse(crlElems=result[6], dLimitValue=0.05)  # [hl]

result = MeshCleanup.ManualCheck.Tet(
  crlTargets=[Part(1)],
  iElemQualityType=4,
  iCheckCondition=0,
  dLimitValue=0.02
)
print(f"Number of error elements: {result[5]}")
