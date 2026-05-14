---
title: "Home.ImportMesh.Nastran()"
description: "Import a Nastran file (*.bdf) to the Jupiter Database (Mesh, boundary conditions, etc.)"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Home > ImportMesh > Nastran"
macro _link: "[ImportBdf](../../macro/home/ImportBdf)"
---

## Description

Import a Nastran file (\*.bdf) to the Jupiter Database (Mesh, boundary conditions, etc.).

## Syntax

```psj
Home.ImportMesh.Nastran(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[String] @required -->
### `strlPaths`

- A list of the Nastran files (\*.bdf files) which will be used for importing.

<!-- @since:5.1.0 @type:Integer @optional @default:2 -->
### `iImportType`

- The import type:
  - 0: Standard Nastran BDF - Import the BDF model geometry only.
  - 1: Standard Nastran BDF by Property with 1D2D3D-Part - Import the BDF model geometry and material property. All material parts are applied to each part.
  - 2: Standard Nastran BDF by Property with 1D-Edge,2D-Face,3D-Part - Import the BDF model geometry and material property. Parts are created for each material property. The 1D, 2D material properties are applied to edges or faces of a single part. 3D material properties are applied to each part. (Hollow 1D material properties are applied to each part.)
  - 5: Create parts, properties, and materials by referring to the part divisions indicated in the comments of the BDF file exported from NX-Nastran, using the names specified in the comments.

<!-- @since:5.1.0 @type:Double @optional @default:60.0 -->
### `dFaceAngle`

- The angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).

<!-- @since:5.1.0 @type:Double @optional @default:60.0 -->
### `dEdgeAngle`

- The angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bReadJPTComment`

- The option that read name comments for Jupiter.

<!-- @since:5.1.0 @type:Integer @optional @default:-1 -->
### `iCreateDup1DElemAnswer`

- The option that creating duplicated 1D element.
  - -1: Unknown
  - 0: No
  - 1: yes

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bReadHMComment`

- The option that read HM comments.

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The Nastran file (\*.bdf file) is imported successfully.
  - False: The Nastran file (\*.bdf file) cannot be imported.

## Sample Code

```psj {51}
from os import environ

nastran _file _path = environ["Temp"] + "/TechnoStar/Exported _Nastran _File _EXPORT _BDF.bdf"

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

Analysis.Nastran.LinearStatic(nastranAnalysis=NASTRAN _ANALYSIS(iSolverType=1,
                                                               iGridFormatType=1,
                                                               bDeleteFloatingNodes=True,
                                                               dEpsilon=DFLT _DBL,
                                                               iMaxNumOfIter=DFLT _INT,
                                                               iMemory=DFLT _INT,
                                                               iNcpu=1,
                                                               iSolNo=101,
                                                               nastranOutputRequest=NASTRAN _OUTPUT _REQUEST(
                                                                iValueBcresults=DFLT _INT,
                                                                iValueBgresults=DFLT _INT,
                                                                iTypeStrain=0),
                                                               nastranNonlinear=NASTRAN _NONLINEAR(bUseEPSW=True)),
                              iDummyPropMaterialID=1,
                              strPath=nastran _file _path)

JPT.Exec('New Document()')
import _status = Home.ImportMesh.Nastran(strlPaths=[nastran _file _path])
JPT.Debugger(import _status)
```
