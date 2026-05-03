---
title: "Home.ImportCAD.Spatial()"
description: "Import a CAD file by using Spatial interface to the Jupiter Database"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Home > ImportCAD > Spatial"
macro_link: "[ImportSpatial](../../macro/home/ImportSpatial)"
---

## Description

Import a CAD file by using Spatial interface to the Jupiter Database.

## Syntax

```psj
Home.ImportCAD.Spatial(...)
```

## Inputs

### `strlPaths` @type(List\[String]) @required

- A list of the CAD files which will be used for importing.

### `dSurfacePlaneTolerance` @type(Double) @default(0.0)

- The maximum divergence distance when converting the original surface into a facet plane.

### `dSurfacePlaneAngle` @type(Double) @default(20.0)

- The maintain areas with setting angles larger than the angle between facets of the surface plane of the geometry.

### `dMaxFacetWidth` @type(Double) @default(1000.0)

- The maximum size of a single facet edge.

### `bNXMultipart` @type(Boolean) @default(True)

- Enable/disable the configure of the multi-body reading settings.
  - On: Load multi-body into one part.
  - Off: Separate the multi-body into parts and load it under the sub-assembly.

### `bHealing` @type(Boolean) @default(True)

- Enable/disable the healing function.

### `bSetFaceColor` @type(Boolean) @default(False)

- Enable/disable using color information.

## Return Code

A _Boolean_ specifying whether the function is executed successfully or not:

- True: The CAD file (IGES file, STEP file, etc.) is imported successfully.
- False: The CAD file (IGES file, STEP file, etc.) cannot be imported.

## Sample Code

```psj {1,2,3}
imported_status = Home.ImportCAD.Spatial(strlPaths=[JPT.GetProgramPath() +
                                                    "SampleData/CAD_Model/IGES/A400MA.igs"],
                                         bSetFaceColor=True)
JPT.Debugger(imported_status)
```
