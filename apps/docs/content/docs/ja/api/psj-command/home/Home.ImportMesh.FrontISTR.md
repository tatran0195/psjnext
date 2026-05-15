---
title: "Home.ImportMesh.FrontISTR()"
description: "Import an FrontISTR file (*.msh) to the Jupiter Database (Mesh, boundary conditions, etc.)"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Home > ImportMesh > FrontISTR"
macro _link: "[ImportPreFrontISTR](../../macro/home/ImportPreFrontISTR)"
---

## Description

Import an FrontISTR file (.mesh / .dat) to the Jupiter Database (Mesh, boundary conditions, etc.).

## Syntax

```psj
Home.ImportMesh.FrontISTR(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### strlPaths

- Specify a list of the FrontISTR files (.mesh / .dat files) which will be used for importing.

<!-- @since:5.1.0 @optional -->
### dFaceAngle

- Specify the angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).
- The default value is 60.0.

<!-- @since:5.1.0 @optional -->
### dEdgeAngle

- Specify the angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).
- The default value is 60.0.

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The FrontISTR file (.mesh / .dat file) is imported successfully.
  - False: The FrontISTR file (.mesh / .dat file) cannot be imported.

## Sample Code

```psj {35-43}
from os import environ

FrontISTR _file _path = environ["Temp"] + "/TechnoStar/"
FrontISTR _job _name = "Job _1"

Geometry.Part.Cube()
Meshing.SolidMeshing(crlParts=[Part(1)],
                     dGradingFactor=1.05,
                     dStretchLimit=0.1,
                     iSpeedVsQual=1,
                     iRegion=1,
                     bSafeMode=False,
                     iParallel=12,
                     bInternalMeshOnly=False,
                     iPartColor=65280)

BoundaryConditions.FixedConstraint(crlTargets=[Face(24)])
BoundaryConditions.Pressure.General(dPressure=5000000.0,
                                    crlTargets=[Face(23)])

Properties.Material.Add("Stainless _Steel",
                        [Density([(DENSITY, 7.75e-09)]),
                         Elastic([(YOUNGS _MODULUS, 193000.0),
                                  (POISSONS _RATIO, 0.31)])])
Properties.Solid(crlTargets=[Part(1)],
                 strName="Cube _for _testing",
                 iPropertyColor=16131973,
                 crMaterial=Material(1),
                 iCordM=-2,
                 dDynaRemeshVal1=DFLT _DBL,
                 dDynaRemeshVal2=DFLT _DBL,
                 dDispHG=DFLT _DBL,
                 iFLG=-1)

JPT.Exec(f'FrontISTR _LinearStatic("{FrontISTR _file _path}", \
        [], "{FrontISTR _job _name}", 3, 20000, 2, 0, 0, 1e-06, 1, 0, 0, 0, "", "STEP0", 0, \
        ["AP1", 0.25, 10, 50, 10, 1, 1.25, 1, 1, 1, 5, 0.25, 5], \
        0, ["TP1", 0, 0, 0, 0, 0, 0], 1e-05, 10, 0, 0, 0, "", "", \
        0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 3, 0, 0, 1, 1, 1, 1, 0, 0, \
        0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
        0, 0, 0, 0, 0, 0, 0, 0, "", "", "", "", "", "", "", "", 0, 0, 1, \
        "10", "1.0e-8", "60", 0, 0, "", "", "", "", "0.0", "1.0", 0, 0, \
        "0.0", "0.0", "0.log", "", "1.0e-8", "10", 1, "1", 0, 0, 0, 0, "", "", 1, 0, 0)')

JPT.Exec('New Document()')
import _status = Home.ImportMesh.FrontISTR(strlPaths=[FrontISTR _file _path+FrontISTR _job _name+".msh"])
JPT.Debugger(import _status)
```
