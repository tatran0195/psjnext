# Title:   Geometry.MakeFacePlanar()
# Desc:    Flatten curved faces into the planar face
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/geometry/Geometry.MakeFacePlanar
# ---
Geometry.Part.Cube()

Geometry.Part.Trapezoid(dlOrigin=[0.0005, 0.0005, 0.01], dlLength=[0.005, 0.005, 0.005],
    dTopXLength=3.0, strName="Trapezoid_5", iPartColor=7697908)

Geometry.MakeFacePlanar(dlPlanePt1=[0.01, 0.0, 0.01], dlPlanePt2=[0.01, 0.01, 0.01],
    dlPlanePt3=[0.0, 0.01, 0.01], ilFaceIds=[52, 50, 48, 49, 47])
