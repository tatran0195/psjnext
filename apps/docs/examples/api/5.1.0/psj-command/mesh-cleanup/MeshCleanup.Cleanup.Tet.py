# Title:   MeshCleanup.Cleanup.Tet()
# Desc:    Command for cleaning tetrahedral mesh elements based on quality check results.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/mesh-cleanup/MeshCleanup.Cleanup.Tet
# ---
# Prepare model
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

# Check
ret = MeshCleanup.ManualCheck.Tet(
  crlTargets=[Part(1)],
  iElemQualityType=0,
  iCheckCondition=0,
  dLimitValue=0.1
)
print(f"number of error elements: {ret[5]}")

# Cleanup
MeshCleanup.Cleanup.Tet(  # [hl:start]
    crlTargets=[Part(1)], 
    dMinValue=ret[1], 
    dMaxValue=ret[2], 
    dAverageValue=ret[3], 
    iTotalEntities=ret[4], 
    iCheckCondition=0,   # [hl:end]
    dLimitValue=0.1, 
    iFailedElements=ret[5],
    iCleanupCheck=1,
    iMode=1
)

ret = MeshCleanup.ManualCheck.Tet(
  crlTargets=[Part(1)],
  iElemQualityType=0,
  iCheckCondition=0,
  dLimitValue=0.1
)
print(f"number of error elements: {ret[5]}")
