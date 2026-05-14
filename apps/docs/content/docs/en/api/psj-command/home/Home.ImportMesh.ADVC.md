---
title: "Home.ImportMesh.ADVC()"
description: "Import an ADVC file (*.adx) to the Jupiter Database (Mesh, boundary conditions, etc.)"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Home > ImportMesh > ADVC"
macro _link: "[ImportAdxList](../../macro/home/ImportAdxList)"
---

## Description

Import an ADVC file (\*.adx) to the Jupiter Database (Mesh, boundary conditions, etc.).

## Syntax

```psj
Home.ImportMesh.ADVC(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[String] @required -->
### `strlPaths`

- A list of the ADVC files (\*.adx files) which will be used for importing.

<!-- @since:5.1.0 @type:Double @optional @default:60.0 -->
### `dFaceAngle`

- The angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).

<!-- @since:5.1.0 @type:Double @optional @default:60.0 -->
### `dEdgeAngle`

- The angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).

<!-- @since:5.1.0 @type:Bool @optional @default:False -->
### `bReadCommentsForJupiter`

- Whether Jupiter enables to read Material, Property, LBC, Contact, Job name, and related group names.

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The ADVC file (\*.adx file) is imported successfully.
  - False: The ADVC file (\*.adx file) cannot be imported.

## Sample Code

```psj {84}
from os import environ

advc _file _path = environ["Temp"] + "/TechnoStar/Exported _ADVC _File _EXPORT _ADX.adx"

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

JPT.Exec('AdvcStaticProcess("ADVC _DEFAULT _PROCESS", 0, 0, 1, 1, 1, 1e-05, \
                            -1, -1, 2147483647, -1, 2147483647, 1.79769e+308, \
                            1.79769e+308, 1.79769e+308, 0, 1.79769e+308, 1.79769e+308, \
                            1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, \
                            1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, \
                            2147483647, 2147483647, 1.79769e+308, 2147483647, 0, -1, \
                            2147483647, 2147483647, 1.79769e+308, 1.79769e+308, \
                            1.79769e+308, 1.79769e+308, 2147483647, 0, 1.79769e+308, \
                            1.79769e+308, 0, 0, 2147483647, 2147483647, 2147483647, \
                            1.79769e+308, 1.79769e+308, 1.79769e+308, 2147483647, \
                            2147483647, 1.79769e+308, 1.79769e+308, 1.79769e+308, \
                            1.79769e+308, 1.79769e+308, 0, 1.79769e+308, 1.79769e+308, \
                            1.79769e+308, 1.79769e+308, 1.79769e+308, 0:0, \
                            [], [], [], [], -1, "", [], "", 2147483647)')

JPT.Exec('AdvcStaticProcess("ADVC _DEFAULT _PROCESS", 0, 0, 1, 1, 1, 1e-05, -1, \
                            -1, 2147483647, -1, 2147483647, 1.79769e+308, 1.79769e+308, \
                            1.79769e+308, 0, 1.79769e+308, 1.79769e+308, 1.79769e+308, \
                            1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, \
                            1.79769e+308, 1.79769e+308, 1.79769e+308, 2147483647, \
                            2147483647, 1.79769e+308, 2147483647, 0, -1, 2147483647, \
                            2147483647, 1.79769e+308, 1.79769e+308, 1.79769e+308, \
                            1.79769e+308, 2147483647, 0, 1.79769e+308, 1.79769e+308, \
                            0, 0, 2147483647, 2147483647, 2147483647, 1.79769e+308, \
                            1.79769e+308, 1.79769e+308, 2147483647, 2147483647, \
                            1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, \
                            1.79769e+308, 0, 1.79769e+308, 1.79769e+308, 1.79769e+308, \
                            1.79769e+308, 1.79769e+308, 119:1, \
                            [(37:1, 0:0, 1), (40:1, 0:0, 1)], [], [], [], -1, "", [], "", 2147483647)')

JPT.Exec('AdvcStaticProcess("ADVC _DEFAULT _PROCESS", 0, 0, 1, 1, 1, 1e-05, -1, -1, \
                            2147483647, -1, 2147483647, 1.79769e+308, 1.79769e+308, \
                            1.79769e+308, 0, 1.79769e+308, 1.79769e+308, 1.79769e+308, \
                            1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, \
                            1.79769e+308, 1.79769e+308, 1.79769e+308, 2147483647, \
                            2147483647, 1.79769e+308, 2147483647, 0, -1, 2147483647, \
                            2147483647, 1.79769e+308, 1.79769e+308, 1.79769e+308, \
                            1.79769e+308, 2147483647, 0, 1.79769e+308, 1.79769e+308, \
                            0, 0, 2147483647, 2147483647, 2147483647, 1.79769e+308, \
                            1.79769e+308, 1.79769e+308, 2147483647, 2147483647, \
                            1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, \
                            1.79769e+308, 0, 1.79769e+308, 1.79769e+308, 1.79769e+308, \
                            1.79769e+308, 1.79769e+308, 119:1, [], [], [], [], \
                            -1, "", [], "", 2147483647)')

JPT.Exec('ADVC _Structure("Job _1", "", 0, [119:1], [], [], 0, 0:0, 0, 0, 0, 0, 0, 0, 0, \
                         [3:1], 1, 1, 1, 1, 0, 1, 22:1, 0, "", 2147483647, 2147483647, \
                         0, 1, [], 0, 0, {}, 0, 10, 10, 1, 0, "", 1)'.format(advc _file _path))

JPT.Exec('New Document()')
import _status = Home.ImportMesh.ADVCADX(strlPaths=[advc _file _path])
JPT.Debugger(import _status)
```
