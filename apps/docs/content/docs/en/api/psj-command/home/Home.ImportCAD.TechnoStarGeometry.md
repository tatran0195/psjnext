---
title: "Home.ImportCAD.TechnoStarGeometry()"
description: "Import Geometry bdf file"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Home > ImportCAD > TechnoStarGeometry"
macro _link: "[ImportGeomBDF](../../macro/home/ImportGeomBDF)"
---

## Description

Import Geometry by bdf file

## Syntax

```psj
Home.ImportCAD.TechnoStarGeometry(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[String] @optional @default:[] -->
### `strlPath`

- The path.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bUseUnit`

- The use unit.

## Return Code

A _String_ of 1 if successed, or 0 if failed.

## Sample Code

```psj {1}
Home.ImportCAD.TechnoStarGeometry(strlPath=[], bUseUnit=True)
```
