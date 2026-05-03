---
title: "Home.ImportCAD.TechnoStarGeometry()"
description: "Import Geometry bdf file"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Home > ImportCAD > TechnoStarGeometry"
macro_link: "[ImportGeomBDF](../../macro/home/ImportGeomBDF)"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Import Geometry by bdf file

## Syntax

```psj
Home.ImportCAD.TechnoStarGeometry(...)
```

## Inputs

### `strlPath` @type(List\[String]) @default(\[])

- The path.

### `bUseUnit` @type(Boolean) @default(True)

- The use unit.

## Return Code

A _String_ of 1 if successed, or 0 if failed.

## Sample Code

```psj {1}
Home.ImportCAD.TechnoStarGeometry(strlPath=[], bUseUnit=True)
```
