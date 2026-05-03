---
title: "Home.ImportCAD.Elysium()"
description: "Import a CAD file by using Elysium interface to the Jupiter Database"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Home > Import CAD > Elysium"
---

## Description

Import a CAD file by using Elysium interface to the Jupiter Database.

## Syntax

```psj
Home.ImportCAD.Elysium(...)
```

## Inputs

### `strlPaths` @type(List\[String]) @required

- A list of the CAD files which will be used for importing.

### `dChordHeightTolerance` @type(Double) @default(1.0)

- The maximum distance from the actual surface to the facet face. The smaller the Chord Height, the smaller the facets the more accurate the curvature of the surface is represented.

### `dAngleToleranceDegree` @type(Double) @default(5.0)

- The angle tolerance which influences the tessellation of curves with relatively small radii in comparison to the overall size of the CAD model.

### `dPointCoincidentTolerance` @type(Double) @default(0.01)

- The tolerance which influences the detection of coincident (connected) parts.

### `iConvertIsolatedCurve` @type(Integer) @default(0)

- The convert isolated curve option.
  - 0: Off
  - 1: On

### `iDekCleanselfintersectingloop` @type(Integer) @default(2)

- The option that detects and eliminates loops that are self-intersecting at vertex locations.
  - 0: Disable cleaning.
  - 2: Detect and eliminate self-intersecting loops at vertex locations.
  - 3: Detect and eliminate self-intersecting loops.

### `iDekVolumetopart` @type(Integer) @default(4)

- The number of volumes to part.

### `iIgesFixedCurvePreference` @type(Integer) @default(0)

- The calculation method of the trim curve. Using for IGES CAD type.
  - 0: Value in IGES file
  - 1: 2D Curve
  - 2: 3D Curve

### `iIgesAutostitch` @type(Integer) @default(1)

- The option that control (on/off) filling the gaps of the IGES file without a topology. Using for IGES CAD type.
  - 0: Off
  - 1: On

### `dIgesStitchtolerance` @type(Double) @default(0.1)

- The tolerance for filling the gaps. Using for IGES CAD type.

### `iCatiaConvertNotShownElement` @type(Integer) @default(0)

- The option that controls the conversion of hidden elements. Using for CATIA CAD type.
  - 0: Off
  - 1: On

### `iCatiaConvertNotShownInstance` @type(Integer) @default(0)

- The option that controls the conversion of hidden instances. Using for CATIA CAD type.
  - 0: Off
  - 1: On

### `iCatiaConvertaxis` @type(Integer) @default(1)

- The option that controls the conversion of coordinate systems. Using for CATIA CAD type.
  - 0: Off
  - 1: On

### `iStepCreateseam` @type(Integer) @default(1)

- The option that creates seam to topologies without an outer loop. Using for STEP CAD type.
  - 0: No Seam
  - 1: Dependent on CAD
  - 2: Add Seam

### `dStepPointtolerance` @type(Double) @default(0.0)

- The tolerance to check the same point. Using for STEP CAD type.

### `iAcisHealacisbeforeversion` @type(Integer) @default(0)

- The option using healing function. Using for ACIS CAD type.
  - 0: Off
  - 1: On

### `iJtConvertgeometrytype` @type(Integer) @default(1)

- The target element type for conversion. Using for JT CAD type.
  - 0: Off
  - 1: Brep

### `bFaceColor` @type(Boolean) @default(False)

- The color information option.

### `iJtConvertgeneralpart` @type(Integer) @default(1)

- The option that control the conversion of the General Part types. Using for JT CAD type.
  - 0: Off
  - 1: On

### `iJtConvertaxis` @type(Integer) @default(1)

- The option that control the conversion of coordinate systems. Using for JT CAD type.
  - 0: Off
  - 1: On

### `iJtConvertcenterline` @type(Integer) @default(0)

- The option that control the conversion of the center line. Using for JT CAD type.
  - 0: Off
  - 1: On

## Return Code

A _Boolean_ specifying whether the function is executed successfully or not:

- True: The CAD file (IGES file, STEP file, etc.) is imported successfully.
- False: The CAD file (IGES file, STEP file, etc.) cannot be imported.

## Sample Code

```psj {1,2,3,4,5}
imported_status = Home.ImportCAD.Elysium(strlPaths=[JPT.GetProgramPath() +
                                                    "SampleData/CAD_Model/IGES/A400MA.igs"],
                                         dAngleToleranceDegree=3.0,
                                         dPointCoincidentTolerance=1e-05,
                                         dIgesStitchtolerance=0.01)
JPT.Debugger(imported_status)
```
