# Title:   Geometry.RemoveRibBoss()
# Desc:    Remove Rib or Boss geometry
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/geometry/Geometry.RemoveRibBoss
# ---
Geometry.Part.Cube(ilAxialNodes=[11, 11, 11])

Geometry.Edge.Line(dllPoints=[[0.01, 0.01, 0.005], [0, 0.01, 0.005]], crlFaces=[Face(22)])

Geometry.Part.Cylinder(dlOrigin=[0.005, 0.01, 0.005], dTopRadius=0.002, dBottomRadius=0.002,
    dHeight=0.003)

Assemble.BooleanEx([Part(1, 2)])

Geometry.RemoveRibBoss(crlFaces=[Face(35, 37)])
