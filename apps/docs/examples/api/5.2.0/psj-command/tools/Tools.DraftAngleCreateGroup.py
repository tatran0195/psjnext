# Title:   Tools.DraftAngleCreateGroup()
# Desc:    Create the nodal groups for each draft angle
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.DraftAngleCreateGroup
# ---
# Create Sample Model
Geometry.Part.Trapezoid(
    dlLength=[0.01, 0.001, 0.01], 
    ilAxialNodes=[10, 2, 10], 
    iPartColor=7961077)

JPT.ViewFitToModel()

MeshEdit.OneNode(
    crlNodes=[Node(45)],
    crlFaceFixed=[Face(21)], 
    bOffsetvector=True, dlOffset=[0.8, 0.0, 0.0], dOffset=0.0, 
    dDistStrong=2.0, dDistWeak=5.0)

MeshEdit.OneNode(
    crlNodes=[Node(56)],
    crlFaceFixed=[Face(21)], 
    bOffsetvector=True, dlOffset=[-0.8, 0.0, 0.0], dOffset=0.0,
    dDistStrong=2.0, dDistWeak=5.0)

MeshEdit.OneNode(
    crlNodes=[Node(4)], 
    crlFaceFixed=[Face(21)], 
    bOffsetvector=True, dlOffset=[0.8, 0.0, 0.0], dOffset=0.0, 
    dDistStrong=2.0, dDistWeak=5.0)

# Calculate Draft Angle
draft_angle_result=Tools.DraftAngle(dlDraftDirection=[0, 1, 0], crlTargets=[Part(1)])

# Save result in group 
Tools.DraftAngleCreateGroup(listPairCursorData=draft_angle_result)  # [hl]

# Overwrite result in group with different parameter 
Tools.DraftAngleCreateGroup(  # [hl:start]
    listPairCursorData=draft_angle_result, 
    iNumDigits=5, dGroupMax=60, dGroupMin=-60)  # [hl:end]
