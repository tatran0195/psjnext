---
title: "Post.ImportResults.ImportTsdbMesh()"
description: "import tsdb mesh"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Post > ImportResults > ImportTsdbMesh"
---

## Description

Import tsdb mesh

## Syntax

```psj
Post.ImportResults.ImportTsdbMesh(strTsdbFilePath, strBtxFilePath, iImportType=1, dFaceAngle=60.0, dEdgeAngle=60.0)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `strTsdbFilePath`

- The tsdb file path.

<!-- @since:5.0.1 @type:String @required -->
### `strBtxFilePath`

- The btx file path.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iImportType`

- The import type.

<!-- @since:5.0.1 @type:Double @optional @default:60.0 -->
### `dFaceAngle`

- The face angle.

<!-- @since:5.0.1 @type:Double @optional @default:60.0 -->
### `dEdgeAngle`

- The edge angle.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Post.ImportResults.ImportTsdbMesh(strTsdbFilePath, strBtxFilePath, iImportType=1, dFaceAngle=60.0, dEdgeAngle=60.0)
```
