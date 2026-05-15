---
title: "Home.ImportMesh.AnsysDat()"
description: "Import an Ansys file (*.dat) to the Jupiter Database (Mesh, boundary conditions, etc.)"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Home > ImportMesh > AnsysDat"
macro _link: "[ImportAnsys](../../macro/home/ImportAnsys)"
---

## Description

Import an Ansys file (\*.dat) to the Jupiter Database (Mesh, boundary conditions, etc.).

## Syntax

```psj
Home.ImportMesh.AnsysDat(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### strlPaths

- Specify a list of the Ansys files (\*.dat files) which will be used for importing.

<!-- @since:5.0.1 @optional -->
### dFaceAngle

- Specify the angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).
- The default value is 60.0.

<!-- @since:5.0.1 @optional -->
### dEdgeAngle

- Specify the angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).
- The default value is 60.0.

## Return Code

A _Boolean_ specifying whether the function is executed successfully or not:

- True: The Ansys file (\*.dat file) is imported successfully.
- False: The Ansys file (\*.dat file) cannot be imported.

## Sample Code

```psj {41}
from os import environ

ansys _file _path = environ["Temp"] + "/TechnoStar/Exported _Ansys _File _EXPORT _DAT.dat"

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

Analysis.Ansys.LinearStatic("Job1",
                            ansysAnalysisBasic=BASIC(dTimeStepSize=1.0,
                                                     dMinTimeStep=1.0),
                            iLoadCaseId=1,
                            strFileName=ansys _file _path)

JPT.Exec('New Document()')
import _status = Home.ImportMesh.AnsysDat(strlPaths=[ansys _file _path])
JPT.Debugger(import _status)
```
