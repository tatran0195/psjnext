# Title:   MeshCleanup.Cleanup.Auto()
# Desc:    Command for automatically cleaning triangle or quadrilateral mesh elements based on quality check results.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/mesh-cleanup/MeshCleanup.Cleanup.Auto
# ---
#Prepare Model
Geometry.Part.Cube(
    ilAxialNodes=[3, 3, 3], 
    iPartColor=7463537
)

MeshCleanup.Manual2D.Split(
    crplElemEdge=[CursorPair(Node(7), Node(15))], 
    dRatio=0.99
)

MeshCleanup.Manual2D.Split(
    crplElemEdge=[CursorPair(Node(16), Node(22))], 
    dRatio=0.99
)

# Check
result = MeshCleanup.AutoCheck.Tri(
    crlTargets=[Part(1)], 
    bStretchCheck=True, 
    bAspectRatioCheck=True, 
    bEdgeLengthCheck=True, 
    bAreaCheck=True, 
    bNodeValenceCheck=True, 
    bInteriorAngleCheck=True, 
    bDuplicateElemsCheck=True, 
    dStretchLimit=0.1, 
    dAspectRatioLimit=10, 
    dEdgeLengthLimit=0.0001, 
    dAreaLimit=1e-08, 
    dNodeValenceLimit=10, 
    dInteriorAngleLimit=0.174533
)

print(f"Number of error elements: {result[1]}")

# Auto cleanup
MeshCleanup.Cleanup.Auto(  # [hl:start]
    crlParts=[Part(1)], 
    iElemType=0, 
    blCheckCondition=[False, True, False, False, True, False, False], 
    blElemQuality=[False, True, True, True, True, True, True],
     dlLimitValue=[0.1, 10.0, 0.0001, 1e-08, 10.0, 10.0, 0.0], 
    crlElems=result[2]
)  # [hl:end]

result = MeshCleanup.AutoCheck.Tri(
    crlTargets=[Part(1)], 
    bStretchCheck=True, 
    bAspectRatioCheck=True, 
    bEdgeLengthCheck=True, 
    bAreaCheck=True, 
    bNodeValenceCheck=True, 
    bInteriorAngleCheck=True, 
    bDuplicateElemsCheck=True, 
    dStretchLimit=0.1, 
    dAspectRatioLimit=10, 
    dEdgeLengthLimit=0.0001, 
    dAreaLimit=1e-08, 
    dNodeValenceLimit=10, 
    dInteriorAngleLimit=0.174533
)

print(f"Number of error elements: {result[1]}")
