---
title: "BoundaryConditions.Pressure.SurfaceLoads()"
description: "create distrubited pressure"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > Pressure > SurfaceLoads"
---

## Description

Create distrubited pressure.

## Syntax

```psj
BoundaryConditions.Pressure.SurfaceLoads(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "SurfaceLoads1".

<!-- @since:5.0.1 @optional -->
### dlPressure

- Specify the pressure.
- The default value is \[0,0,0].

<!-- @since:5.0.1 @optional -->
### iArrowDir

- Specify the arrow direction.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crCoordinate

- Specify the coordinate.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### crlTargetsFace

- Specify the target face.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crEditCur

- Specify the edit cur.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Geometry.Part.Cube()
BoundaryConditions.Pressure.SurfaceLoads(strName="SurfaceLoads1", dlPressure=[100,0,100], iArrowDir=0, crCoordinate=None, crlTargetFace=[Face(26)], crEditCur=None)
```
