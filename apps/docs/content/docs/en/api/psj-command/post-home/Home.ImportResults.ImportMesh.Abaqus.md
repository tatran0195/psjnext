---
title: "Home.ImportResults.ImportMesh.Abaqus()"
description: "Import an Abaqus mesh file to the Jupiter Database as Post document to add result to the mesh."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Home > ImportResults > ImportMesh > Abaqus"
macro _link: "[ImportInpToPost](../../macro/home/ImportInpToPost)"
---

## Description

Import an Abaqus mesh file (\*.inp) to the Jupiter Database (Mesh, boundary conditions, etc.) as Post document to add result to the mesh.

## Syntax

```psj
Home.ImportResults.ImportMesh.Abaqus(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @required -->
### `strPath`

- The specifying an Abaqus file (\*.inp file) which will be used for importing.

<!-- @since:5.1.0 @type:Double @optional @default:60.0 (degree) -->
### `dFaceAngle`

- The angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).

<!-- @since:5.1.0 @type:Double @optional @default:60.0 (degree) -->
### `dEdgeAngle`

- The angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
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
import _status = Home.ImportResults.ImportMesh.Abaqus(strPath=abaqus _file _path,
                                          dFaceAngle=3.000001285727965,
                                          dEdgeAngle=3.000001285727965,
                                          iImportType=0)
JPT.Debugger(import _status)
```
