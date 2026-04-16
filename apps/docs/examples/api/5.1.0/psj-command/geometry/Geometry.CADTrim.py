# Title:   Geometry.CADTrim()
# Desc:    CAD Trim
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/geometry/Geometry.CADTrim
# ---
Home.ImportCAD.Parasolid([JPT.GetProgramPath() + "SampleData\\bracket.x_t"],
    dAngleToleranceDegree=7.0, dScale=0.001)

Geometry.CADTrim(crlFaces=[Face(149)], crlParts=[Part(1)], dTrimSize=20.0, dTrimAngle=16.0)
