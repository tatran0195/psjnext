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

<!-- @since:5.0.1 @required -->
### strlPaths

- Specify a list of the CAD files which will be used for importing.

<!-- @since:5.0.1 @optional -->
### dChordHeightTolerance

- Specify the maximum distance from the actual surface to the facet face. The smaller the Chord Height, the smaller the facets the more accurate the curvature of the surface is represented.
- The default value is 1.0.

<!-- @since:5.0.1 @optional -->
### dAngleToleranceDegree

- Specify the angle tolerance which influences the tessellation of curves with relatively small radii in comparison to the overall size of the CAD model.
- The default value is 5.0.

<!-- @since:5.0.1 @optional -->
### dPointCoincidentTolerance

- Specify the tolerance which influences the detection of coincident (connected) parts.
- The default value is 0.01.

<!-- @since:5.0.1 @optional -->
### iConvertIsolatedCurve

- Specify the convert isolated curve option.
  - 0: Off
  - 1: On
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iDekCleanselfintersectingloop

- Specify the option that detects and eliminates loops that are self-intersecting at vertex locations.
  - 0: Disable cleaning.
  - 2: Detect and eliminate self-intersecting loops at vertex locations.
  - 3: Detect and eliminate self-intersecting loops.
- The default value is 2.

<!-- @since:5.0.1 @optional -->
### iDekVolumetopart

- Specify the number of volumes to part.
- The default value is 4.

<!-- @since:5.0.1 @optional -->
### iIgesFixedCurvePreference

- Specify the calculation method of the trim curve. Using for IGES CAD type.
  - 0: Value in IGES file
  - 1: 2D Curve
  - 2: 3D Curve
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iIgesAutostitch

- Specify the option that control (on/off) filling the gaps of the IGES file without a topology. Using for IGES CAD type.
  - 0: Off
  - 1: On
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### dIgesStitchtolerance

- Specify the tolerance for filling the gaps. Using for IGES CAD type.
- The default value is 0.1.

<!-- @since:5.0.1 @optional -->
### iCatiaConvertNotShownElement

- Specify the option that controls the conversion of hidden elements. Using for CATIA CAD type.
  - 0: Off
  - 1: On
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iCatiaConvertNotShownInstance

- Specify the option that controls the conversion of hidden instances. Using for CATIA CAD type.
  - 0: Off
  - 1: On
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iCatiaConvertaxis

- Specify the option that controls the conversion of coordinate systems. Using for CATIA CAD type.
  - 0: Off
  - 1: On
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### iStepCreateseam

- Specify the option that creates seam to topologies without an outer loop. Using for STEP CAD type.
  - 0: No Seam
  - 1: Dependent on CAD
  - 2: Add Seam
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### dStepPointtolerance

- Specify the tolerance to check the same point. Using for STEP CAD type.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iAcisHealacisbeforeversion

- Specify the option using healing function. Using for ACIS CAD type.
  - 0: Off
  - 1: On
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iJtConvertgeometrytype

- Specify the target element type for conversion. Using for JT CAD type.
  - 0: Off
  - 1: Brep
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### bFaceColor

- Specify the color information option.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### iJtConvertgeneralpart

- Specify the option that control the conversion of the General Part types. Using for JT CAD type.
  - 0: Off
  - 1: On
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### iJtConvertaxis

- Specify the option that control the conversion of coordinate systems. Using for JT CAD type.
  - 0: Off
  - 1: On
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### iJtConvertcenterline

- Specify the option that control the conversion of the center line. Using for JT CAD type.
  - 0: Off
  - 1: On
- The default value is 0.

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
