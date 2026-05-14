---
title: "Home.ExportGeometryBDF()"
description: "Export Geometry BDF file."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Home > ExportGeometryBDF"
---

## Description

Export Geometry BDF file.

## Syntax

```psj
Home.ExportGeometryBDF(strFileName, crlParts=[], bBigID=False, bUseUnit=True, bVert=True, bEdge=True, bFace=True, bSolid=True)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `strFileName`

- The file name.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlParts`

- The part.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bBigID`

- The big ID.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bUseUnit`

- The use unit.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bVert`

- The vert.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bEdge`

- The edge.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bFace`

- The face.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bSolid`

- The solid.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Home.ExportGeometryBDF(strFileName, crlParts=[], bBigID=False, bUseUnit=True, bVert=True, bEdge=True, bFace=True, bSolid=True)
```
