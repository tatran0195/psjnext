---
title: "Geometry.CADTrim()"
description: "CAD Trim"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > CAD Trim"
macro_link: "[GeometryCADTrim](../../macro/geometry/GeometryCADTrim)"
---

## Description

This method reduces the number of facets (triangle patch shape) for CAD shape. This can be obtained by recursively finding and collapsing adjacent element edges that are at an angle less than a specified angle or at an element edge length less than a specified size.

## Syntax

```psj
Geometry.CADTrim(crlFaces = [], crlParts = [], dTrimSize=1.0, dTrimAngle=15.0)
```

## Inputs

### `crlFaces` @type(List\[Cursor]) @default(\[])

- Faces to be trimmed. Eithe&#x72;_&#x63;rlFaces_, o&#x72;_&#x63;rlPart&#x73;_&#x6D;ust be specified.

### `crlParts` @type(List\[Cursor]) @default(\[])

- Parts to be trimmed. Eithe&#x72;_&#x63;rlFaces_, o&#x72;_&#x63;rlPart&#x73;_&#x6D;ust be specified.

### `dTrimSize` @type(Double) @default(1.0)

- The maximum length of element edge.

### `dTrimAngle` @type(Double) @default(15.0)

- The maximum angle in degrees between element edges.

## Return Code

A _String_ of 1 if success, or 0 if fail.

## Sample Code

```psj
Home.ImportCAD.Parasolid([JPT.GetProgramPath() + "SampleData\\bracket.x_t"],
    dAngleToleranceDegree=7.0, dScale=0.001)

Geometry.CADTrim(crlFaces=[Face(149)], crlParts=[Part(1)], dTrimSize=20.0, dTrimAngle=16.0)
```
