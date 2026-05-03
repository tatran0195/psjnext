---
title: "Home.ImportCAD.Parasolid()"
description: "Import a parasolid file (*.x_t) to the Jupiter Database"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Home > Import CAD > Parasolid"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Import a parasolid file (\*.x\_t) to the Jupiter Database.

## Syntax

```psj
Home.ImportCAD.Parasolid(...)
```

## Inputs

### `strlPaths` @type(List\[String]) @required

- A list of the parasolid files (\*.x\_t files) which will be used for importing.

### `dChordHeightTolerance` @type(Double) @default(0.0)

- The maximum distance from the actual surface to the facet face. The smaller the Chord Height, the smaller the facets the more accurate the curvature of the surface is represented.

### `dAngleToleranceDegree` @type(Double) @default(7.0)

- The angle tolerance which influences the tessellation of curves with relatively small radii in comparison to the overall size of the CAD model.

### `dSurfacePlaneTolerance` @type(Double) @default(0.0)

- The maximum divergence distance when converting the original surface into a facet face.

### `dSurfacePlaneAngle` @type(Double) @default(20.0)

- The maintained areas with the setting angles larger than the angle between facets face of the geometry.

### `dMaxFacetWidth` @type(Double) @default(0.1)

- The maximum size of a single facet edge.

### `dMinFacetWidth` @type(Double) @default(0.0)

- The minimum size of a single facet edge.

### `dScale` @type(Double) @default(0.001)

- The unit ratio imported from the file's unit into the document's unit.

### `bUseColorInformation` @type(Boolean) @default(False) @since(5.1.0)

- Whether to read color information in the CAD file.

## Return Code

A _Boolean_ specifying whether the function is executed successfully or not:

- True: The parasolid file (\*.x\_t file) is imported successfully.
- False: The parasolid file (\*.x\_t file) cannot be imported.

## Sample Code

```psj {1,2,3,4}
imported_status = Home.ImportCAD.Parasolid(strlPaths=[JPT.GetProgramPath() +
                                                      "SampleData/CAD_Model/Parasolid/BWM_GRABCAD.x_t"],
                                           dAngleToleranceDegree=7.0,
                                           dScale=0.001)
JPT.Debugger(imported_status)
```
