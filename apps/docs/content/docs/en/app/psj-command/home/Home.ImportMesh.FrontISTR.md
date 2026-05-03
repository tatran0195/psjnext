---
title: "Home.ImportMesh.FrontISTR()"
description: "Import an FrontISTR file (*.msh) to the Jupiter Database (Mesh, boundary conditions, etc.)"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Home > ImportMesh > FrontISTR"
macro_link: "[ImportPreFrontISTR](../../macro/home/ImportPreFrontISTR)"
---

## Description

Import an FrontISTR file (.mesh / .dat) to the Jupiter Database (Mesh, boundary conditions, etc.).

## Syntax

```psj
Home.ImportMesh.FrontISTR(...)
```

## Inputs

### `strlPaths` @type(List\[String]) @required

- A list of the FrontISTR files (.mesh / .dat files) which will be used for importing.

### `dFaceAngle` @type(Double) @default(60.0)

- The angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).

### `dEdgeAngle` @type(Double) @default(60.0)

- The angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The FrontISTR file (.mesh / .dat file) is imported successfully.
  - False: The FrontISTR file (.mesh / .dat file) cannot be imported.

## Sample Code

```psj {35-43}
from os import environ

FrontISTR_file_path = environ["Temp"] + "/TechnoStar/"
FrontISTR_job_name = "Job_1"

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

Properties.Material.Add("Stainless_Steel",
                        [Density([(DENSITY, 7.75e-09)]),
                         Elastic([(YOUNGS_MODULUS, 193000.0),
                                  (POISSONS_RATIO, 0.31)])])
Properties.Solid(crlTargets=[Part(1)],
                 strName="Cube_for_testing",
                 iPropertyColor=16131973,
                 crMaterial=Material(1),
                 iCordM=-2,
                 dDynaRemeshVal1=DFLT_DBL,
                 dDynaRemeshVal2=DFLT_DBL,
                 dDispHG=DFLT_DBL,
                 iFLG=-1)

JPT.Exec(f'FrontISTR_LinearStatic("{FrontISTR_file_path}", \
        [], "{FrontISTR_job_name}", 3, 20000, 2, 0, 0, 1e-06, 1, 0, 0, 0, "", "STEP0", 0, \
        ["AP1", 0.25, 10, 50, 10, 1, 1.25, 1, 1, 1, 5, 0.25, 5], \
        0, ["TP1", 0, 0, 0, 0, 0, 0], 1e-05, 10, 0, 0, 0, "", "", \
        0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 3, 0, 0, 1, 1, 1, 1, 0, 0, \
        0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
        0, 0, 0, 0, 0, 0, 0, 0, "", "", "", "", "", "", "", "", 0, 0, 1, \
        "10", "1.0e-8", "60", 0, 0, "", "", "", "", "0.0", "1.0", 0, 0, \
        "0.0", "0.0", "0.log", "", "1.0e-8", "10", 1, "1", 0, 0, 0, 0, "", "", 1, 0, 0)')

JPT.Exec('New Document()')
import_status = Home.ImportMesh.FrontISTR(strlPaths=[FrontISTR_file_path+FrontISTR_job_name+".msh"])
JPT.Debugger(import_status)
```
