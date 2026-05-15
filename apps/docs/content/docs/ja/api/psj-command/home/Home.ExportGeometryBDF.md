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

<!-- @since:5.0.1 @required -->
### strFileName

- Specify the file name.

<!-- @since:5.0.1 @optional -->
### crlParts

- Specify the part.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### bBigID

- Specify the big ID.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### bUseUnit

- Specify the use unit.
- The default value is _True_.

<!-- @since:5.0.1 @optional -->
### bVert

- Specify the vert.
- The default value is _True_.

<!-- @since:5.0.1 @optional -->
### bEdge

- Specify the edge.
- The default value is _True_.

<!-- @since:5.0.1 @optional -->
### bFace

- Specify the face.
- The default value is _True_.

<!-- @since:5.0.1 @optional -->
### bSolid

- Specify the solid.
- The default value is _True_.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Home.ExportGeometryBDF(strFileName, crlParts=[], bBigID=False, bUseUnit=True, bVert=True, bEdge=True, bFace=True, bSolid=True)
```
