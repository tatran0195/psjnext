---
title: "Home.ImportMesh.LsDyna()"
description: "Import a LS-Dyna file (*.k) to the Jupiter Database (Mesh, boundary conditions, etc.)"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Home > ImportMesh > LsDyna"
macro_link: "[ImportLsDyna](../../macro/home/ImportLsDyna)"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] title changed across versions
     context: {"values":["Home.ImportMesh.LSDYNA()","Home.ImportMesh.LsDyna()"]}
   [frontmatter_conflict] description changed across versions
     context: {"values":["Import an Ls-Dyna file (*.k) to the Jupiter Database (Mesh, boundary conditions, etc.)","Import a LS-Dyna file (*.k) to the Jupiter Database (Mesh, boundary conditions, etc.)"]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Import a LS-Dyna file (\*.k) to the Jupiter Database (Mesh, boundary conditions, etc.)

## Syntax

```psj
Home.ImportMesh.LsDyna(...)
```

## Inputs

### `strlPaths` @type(List\[String]) @required

- A list of the LS-Dyna files (\*.k files) which will be used for importing.

### `dFaceAngle` @type(Double) @default(60.0)

- The angle tolerance in order to determine the face division (By creating an edge between adjacent elements with an angle smaller than the specified value).

### `dEdgeAngle` @type(Double) @default(60.0)

- The angle tolerance in order to determine the edge division (By creating a vertex on adjacent edge elements with an angle larger than the specified value).

## Return Code

- A _Boolean_ specifying whether the function is executed successfully or not:
  - True: The LS-Dyna file (\*.k file) is imported successfully.
  - False: The LS-Dyna file (\*.k file) cannot be imported.

## Sample Code

```psj {40}
from os import environ

lsdyna_file_path = environ["Temp"] + "/TechnoStar/Exported_LSDyna_File_EXPORT_K.k"

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

Analysis.LSDYNAJob()
Analysis.ExportLsdyna(strPath=lsdyna_file_path, 
                    crJob=LSDynaJob(1))


JPT.Exec('New Document()')
import_status = Home.ImportMesh.LsDyna(strlPaths=[lsdyna_file_path])
JPT.Debugger(import_status)
```
