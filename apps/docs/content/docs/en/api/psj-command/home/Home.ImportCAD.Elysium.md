---
title: "Home.ImportCAD.Elysium()"
description: "Import a CAD file by using Elysium interface to the Jupiter Database"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Home > Import CAD > Elysium"
---

## Description

Import a CAD file by using Elysium interface to the Jupiter Database.

## Syntax

```psj
Home.ImportCAD.Elysium(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[String] @required -->
### `strlPaths`

- A list of the CAD files which will be used for importing.

<!-- @since:5.0.1 @type:Double @optional @default:1.0 -->
### `dChordHeightTolerance`

- The maximum distance from the actual surface to the facet face. The smaller the Chord Height, the smaller the facets the more accurate the curvature of the surface is represented.

<!-- @since:5.0.1 @type:Double @optional @default:5.0 -->
### `dAngleToleranceDegree`

- The angle tolerance which influences the tessellation of curves with relatively small radii in comparison to the overall size of the CAD model.

<!-- @since:5.0.1 @type:Double @optional @default:0.01 -->
### `dPointCoincidentTolerance`

- The tolerance which influences the detection of coincident (connected) parts.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iConvertIsolatedCurve`

- The convert isolated curve option.
  - 0: Off
  - 1: On

<!-- @since:5.0.1 @type:Integer @optional @default:2 -->
### `iDekCleanselfintersectingloop`

- The option that detects and eliminates loops that are self-intersecting at vertex locations.
  - 0: Disable cleaning.
  - 2: Detect and eliminate self-intersecting loops at vertex locations.
  - 3: Detect and eliminate self-intersecting loops.

<!-- @since:5.0.1 @type:Integer @optional @default:4 -->
### `iDekVolumetopart`

- The number of volumes to part.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iIgesFixedCurvePreference`

- The calculation method of the trim curve. Using for IGES CAD type.
  - 0: Value in IGES file
  - 1: 2D Curve
  - 2: 3D Curve

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iIgesAutostitch`

- The option that control (on/off) filling the gaps of the IGES file without a topology. Using for IGES CAD type.
  - 0: Off
  - 1: On

<!-- @since:5.0.1 @type:Double @optional @default:0.1 -->
### `dIgesStitchtolerance`

- The tolerance for filling the gaps. Using for IGES CAD type.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iCatiaConvertNotShownElement`

- The option that controls the conversion of hidden elements. Using for CATIA CAD type.
  - 0: Off
  - 1: On

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iCatiaConvertNotShownInstance`

- The option that controls the conversion of hidden instances. Using for CATIA CAD type.
  - 0: Off
  - 1: On

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iCatiaConvertaxis`

- The option that controls the conversion of coordinate systems. Using for CATIA CAD type.
  - 0: Off
  - 1: On

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iStepCreateseam`

- The option that creates seam to topologies without an outer loop. Using for STEP CAD type.
  - 0: No Seam
  - 1: Dependent on CAD
  - 2: Add Seam

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dStepPointtolerance`

- The tolerance to check the same point. Using for STEP CAD type.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iAcisHealacisbeforeversion`

- The option using healing function. Using for ACIS CAD type.
  - 0: Off
  - 1: On

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iJtConvertgeometrytype`

- The target element type for conversion. Using for JT CAD type.
  - 0: Off
  - 1: Brep

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bFaceColor`

- The color information option.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iJtConvertgeneralpart`

- The option that control the conversion of the General Part types. Using for JT CAD type.
  - 0: Off
  - 1: On

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iJtConvertaxis`

- The option that control the conversion of coordinate systems. Using for JT CAD type.
  - 0: Off
  - 1: On

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iJtConvertcenterline`

- The option that control the conversion of the center line. Using for JT CAD type.
  - 0: Off
  - 1: On

## Return Code

A _Boolean_ specifying whether the function is executed successfully or not:

- True: The CAD file (IGES file, STEP file, etc.) is imported successfully.
- False: The CAD file (IGES file, STEP file, etc.) cannot be imported.

## Sample Code

```psj {1,2,3,4,5}
imported _status = Home.ImportCAD.Elysium(strlPaths=[JPT.GetProgramPath() +
                                                    "SampleData/CAD _Model/IGES/A400MA.igs"],
                                         dAngleToleranceDegree=3.0,
                                         dPointCoincidentTolerance=1e-05,
                                         dIgesStitchtolerance=0.01)
JPT.Debugger(imported _status)
```
