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

<!-- @since:5.0.1 @type:String @optional @default:"SurfaceLoads1" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Double List @optional @default:[0,0,0] -->
### `dlPressure`

- The pressure.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iArrowDir`

- The arrow direction.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCoordinate`

- The coordinate.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargetsFace`

- The target face.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEditCur`

- The edit cur.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Geometry.Part.Cube()
BoundaryConditions.Pressure.SurfaceLoads(strName="SurfaceLoads1", dlPressure=[100,0,100], iArrowDir=0, crCoordinate=None, crlTargetFace=[Face(26)], crEditCur=None)
```
