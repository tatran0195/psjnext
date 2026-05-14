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

<!-- @since:5.0.1 @type:List[String] @required -->
### `strlPaths`

- A list of the parasolid files (\*.x\_t files) which will be used for importing.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dChordHeightTolerance`

- The maximum distance from the actual surface to the facet face. The smaller the Chord Height, the smaller the facets the more accurate the curvature of the surface is represented.

<!-- @since:5.0.1 @type:Double @optional @default:7.0 -->
### `dAngleToleranceDegree`

- The angle tolerance which influences the tessellation of curves with relatively small radii in comparison to the overall size of the CAD model.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dSurfacePlaneTolerance`

- The maximum divergence distance when converting the original surface into a facet face.

<!-- @since:5.0.1 @type:Double @optional @default:20.0 -->
### `dSurfacePlaneAngle`

- The maintained areas with the setting angles larger than the angle between facets face of the geometry.

<!-- @since:5.0.1 @type:Double @optional @default:0.1 -->
### `dMaxFacetWidth`

- The maximum size of a single facet edge.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dMinFacetWidth`

- The minimum size of a single facet edge.

<!-- @since:5.0.1 @type:Double @optional @default:0.001 -->
### `dScale`

- The unit ratio imported from the file's unit into the document's unit.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bUseColorInformation`

- Whether to read color information in the CAD file.

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
