---
title: "Home.ImportResults.ImportMesh.Nastran()"
description: "Import a Nastran mesh file to the Jupiter Database as Post document to add result to the mesh."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Home > ImportResults > ImportMesh > Nastran"
macro _link: "[CmdImportTSVBdfPost](../../macro/home/CmdImportTSVBdfPost)"
---

## Description

Import a Nastran mesh file (\*.bdf, \*.nas, \*.dat) to the Jupiter Database as Post document to add result to the mesh.

## Syntax

```psj
Home.ImportResults.ImportMesh.Nastran(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @required -->
### `strPath`

- A Nastran files (\*.bdf , \*.nas, \*.dat file) which will be used for importing.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iImportType`

- The import type. Here is set to always 1.

<!-- @since:5.1.0 @type:Double @optional @default:60.0 (degree) -->
### `dFaceAngle`

- The angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).

<!-- @since:5.1.0 @type:Double @optional @default:60.0 (degree) -->
### `dEdgeAngle`

- The angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bReadLoadAndConstraint`

- Whether or not to read loads and constraint.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bReadConnection`

- Whether or not to read connections.

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The Nastran file (\*.bdf file) is imported successfully.
  - False: The Nastran file (\*.bdf file) cannot be imported.

## Sample Code

```psj {50}
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
                                                               nastranOutputRequest=NASTRAN _OUTPUT _REQUEST(iValueBcresults=DFLT _INT,
                                                                                                           iValueBgresults=DFLT _INT,
                                                                                                           iTypeStrain=0),
                                                               nastranNonlinear=NASTRAN _NONLINEAR(bUseEPSW=True)),
                              iDummyPropMaterialID=1,
                              strPath=nastran _file _path)

JPT.Exec('New Document()')
import _status = Home.ImportResults.ImportMesh.Nastran(strPath=nastran _file _path)
JPT.Debugger(import _status)
```
