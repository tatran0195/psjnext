# Title:   MidPlane.FindMidPlane()
# Desc:    Create mid-planes for the specified parts.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/midplane/MidPlane.FindMidPlane
# ---
Geometry.Part.Cube(dlLength=[0.001, 0.01, 0.01])
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0],
                    dlLength=[0.002, 0.01, 0.01],
                    strName="Cube_2",
                    iPartColor=6409934)
MidPlane.FindMidPlane(crlTargetParts=[Part(1, 2)])  # [hl]
