---
title: "Home.ImportMesh.AbaqusINP()"
description: "Import an Abaqus file (*.inp) to the Jupiter Database (Mesh, boundary conditions, etc.)"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Home > ImportMesh > AbaqusINP"
macro _link: "[ImportInp](../../macro/home/ImportInp)"
---

## Description

Import an Abaqus file (\*.inp) to the Jupiter Database (Mesh, boundary conditions, etc.).

## Syntax

```psj
Home.ImportMesh.AbaqusINP(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### strlPaths

- Specify a list of the Abaqus files (\*.inp files) which will be used for importing.

<!-- @since:5.0.1 @optional -->
### dFaceAngle

- Specify the angle tolerance in order to determine the face division. Define a face by creating an edge between adjacent elements with an angle smaller than the specified value.
- The default value is 60.0.

<!-- @since:5.0.1 @optional -->
### dEdgeAngle

- Specify the angle tolerance in order to determine the edge division. Divide an edge by creating a vertex on adjacent edge elements with an angle smaller than the specified value.
- The default value is 60.0.

<!-- @since:5.0.1 @optional -->
### iImportType

- Specify the import type.
  - 0: Standard Abaqus Inp - Import the model geometry only.
  - 1: Standard Abaqus Inp by Property - Import the model geometry and material property. A body is created for each material property.
- The default value is 1.

## Return Code

A _Boolean_ specifying whether the function is executed successfully or not:

- True: The Abaqus file (\*.inp file) is imported successfully.
- False: The Abaqus file (\*.inp file) cannot be imported.

## Sample Code

```psj {41,42,43,44}
from os import environ

abaqus _file _path = environ["Temp"] + "/TechnoStar/Exported _Abaqus _File _EXPORT _INP.inp"

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

JPT.Exec('CreateAbaqusJob("Job _1", 0, 0, 0, 0, 1, 0, "", \
                          [], 0:0, [], 0, 1, 0, 0, 1, 22:1, 1, 0, 0, 0)')

Analysis.ExportAbaqus(crAbaJob=AbaqusJob(1),
                      strInpPath=abaqus _file _path)

JPT.Exec('New Document()')
import _status = Home.ImportMesh.AbaqusINP(strlPaths=[abaqus _file _path],
                                          dFaceAngle=3.000001285727965,
                                          dEdgeAngle=3.000001285727965,
                                          iImportType=0)
JPT.Debugger(import _status)
```
