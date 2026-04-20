# Title:   MeshCleanup.Cleanup.Manual()
# Desc:    Command for cleaning surface mesh elements that do not meet the specified quality criteria.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/mesh-cleanup/MeshCleanup.Cleanup.Manual
# ---
# Prepare Model
Geometry.Part.Cube(ilAxialNodes=[3, 3, 3], iPartColor=7463537)
MeshEdit.CreateNode.Point(
  iNewNodeID=27,
  posPoint=[
    0.005225089844316244,
    0.00481416005641222,
    0.009999999776482582,
  ],
  crTarget=Face(26),
)

# Check
ret = MeshCleanup.ManualCheck.Tri(
  crlTargets=[Part(1)],
  iCheckCondition=0,
  dLimitValue=0.1,
)
print(f"number of error elements: {ret[5]}")
MeshCleanup.Cleanup.Manual(  # [hl:start]
  crlParts=[Part(1)],
  dLimitValue=0.1,
  dCFLValue=0.1,
  crlElems=ret[6],
)  # [hl:end]

ret = MeshCleanup.ManualCheck.Tri(
  crlTargets=[Part(1)],
  iCheckCondition=0,
  dLimitValue=0.1,
)
print(f"number of error elements: {ret[5]}")
