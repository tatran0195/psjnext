# Title:   MeshCleanup.Cleanup.TetEdge()
# Desc:    Command for cleaning tetrahedral mesh elements by edge length.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/mesh-cleanup/MeshCleanup.Cleanup.TetEdge
# ---
Geometry.Part.Cube(
  ilAxialNodes=[3, 3, 3],
  iPartColor=7463537,
)

MeshCleanup.Manual2D.Split(
    crplElemEdge=[CursorPair(Node(7), Node(15))], 
    dRatio=0.99)

Meshing.SolidMeshing(
  crlParts=[Part(1)],
  dGradingFactor=1.05,
  iSpeedVsQual=1,
  iRegion=1,
  bSafeMode=False,
  iParallel=16,
  bInternalMeshOnly=True,
  iPartColor=65280,
)

result = MeshCleanup.ManualCheck.Tet(
  crlTargets=[Part(1)],
  iElemQualityType=6,
  iCheckCondition=0,
  dLimitValue=0.0001,
)

print(result[7])
print(f"Number of error elements: {result[5]}")

# Cleanup
MeshCleanup.Cleanup.TetEdge(  # [hl:start]
  crplElemEdges=result[7],
  iCondition=0,
  dLimitValue=0.0001,
)  # [hl:end]

result = MeshCleanup.ManualCheck.Tet(
  crlTargets=[Part(1)],
  iElemQualityType=6,
  iCheckCondition=0,
  dLimitValue=0.0001,
)
print(f"Number of error elements: {result[5]}")
