# Title:   Geometry.LogoRemoval()
# Desc:    Removal logos or bolts
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/geometry/Geometry.LogoRemoval
# ---
Geometry.Part.Cube()

Geometry.Part.Cube(dlOrigin=[0.0045, 0.002, 0.0095], dlLength=[0.001, 0.006, 0.001])

Geometry.Part.Cube(dlOrigin=[0.003, 0.001, 0.0095], dlLength=[0.004, 0.001, 0.001])

Geometry.Part.Cube(dlOrigin=[0.003, 0.008, 0.0095], dlLength=[0.004, 0.001, 0.001])

Assemble.BooleanEx([Part(2, 3, 4)])

Geometry.MergeEntities.Faces(crlFaces=[Face(51, 52, 77, 78, 103, 104)])

Assemble.BooleanEx([Part(1, 2)], iBooleanType=1)

Geometry.LogoRemoval(crlStartFaces=[Face(51)], crlStopFaces=[Face(26)])
