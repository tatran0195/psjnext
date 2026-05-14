---
title: "Home.ImportCAD.Spatial()"
description: "Import a CAD file by using Spatial interface to the Jupiter Database"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Home > ImportCAD > Spatial"
macro _link: "[ImportSpatial](../../macro/home/ImportSpatial)"
---

## Description

Import a CAD file by using Spatial interface to the Jupiter Database.

## Syntax

```psj
Home.ImportCAD.Spatial(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[String] @required -->
### `strlPaths`

- A list of the CAD files which will be used for importing.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dSurfacePlaneTolerance`

- The maximum divergence distance when converting the original surface into a facet plane.

<!-- @since:5.0.1 @type:Double @optional @default:20.0 -->
### `dSurfacePlaneAngle`

- The maintain areas with setting angles larger than the angle between facets of the surface plane of the geometry.

<!-- @since:5.0.1 @type:Double @optional @default:1000.0 -->
### `dMaxFacetWidth`

- The maximum size of a single facet edge.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bNXMultipart`

- The enable/disable the configure of the multi-body reading settings.
  - On: Load multi-body into one part.
  - Off: Separate the multi-body into parts and load it under the sub-assembly.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bHealing`

- The enable/disable the healing function.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bSetFaceColor`

- The enable/disable using color information.

## Return Code

A _Boolean_ specifying whether the function is executed successfully or not:

- True: The CAD file (IGES file, STEP file, etc.) is imported successfully.
- False: The CAD file (IGES file, STEP file, etc.) cannot be imported.

## Sample Code

```psj {1,2,3}
imported _status = Home.ImportCAD.Spatial(strlPaths=[JPT.GetProgramPath() +
                                                    "SampleData/CAD _Model/IGES/A400MA.igs"],
                                         bSetFaceColor=True)
JPT.Debugger(imported _status)
```
