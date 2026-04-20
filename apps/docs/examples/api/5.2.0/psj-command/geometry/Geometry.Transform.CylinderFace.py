# Title:   Geometry.Transform.CylinderFace()
# Desc:    Transform to matching two cylindrical surfaces
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/geometry/Geometry.Transform.CylinderFace
# ---
Geometry.Part.Cylinder()
Geometry.Part.Cylinder(dlOrigin=[0.02, 0.0, 0.0], strName="Cylinder_2", iPartColor=6812659)
Geometry.Transform.CylinderFace(crlParts=[Part(1), Part(2)], veclPoint=[[0, 0, 0], [0, -1000, 0],  # [hl]
    [10, 0, 0], [0, 10, 0], [0, -990, 0], [10.0, 10, 10]], bCreateNewPart=True)
