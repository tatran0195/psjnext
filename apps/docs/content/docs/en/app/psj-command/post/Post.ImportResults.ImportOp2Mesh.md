---
title: "Post.ImportResults.ImportOp2Mesh()"
description: "import Nastran op2 mesh"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Post > ImportResults > ImportOp2Mesh"
---

## Description

Import Nastran op2 mesh

## Syntax

```psj
Post.ImportResults.ImportOp2Mesh(strlFilePaths, iImportType=0, dFaceAngle=60.0, dEdgeAngle=60.0)
```

## Inputs

### `strlFilePaths` @type(List\[String]) @required

- The file paths.

### `iImportType` @type(Integer) @default(0)

- The import type.

### `dFaceAngle` @type(Double) @default(60.0)

- The face angle.

### `dEdgeAngle` @type(Double) @default(60.0)

- The edge angle.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Post.ImportResults.ImportOp2Mesh(strlFilePaths, iImportType=0, dFaceAngle=60.0, dEdgeAngle=60.0)
```
