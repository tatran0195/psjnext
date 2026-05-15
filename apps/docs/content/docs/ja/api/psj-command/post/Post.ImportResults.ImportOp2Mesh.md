---
title: "Post.ImportResults.ImportOp2Mesh()"
description: "import Nastran op2 mesh"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Post > ImportResults > ImportOp2Mesh"
---

## Description

Import Nastran op2 mesh

## Syntax

```psj
Post.ImportResults.ImportOp2Mesh(strlFilePaths, iImportType=0, dFaceAngle=60.0, dEdgeAngle=60.0)
```

## Inputs

<!-- @since:5.0.1 @required -->
### strlFilePaths

- Specify the file paths.

<!-- @since:5.0.1 @optional -->
### iImportType

- Specify the import type.
- The default value is 0.

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
Post.ImportResults.ImportOp2Mesh(strlFilePaths, iImportType=0, dFaceAngle=60.0, dEdgeAngle=60.0)
```
