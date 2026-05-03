---
title: "BoundaryConditions.Pressure.SurfaceLoads()"
description: "create distrubited pressure"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > Pressure > SurfaceLoads"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create distrubited pressure.

## Syntax

```psj
BoundaryConditions.Pressure.SurfaceLoads(...)
```

## Inputs

### `strName` @type(String) @default("SurfaceLoads1")

- The name.

### `dlPressure` @type(Double List) @default(\[0,0,0])

- The pressure.

### `iArrowDir` @type(Integer) @default(0)

- The arrow direction.

### `crCoordinate` @type(Cursor) @default(None)

- The coordinate.

### `crlTargetsFace` @type(List\[Cursor]) @default(\[])

- The target face.

### `crEditCur` @type(Cursor) @default(None)

- The edit cur.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Geometry.Part.Cube()
BoundaryConditions.Pressure.SurfaceLoads(strName="SurfaceLoads1", dlPressure=[100,0,100], iArrowDir=0, crCoordinate=None, crlTargetFace=[Face(26)], crEditCur=None)
```
