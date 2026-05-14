---
title: "Geometry.CADTrim()"
description: "CAD Trim"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > CAD Trim"
macro _link: "[GeometryCADTrim](../../macro/geometry/GeometryCADTrim)"
---

## Description

This method reduces the number of facets (triangle patch shape) for CAD shape. This can be obtained by recursively finding and collapsing adjacent element edges that are at an angle less than a specified angle or at an element edge length less than a specified size.

## Syntax

```psj
Geometry.CADTrim(crlFaces = [], crlParts = [], dTrimSize=1.0, dTrimAngle=15.0)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlFaces`

- The faces to be trimmed. Either _crlFaces_, or _crlParts_ must be specified.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlParts`

- The parts to be trimmed. Either _crlFaces_, or _crlParts_ must be specified.

<!-- @since:5.0.1 @type:Double @optional @default:1.0 -->
### `dTrimSize`

- The maximum length of element edge.

<!-- @since:5.0.1 @type:Double @optional @default:15.0 -->
### `dTrimAngle`

- The maximum angle in degrees between element edges.

## Return Code

A _String_ of 1 if success, or 0 if fail.

## Sample Code

```psj
Home.ImportCAD.Parasolid([JPT.GetProgramPath() + "SampleData\\bracket.x _t"],
    dAngleToleranceDegree=7.0, dScale=0.001)

Geometry.CADTrim(crlFaces=[Face(149)], crlParts=[Part(1)], dTrimSize=20.0, dTrimAngle=16.0)
```
