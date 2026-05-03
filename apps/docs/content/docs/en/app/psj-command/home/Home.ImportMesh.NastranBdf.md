---
title: "Home.ImportMesh.NastranBdf()"
description: "Import a Nastran file (*.bdf) to the Jupiter Database (Mesh, boundary conditions, etc.)"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Home > ImportMesh > NastranBdf"
macro_link: "[ImportBdf](../../macro/home/ImportBdf)"
---

## Description

Import a Nastran file (\*.bdf) to the Jupiter Database (Mesh, boundary conditions, etc.).

## Syntax

```psj
Home.ImportMesh.NastranBdf(...)
```

## Inputs

### `strlPaths` @type(List\[String]) @required

- A list of the Nastran files (\*.bdf files) which will be used for importing.

### `iImportType` @type(Integer) @default(2)

- The import type:
  - 0: Standard Nastran BDF - Import the BDF model geometry only.
  - 1: Standard Nastran BDF by Property with 1D2D3D-Part - Import the BDF model geometry and material property. All material parts are applied to each part.
  - 2: Standard Nastran BDF by Property with 1D-Edge,2D-Face,3D-Part - Import the BDF model geometry and material property. Parts are created for each material property. The 1D, 2D material properties are applied to edges or faces of a single part. 3D material properties are applied to each part. (Hollow 1D material properties are applied to each part.)

### `dFaceAngle` @type(Double) @default(60.0)

- The angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).

### `dEdgeAngle` @type(Double) @default(60.0)

- The angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).

### `bReadNameComment` @type(Boolean) @default(False)

- The option that read name comments for Jupiter.

### `iCreateDup1DElemAnswer` @type(Integer) @default(-1)

- The option that creating duplicated 1D element.
  - -1: Unknown
  - 0: No
  - 1: yes

## Return Code

A _Boolean_ specifying whether the function is executed successfully or not:

- True: The Nastran file (\*.bdf file) is imported successfully.
- False: The Nastran file (\*.bdf file) cannot be imported.

## Sample Code

```psj {50}
from os import environ

nastran_file_path = environ["Temp"] + "/TechnoStar/Exported_Nastran_File_EXPORT_BDF.bdf"

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

Analysis.Nastran.LinearStatic(nastranAnalysis=NASTRAN_ANALYSIS(iSolverType=1,
                                                               iGridFormatType=1,
                                                               bDeleteFloatingNodes=True,
                                                               dEpsilon=DFLT_DBL,
                                                               iMaxNumOfIter=DFLT_INT,
                                                               iMemory=DFLT_INT,
                                                               iNcpu=1,
                                                               iSolNo=101,
                                                               nastranOutputRequest=NASTRAN_OUTPUT_REQUEST(iValueBcresults=DFLT_INT,
                                                                                                           iValueBgresults=DFLT_INT,
                                                                                                           iTypeStrain=0),
                                                               nastranNonlinear=NASTRAN_NONLINEAR(bUseEPSW=True)),
                              iDummyPropMaterialID=1,
                              strPath=nastran_file_path)

JPT.Exec('New Document()')
import_status = Home.ImportMesh.AnsysDat(strlPaths=[nastran_file_path])
JPT.Debugger(import_status)
```
