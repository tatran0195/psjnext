# Title:   Geometry.Transform.OOBBAlignment()
# Desc:    A bounding box is defined for each part in such a way that it minimizes empty space, and part movement is performed by aligning these bounding boxes with each other.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/geometry/Geometry.Transform.OOBBAlignment
# ---
#Prepare model

Geometry.Part.Cube(
    dlLength=[0.01, 0.005, 0.003], 
    iPartColor=7697908
)

Geometry.Part.Cube(
    dlLength=[0.008, 0.006, 0.002], 
    strName="Cube_2", 
    iPartColor=7463537
)

Geometry.Transform.Translation(
    crlParts=[Part(2)], 
    dlTranslationVector=[[0.02, 0.005, 0.03]], 
    bCopyReference=True
)

Geometry.Transform.Rotation(
    crlParts=[Part(2)], 
    vecAxis=[0.001, 0.001, 0.001], 
    dAngle=0.523599, 
    dTol=1e-05
)

Geometry.Transform.Rotation(
    crlParts=[Part(2)], 
    posCenter=[0.03143696486949921, 
    0.007476926781237125, 
    0.02508611045777798], 
    vecAxis=[0.001, 0.001, 0.001], 
    dAngle=0.523599, 
    dTol=1e-05
)

# Alignment by OOBB
Geometry.Transform.OOBBAlignment(  # [hl:start]
    crReferencePart=Part(1), 
    crMovingPart=Part(2), 
    iPositionType=4, 
    dlTranslation=[0, 0.0005, 0]
)  # [hl:end]

JPT.ViewFitToModel()
