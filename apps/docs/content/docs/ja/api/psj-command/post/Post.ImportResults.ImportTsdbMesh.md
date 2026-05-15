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

<!-- @since:5.0.1 @required -->
### strTsdbFilePath

- Specify the tsdb file path.

<!-- @since:5.0.1 @required -->
### strBtxFilePath

- Specify the btx file path.

<!-- @since:5.0.1 @optional -->
### iImportType

- Specify the import type.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### dFaceAngle

- Specify the face angle.
- The default value is 60.0.

<!-- @since:5.0.1 @optional -->
### dEdgeAngle

- Specify the edge angle.
- The default value is 60.0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Post.ImportResults.ImportTsdbMesh(strTsdbFilePath, strBtxFilePath, iImportType=1, dFaceAngle=60.0, dEdgeAngle=60.0)
```
