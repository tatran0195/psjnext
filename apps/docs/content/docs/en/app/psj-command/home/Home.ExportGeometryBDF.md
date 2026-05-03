---
title: "Home.ExportGeometryBDF()"
description: "Export Geometry BDF file."
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Home > ExportGeometryBDF"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Unknown Description","Export Geometry BDF file."]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Export Geometry BDF file.

## Syntax

```psj
Home.ExportGeometryBDF(strFileName, crlParts=[], bBigID=False, bUseUnit=True, bVert=True, bEdge=True, bFace=True, bSolid=True)
```

## Inputs

### `strFileName` @type(String) @required

- The file name.

### `crlParts` @type(List\[Cursor]) @default(\[])

- The part.

### `bBigID` @type(Boolean) @default(False)

- The big ID.

### `bUseUnit` @type(Boolean) @default(True)

- The use unit.

### `bVert` @type(Boolean) @default(True)

- The vert.

### `bEdge` @type(Boolean) @default(True)

- The edge.

### `bFace` @type(Boolean) @default(True)

- The face.

### `bSolid` @type(Boolean) @default(True)

- The solid.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Home.ExportGeometryBDF(strFileName, crlParts=[], bBigID=False, bUseUnit=True, bVert=True, bEdge=True, bFace=True, bSolid=True)
```
