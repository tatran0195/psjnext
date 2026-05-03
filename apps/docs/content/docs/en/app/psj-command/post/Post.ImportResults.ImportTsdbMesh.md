---
title: "Post.ImportResults.ImportTsdbMesh()"
description: "import tsdb mesh"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Post > ImportResults > ImportTsdbMesh"
---

## Description

Import tsdb mesh

## Syntax

```psj
Post.ImportResults.ImportTsdbMesh(strTsdbFilePath, strBtxFilePath, iImportType=1, dFaceAngle=60.0, dEdgeAngle=60.0)
```

## Inputs

### `strTsdbFilePath` @type(String) @required

- The tsdb file path.

### `strBtxFilePath` @type(String) @required

- The btx file path.

### `iImportType` @type(Integer) @default(1)

- The import type.

### `dFaceAngle` @type(Double) @default(60.0)

- The face angle.

### `dEdgeAngle` @type(Double) @default(60.0)

- The edge angle.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Post.ImportResults.ImportTsdbMesh(strTsdbFilePath, strBtxFilePath, iImportType=1, dFaceAngle=60.0, dEdgeAngle=60.0)
```
