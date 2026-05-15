---
title: "Home.ImportCAD.Parasolid()"
description: "Import a parasolid file (*.x _t) to the Jupiter Database"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Home > Import CAD > Parasolid"
---

## Description

Import a parasolid file (\*.x\_t) to the Jupiter Database.

## Syntax

```psj
Home.ImportCAD.Parasolid(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### strlPaths

- Specify a list of the parasolid files (\*.x\_t files) which will be used for importing.

<!-- @since:5.0.1 @optional -->
### dChordHeightTolerance

- Specify the maximum distance from the actual surface to the facet face. The smaller the Chord Height, the smaller the facets the more accurate the curvature of the surface is represented.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dAngleToleranceDegree

- Specify the angle tolerance which influences the tessellation of curves with relatively small radii in comparison to the overall size of the CAD model.
- The default value is 7.0.

<!-- @since:5.0.1 @optional -->
### dSurfacePlaneTolerance

- Specify the maximum divergence distance when converting the original surface into a facet face.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dSurfacePlaneAngle

- Specify the maintained areas with the setting angles larger than the angle between facets face of the geometry.
- The default value is 20.0.

<!-- @since:5.0.1 @optional -->
### dMaxFacetWidth

- Specify the maximum size of a single facet edge.
- The default value is 0.1.

<!-- @since:5.0.1 @optional -->
### dMinFacetWidth

- Specify the minimum size of a single facet edge.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dScale

- Specify the unit ratio imported from the file's unit into the document's unit.
- The default value is 0.001.

<!-- @since:5.1.0 @optional -->
### bUseColorInformation

- Specify whether to read color information in the CAD file.
- The default value is _False_.

## Return Code

A _Boolean_ specifying whether the function is executed successfully or not:

- True: The parasolid file (\*.x\_t file) is imported successfully.
- False: The parasolid file (\*.x\_t file) cannot be imported.

## Sample Code

```psj {1,2,3,4}
imported _status = Home.ImportCAD.Parasolid(strlPaths=[JPT.GetProgramPath() +
                                                      "SampleData/CAD _Model/Parasolid/BWM _GRABCAD.x _t"],
                                           dAngleToleranceDegree=7.0,
                                           dScale=0.001)
JPT.Debugger(imported _status)
```
